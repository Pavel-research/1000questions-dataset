from textx.metamodel import metamodel_from_str
from textx.model import children_of_type
import yaml;
import vocabulary;
import os

loc=os.path.dirname(__file__)

grammar = """
Model: seq = Call ('=>' (seq*=Call  ))* ;
Call:  name= ID   '('args= ArgList ')' (op='?')? ;
ArgList: a= Arg? ( ',' a*=Arg) *;
Name: v= ID ;
Arg:
  (v =  Model | v =  INT | v =  Name | v =  BOOL | v =  STRING ) (m ='^')?;
"""


transformModel = metamodel_from_str(grammar)

class QueryModel:
    def v(self):
        print "A"
def setfunc(*arg):
  return QueryModel();
def orFunc(*arg):
    return QueryModel();
def andFunc(*arg):
    return QueryModel();
def notFunc(*arg):
    return QueryModel();
def propFunc(v,pn):
    assert isinstance(pn,vocabulary.PropertyTerm)
    if not isinstance(v,QueryModel) and not isinstance(v, str):
        raise ValueError(v);
def select(cn):
    assert isinstance(cn,vocabulary.ClassTerm);
    return QueryModel()
def filter(p,v,op):
    if isinstance(v,str):
        r=currentQuery.find(v)
        if (r==-1 and v!="*"):
             raise ValueError(v)

    assert op in ['in','not in','in all','not in all',"<",">",">=","<=","count>","count<","count=="]
    assert isinstance(p,vocabulary.PropertyTerm);
    if not isinstance(v,QueryModel) and not isinstance(v, str)and not isinstance(v, int):
        raise ValueError(v);
    return QueryModel()

def filterQuery(p,v,op):
    if isinstance(v,str):
        r=currentQuery.find(v)
        if (r==-1 and v!="*"):
            raise ValueError(v)

    assert op in ['in','not in','in all','not in all',"<",">",">=","<=","count>","count<","count=="]
    assert isinstance(p,QueryModel);
    if not isinstance(v,QueryModel) and not isinstance(v, str)and not isinstance(v, int):
        raise ValueError(v);
    return QueryModel()

def orderBy(p,op):

    assert op in ["<",">","count>","count<"]
    assert isinstance(p,vocabulary.PropertyTerm) or isinstance(p,QueryModel);
    return QueryModel()

def count_compare(v0,v,op):

    assert op in ["<",">",">=","<=","="]
    if not isinstance(v,QueryModel) and not isinstance(v, str)and not isinstance(v, int):
        raise ValueError(v);
    if not isinstance(v0,QueryModel) and not isinstance(v0, str):
        raise ValueError(v);

    return QueryModel()

def filter_related(v):
    if isinstance(v,str):
        r=currentQuery.find(v)
        if (r==-1):
            raise ValueError(v)
    if not isinstance(v,QueryModel) and not isinstance(v, str):
        raise ValueError(v);
    assert True;
def count():
    return
def inverseOf(p):
    assert isinstance(p,vocabulary.PropertyTerm);
    return p;
def orderByPassCount(s):
    return QueryModel();

symbols={
    "SELECT": select,
    "FILTER": filter,
    "FILTER_QUERY": filter,
    "ORDER_BY": orderBy,
    "COUNT_COMPARE": count_compare,
    "FILTER_RELATED": filter_related,
    "set": setfunc,
    "or": orFunc,
    #"and": andFunc,
    "intersect": andFunc,
    "inverseOf": inverseOf,
    "not": notFunc,
    "COUNT":count,
    "CONTEXT":count,
    "FIRST":count,
    "MAX":count,
    "MIN":count,
    "LAST":count,
    "ORDER_BY_PASSING_COUNT": orderByPassCount,
    "PROPERTY" : propFunc,
    "MAP_BY_PROPERTY": inverseOf
}

class QueryComposer:

    def __init__(self,str,voc):
        self.str=str;
        self.voc=voc;
    def parseArg(self,el,vars):
        kind=type(el).__name__;
        if (kind=="Call"):
            return self.parseElement(el,vars);
        if (kind=="Name"):
            if el.v in self.voc.classTerms:
                return self.voc.classTerms[el.v]
            if el.v in self.voc.propertyTerms:
                return self.voc.propertyTerms[el.v]

            raise ValueError(el.v)
        if (kind=="Model"):
            return self.composeFromModel(el);
        return el;
    def parseArgList(self,el,vars):
        res=[];
        if el==None:
            return res;
        for a in el.a:
            res.append(self.parseArg(a.v,vars))
        return res;

    def parseElement(self,el,vars):
        const=None;
        if (el.name  in symbols):
            const=symbols[el.name];
        else: raise ValueError(el.name)
        args=self.parseArgList(el.args,vars);
        return const(*args);
    def composeFunction(self,str,vars):
        model=transformModel.model_from_str(str);
        return self.composeFromModel(model, vars)

    def composeFromModel(self, model):
        chElements = [];
        for el in model.seq:
            fv=self.parseElement(el, vars);
            if (fv!=None):
                chElements.append(fv);
        if (len(chElements)==1):
            return chElements[0]
        return QueryModel()

currentQuery=""
with open(loc+"/questions.txt") as f:
    num = 0
    for line in f:
        if (line[0]=='!'):
            ont=vocabulary.Vocabulary(loc+"/"+line[1:len(line)-1])
            continue
        if not line.strip():
            continue;
        if (line[0]=='#'):
            continue;
        vl=line.index('=');

        question=line[0:vl]
        flow=line[vl+1:len(line)]
        #try:
        currentQuery=question;
        mq=transformModel.model_from_str(flow);
        QueryComposer(question,ont).composeFromModel(mq)
        num =  num +1;
    print str(num)+" questions are validated"
