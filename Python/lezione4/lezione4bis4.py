from collections import Counter
def majority_element(nums: list[int]) -> int:
    """
        Data una lista nums di n elementi, restituire
        l'elemento che compare più di n/2 volte

        Esempio 1:
        nums = [3,2,3] -> restituire 3

        Esempio 2:
        nums =[2,2,1,1,1,2] -> restituire Nne
    """

    maxCount = 0
    index = -1
    for i in range(nums):
        count = 1
        for j in range(i+1, nums):
            if(nums[i] == nums[j]):
                count += 1
        if(count > maxCount):
            maxCount = count
            index = i
    if(maxCount > nums/2):
        print(nums[index])
    else:
        print("No Majority Element")
    

    for i in nums:
        if nums.count(i) > len(nums) / 2:
            return i
    return None

    
""""
    d: dict[int, int] = dict(Counter(nums))
    for i in nums:
        d[i] = nums.count(i)
    



    length = len(nums)
    for key in d:
        d[key] /= length
        if d[key] > 0.5:
            return key
    return None
    """