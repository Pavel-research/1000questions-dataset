class BaseElement:

    def __repr__(self):
        return str(self);

    def canAppend(self,element):
        return True


class AbstractFilter(BaseElement):
    def resultType(self,input):
        return input;

class MapProperty(BaseElement):

    NAME="MAP_BY_PROPERTY"


    def __init__(self,prop):
        self.prop=prop;

    def resultType(self,input):
        return self.prop.range();

class NumberElement(BaseElement):

    def resultType(self,input):
        return input

class Min(NumberElement):

    NAME="MIN"

    def calc(self,input,ct):
        return min(input)

class Max(NumberElement):

    NAME="MAX"

    def calc(self,input,ct):
        return max(input)

class Average(NumberElement):

    NAME="AVERAGE"

    def calc(self,input,ct):
        return sum(input)/len(input)

class Sum(NumberElement):

    NAME="SUM"

    def calc(self,input,ct):
        return sum(input)

class Count(NumberElement):

    NAME="COUNT"

    def calc(self,input,ct):
        return len(input)
    def resultType(self,input):
        return int

class Flow(BaseElement):

    def __init__(self):
        self.seq=[];

    def resultType(self,input):
        for v in self.seq: input=v.resultType(input);
        return input

operators=[Count,Sum,Average,Min,Max,MapProperty]