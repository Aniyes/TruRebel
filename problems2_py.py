'''
Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
'''

def count_evens(num_list):
    '''
    >>> count_evens([2,4,5,6,7])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1,3,5,7,9])
    0
    '''
    counter = 0

    for i in num_list:
        if i % 2 == 0:
            counter += 1
    return counter
    pass


'''
Given an integer list return True if it contains a 2  or a 3
'''
def has23(num_list):
    '''
    >>> has23([2,4,6,7])
    True
    >>> has23([0,0,0,1,4])
    False
    >>> has23([2,3,2,3])
    True
    '''
    for i in num_list:
        if i == 2 or 3:
            return True
        elif i != 2 or 3:
            return False

    pass

'''
Return the sum of the numbers in the array,
returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count
'''
def sum13(num_list):
    '''
    >>> sum13([])
    0
    >>> sum13([1,2,3,4])
    10
    >>> sum13([1,13,4,13,5,13])
    10
    >>> sum13([13,13,13,13])
    0
    '''
    pass

if __name__ == '__main__':
    import doctest

    #uncomment the following line to test the count_evens function
    #doctest.run_docstring_examples(count_evens, globals())

    #uncomment the following line to test the has23 function
    doctest.run_docstring_examples(has23, globals())

    #uncomment the following line to test the sum13 function
    #doctest.run_docstring_examples(sum13, globals())
