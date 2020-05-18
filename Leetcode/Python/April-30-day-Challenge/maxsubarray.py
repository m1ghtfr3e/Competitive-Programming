
def findMax(arr):

    result = []

    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            if arr[i:j]:           #all possible subarrays
                possibles = sum(arr[i:j])    #sum of subarrays
                result.append(possibles)
                result = sorted(result)
                
    if len(result) > 1:
        return result[-1]
    else:
        return result[0]


if __name__ == '__main__':

    print(findMax(arr = [-2,1,-3,4,-1,2,1,-5,4]))            
