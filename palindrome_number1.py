def isPlindrome(x):
    '''
    if you are thinking of converting the integer to a string, note
    the restriction of using extra space.
    so blow is not pefect.
    '''
    i = 1
    x = str(x)
    sign = True
    while i < len(x) and sign:
        if x[i - 1] == x[-i]:
            i = i + 1
        else:
            sign = False
    return sign
