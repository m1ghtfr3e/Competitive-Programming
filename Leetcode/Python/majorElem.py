# Find the major element
# -> Element which appers more than n/2

def majorityElement(nums):
    m = (len(nums) / 2)
    for n in nums:
        if nums.count(n) > m:
            return n




if __name__ == '__main__':

    print(majorityElement([2,2,1,1,1,2,2,]))
