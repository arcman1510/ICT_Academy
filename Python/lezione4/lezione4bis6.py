def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # nums1 = []
    # nums2 = []
    # return [1,2]

    list_set:list = []
    for i in nums1:
        if i in nums2:
            list_set.append(i)
        else:
            continue

    return set(list_set)

print(intersection([2,2,4,2,1], [1,1,2,0,2,1,2]))