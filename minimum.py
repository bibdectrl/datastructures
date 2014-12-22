def lin_min(nums):
    mini = nums[0]
    for num in nums:
        if num < mini:
            mini = num
    return mini

def expo_min(nums):
    for i in nums:
        mini = i
        for j in nums:                     
            if j < i:
                mini = None
        if mini:
            return mini


print expo_min([3, 6, 2, 12, 75, 34, 1, 2, 5])
