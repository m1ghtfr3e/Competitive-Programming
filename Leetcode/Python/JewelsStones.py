def numJewelsInStones(J, S):
    juwels = list(J)
    stones = list(S)
    
    count_juwels = 0
    for i in stones:
        if i in juwels:
            count_juwels += 1

    return count_juwels




if __name__ == '__main__':

    '''
    Example: 
        Input: J = "aA", S = "aAAbbbb"
        Output: 3
    '''

    print(numJewelsInStones('aA', 'aAAbbbb'))