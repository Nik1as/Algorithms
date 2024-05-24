def median(nums):
    sorted_nums = sorted(nums)
    length = len(sorted_nums)
    mid = length // 2
    return (sorted_nums[mid] + sorted_nums[mid - 1]) / 2 if length % 2 == 0 else sorted_nums[mid]


if __name__ == '__main__':
    print(median([1, 324, 5, 23, 3, 47, 9, 54]))
    print(median([1, 324, 5, 23, 3, 47, 9]))
