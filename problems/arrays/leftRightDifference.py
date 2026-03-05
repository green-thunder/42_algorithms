def leftRightDifference(nums: list) -> list:
    total_sum = sum(nums)
    left_sum = 0
    result = []

    for num in nums:
        right_sum = total_sum - left_sum - num

        if left_sum > right_sum:
            result.append(-1)
        elif right_sum > left_sum:
            result.append(1)
        else:
            result.append(0)

        left_sum += num
    
    return result


def sign(diff):
    if diff > 0:
        return 1
    elif diff < 0:
        return -1

    return 0


def leftRightDifference42(nums: list) -> list:
    left, right = 0, sum(nums)
    result = []

    for num in nums:
        right -= num
        result.append(sign(right - left))
        left += num

    return result


if __name__ == "__main__":
    nums = [10, 4, 8, 3]
    result = leftRightDifference42(nums)

    print(result)   