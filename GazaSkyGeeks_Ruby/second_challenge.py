def find_missing_numbers_from_perfect_range(nums):

    perfect_range = set(range(min(nums), max(nums) + 1))#use set because it doesn't allow duplicates
    missing_numbers = perfect_range - set(nums)
    return sorted(list(missing_numbers))

nums = [2, 1, 5, 4, 6, 9, 7, 8, 10]
missing = find_missing_numbers_from_perfect_range(nums)
print("Missing numbers:", missing)

nums = [11,2, 1, 5, 4, 9, 7, 8, 10]
missing = find_missing_numbers_from_perfect_range(nums)
print("Missing numbers:", missing)
