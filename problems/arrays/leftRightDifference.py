def leftRightDifference(nums: list) -> list:
    total_sum = sum(nums)
    left_sum = 0
    result = []

    for i in range(len(nums)):
        master_force = nums[i]
        right_sum = total_sum - left_sum - master_force

        if left_sum > right_sum:
            result.append(-1)
        elif right_sum > left_sum:
            result.append(1)
        else:
            result.append(0)

        left_sum += master_force
    
    return result


if __name__ == "__main__":
    nums = [10, 4, 8, 3]
    result = leftRightDifference(nums)

    print(result)