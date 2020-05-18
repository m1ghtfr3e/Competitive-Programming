def dont_give_me_five(start,end):
    
    arr = [i for i in range(start, end+1) if (i % 5 != 0) or (i % 2 == 0)]
    print(arr)
    return len(arr)


if __name__ == '__main__':

    print(dont_give_me_five(30, 51))