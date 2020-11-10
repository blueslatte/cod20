def twoSum(nums, target):
    for i in range(len(nums) - 1):
        print(len(nums))
        for j in range(i + 1, len(nums)):
            print([i, j])
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum([3, 2, 4], 6))
