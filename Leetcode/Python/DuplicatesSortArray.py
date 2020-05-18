# remove duplicates from sorted array

def removeDuplicates(nums):
    #return len(set(nums))


    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
        nums[i] = nums[j]

    return i + 1


if __name__ == '__main__':

    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))