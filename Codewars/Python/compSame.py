# Same means: array1 is squares of array2
# If elements in array2->square are elements in array1

def comp(arr1, arr2):

    if arr1 == 0 or arr2 == 0 or arr1 == None or arr2 == None:
        return False
    else:

        arr1 = [i*i for i in arr1]
        
        if sorted(arr1) == sorted(arr2):
            return True
        else:
            return False



if __name__ == '__main__':

    a = [121, 144, 19, 161, 19, 144, 19, 11]  
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

    print(comp(a, b))