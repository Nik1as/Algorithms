def min_iterative(nums):
    min_value = nums[0]
    for e in nums:
        if e < min_value:
            min_value = e
    return min_value


def min_recursive(nums):
    def find_min(left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_min = find_min(left, mid)
        right_min = find_min(mid + 1, right)
        return left_min if left_min <= right_min else right_min

    return find_min(0, len(nums) - 1)


if __name__ == '__main__':
    print(min_iterative([1, 4, 23, 453, 2, 25]))
    print(min_recursive([1, 4, 23, 453, 2, 25]))
