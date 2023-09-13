#finding minimum with quadratic O(n^2) approach
#Here iteration goes on multiple times
nums=[98,56,90,54,87]
def find_min_quadratic(nums):
    if not nums:
        return None

    for i in range(len(nums)):
        is_min = True
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                is_min = False
                break
        if is_min:
            return nums[i]
print(find_min_quadratic(nums))

#output: 54

#finding minimum with linear O(n) approach
#Here iteratuion goes on only once
nums=[98,56,90,54,87]
def find_min_linear(nums):
    if not nums:
        return None

    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num
print(find_min_linear(nums))

#Output: 54
