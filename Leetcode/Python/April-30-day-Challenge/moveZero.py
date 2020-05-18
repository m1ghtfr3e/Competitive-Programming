# move zeros

def moveZeros(nums):

    orig_length = len(nums)

    for i in nums:
        if i == 0:
            nums.remove(i)

    diff = orig_length - len(nums)
    zeroes = [0] * diff
    
    return nums + zeroes  
    
    
if __name__ == '__main__':

    print(moveZeros([0,0,1]))
    
    # test cases:
    #[0,1,0,3,12]
