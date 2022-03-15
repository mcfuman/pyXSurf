
"""
Extensible vectorizable list.

In final version has list properties `iterators`,
`aggregator`,`expanded` containing methods that are vectorized in different ways. Iterator is default, return a list with each element obtained by applying its method with same name to each element of `superlist`.
Aggregator accumulate a binary operation, returning a single value. Expanded return a single element by passing the content of `superlist` as n elements to the element method.
Note that passing parameters must be handled accordingly. In particular a list of parameters or a single value can be passed to iterators, however this can create ambiguity. For example, an element method can accept list or single values, so it is not clear when a list is passed to superlist, if this means that the same list is passed to all elements as list argument of element method, rather than passing each element of list argument as scalar argument of elements method. There is no ambiguity if a list of lists or a list with len different from number of superlist elements, this should be checked, otherwise a warning should be visualized telling about the possible ambiguity and default action (possibly passing one value per element, call with nested list [[element]] to apply as list to all values).

In this experimental version, different ways to access object methods are tested.

functions operating on a list of Data2D objects

2020/05/26 moved to dataIO"""
# turned into a class derived from list 2020/01/16, no changes to interface,
# everything should work with no changes.


class Superlist(list):
    """A list of pySurf.Data2D objects on which unknown operations are performed serially."""

    def __getattr__(self,name,*args,**kwargs):
            # devo costruire una nuova funzione che preso un oggetto
            # lista ritorna un oggetto lista ottenuto dal valore restituito dalla funzione su ogni elemento.
            def newfunc(*args, **kwargs):
                attr = [object.__getattribute__(name) for object in self]
                result = [a(*args, **kwargs) if hasattr(attr, '__call__') else a for a in attr]
                return result
            return newfunc




def test_superlist(cls,obj=None):

    print ('test class ',cls)
    if obj is None:
        #s=type(cls,[np.arange(4),np.arange(3)])
        s = cls([np.arange(4),np.arange(3)])
        #s = superlist([np.arange(4),np.arange(3)])

    print('original data:')
    print(s)
    print('\ntest property (np.shape):')
    print(s.shape)
    print('\ntest method (np.flatten):')
    print(s.flatten())

