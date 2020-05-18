
def moveZero(nums):

    x = 0        # we use it as a pointer
    for i in nums:
        if i != 0:
            nums[x] = i
            x += 1
        
    for i in range(x, len(nums)):
        nums[i] = 0
    
    return nums
    
if __name__ == '__main__':

    print(moveZero([0,1,0,3,12]))
    print(moveZero([0,0,1]))
