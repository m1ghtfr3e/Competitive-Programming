def xo(test):
    countX = 0
    countO = 0
    for char in test:
        if char == 'x' or char == 'X':
            countX += 1
        if char == 'o' or char == 'O':
            countO += 1
        else:
            pass
    
    if countO == countX:
        return True
    elif countO == 0 and countX == 0:
        return True
    else:
        return False




if __name__ == '__main__':

    print(xo('xxoooo'))