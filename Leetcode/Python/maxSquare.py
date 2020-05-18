''' Find max square in matrix

0, 0, 1, 0
0, 1, 1, 0
0, 1, 1, 1
1, 0, 0, 1
'''

def maximalSquare(matrix):
    
    for i in range(0, len(matrix)+1):
        for n in matrix:
            print(n)


    #return count





if __name__ == '__main__':

    matrix = [
        [0, 0, 1, 0],
        [1, 0, 1, 1],
        [0, 0, 1, 1],
    ]

    print(maximalSquare(matrix))