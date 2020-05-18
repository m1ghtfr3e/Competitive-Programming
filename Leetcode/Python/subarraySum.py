def subarraySum(nums, k):

    sub = []
    for i in range(len(nums)+1):
        for j in range(i, len(nums)+1):
            if sum(nums[i:j]) == k:
                sub.append(nums[i:j])
    print(sub)
    if len(sub[0]) > 1:
        return len(sub)
    else:
        return len(sub[0])



if __name__ == '__main__':
    print(subarraySum([1,1], 0))
