def sum_of_minimums(numbers):
    res = 0
    for arr in numbers:
        smallest = min(arr)
        res += smallest
    return res



if __name__ == '__main__':

    matrix = [
        [1,2,3,4,5],
        [5,6,7,8,9],
        [20,21,34,56,100],
    ]

    print(sum_of_minimums(matrix))