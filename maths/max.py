def max_iterative(nums):
    max_value = nums[0]
    for e in nums:
        if e > max_value:
            max_value = e
    return max_value


def max_recursive(nums):
    def find_max(left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_max = find_max(left, mid)
        right_max = find_max(mid + 1, right)
        return left_max if left_max >= right_max else right_max

    return find_max(0, len(nums) - 1)


if __name__ == '__main__':
    print(max_iterative([1, 4, 23, 453, 2, 25]))
    print(max_recursive([1, 4, 23, 453, 2, 25]))
