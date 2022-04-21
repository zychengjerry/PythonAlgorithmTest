def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j >= 0:
        return [j,i]

def twoSumAdv(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

def test():
    assert twoSumAdv([2,7,11,15], 9) == [0,1]
    assert twoSumAdv([3,2,4], 6) == [1,2]
    assert twoSumAdv([3,3], 6) == [0,1]

    print("all tests passed")

test()