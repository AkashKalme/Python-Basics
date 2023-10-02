# Docstrings
def test(a):
    '''
    Info: This function tests and prints parameter 'a'.
    '''
    print(a)


test('xyz')
help(test)
print(test.__doc__)
