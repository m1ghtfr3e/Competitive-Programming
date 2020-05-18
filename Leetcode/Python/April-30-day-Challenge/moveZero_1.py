#move zeroes another approach

def moveZeroes(nums):

    orig_length = len(nums)
    
    
    
    #arr = [0] * len()
    
    [nums.remove(i) for i in nums if i == 0]
    
    nums += [0] * (orig_length - len(nums))
    return nums
   
   
def testing(nums=[0,0,1]):
    
    orig = len(nums)
    for i in nums:
        for j in nums:
            if i == 0:
                nums.remove(i)
    nums += [0] * (orig-len(nums))
    return nums   
   
 
def testing1(nums=[0,0,1]):
 
    orig = len(nums)
    nums = [n for n in nums if n != 0] + [0]
    return nums
 
 
if __name__ == '__main__':

    #print(moveZeroes([0,0,1]))
    
    print(testing1())
