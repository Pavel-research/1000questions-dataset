# 1000questions-dataset



* `SELECT (classname)`: returns instances of class and its subclasses
* `FILTER (propName, value_or_query, operator)`: filters passed value by comparing its property 
values with members of `value_or_query` comparison operation is determined by value of `operator'. If there is no current 
 argument filter is executed against all known entities
* `FILTER_RELATED(value_or_query)`: Filters values which are related to values in `value_or_query` If there is no current 
   argument filter is executed against all known entities
* `COUNT()`: returns total number of passed values,
* `PROPERTY(value_or_query,property)` : return particular property or properties of the instance or
instances passed in `value_or_query` argument

* `inverseOf(property)`: returns inversion of given property

* `COUNT_COMPARE(filters,number_or_query,op)` compares number of results of executing `filters` against current values with
   `number_or_query` supported operations: >,<,>=,<=,!=,=

* `or(filter1,filter2..)` executes number of filters against current values and passes them if any filter match
* `not(filter)` executes filter against current values and passes them if filter does not matches

* `ORDER_BY(property,op)` sorts results by the property op can be '>','<'

* `FIRST()` returns first element of argument

* `LAST()` returns last element of argument

* ` MAX()` returns maximum of argument

* `MIN()` returns minumum of argument

* `MAP_BY_PROPERTY(property)` maps input by property same as PROPERTY but with sequencial flow of arguments

* `set(query_or_value,query_or_value1,...)` union of values or query results

* `FILTER_QUERY(q,value_or_query,operator)` - extended version of `FILTER` instead of filteting by property value filters 
   against results of query which is executed for each of filtered elements


"and": andFunc,
