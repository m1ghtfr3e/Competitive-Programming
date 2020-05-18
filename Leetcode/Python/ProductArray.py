import math

def productExceptSelf(nums):
    
    subs = []
    for n, i in enumerate(nums):
        tmp = [n for n in nums]
        tmp.remove(i)
        subs.append(tmp)
    products = []
    for elem in subs:
        products.append(math.prod(elem))
    return products

#better solution:
def productExcSelf(nums):
    subs = []

    for i in nums:
        tmp = [n for n in nums]
        tmp.remove(i)
        subs.append(math.prod(tmp))

    return subs
    
def productExcSelf1(nums):

    eachprod = []
    prod = 1
    for num in nums:
        eachprod.append(prod)
        prod = prod * num
    
    r = []
    prod = 1
    for num in reversed(nums):
        r.append(prod)
        prod = prod * num
      
    solution = []
        
    for prod in eachprod:
        solution.append(prod)
        
        i = 0
    for prod in reversed(r):
        solution[i] *= prod
        i += 1
        
    return solution



if __name__ == '__main__':

    #productExceptSelf([1,2,3,4])
    #productExcSelf([1,2,3,4])
    print(productExcSelf1([1,2,3,4]))