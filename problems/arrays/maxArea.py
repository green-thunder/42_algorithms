def maxArea(nums: list) -> int:
    max_v = 0
    l, r = 0, len(nums) - 1

    while l < r:
        width = r - l 
        current_area = min(nums[l], nums[r]) * width
        max_v = max(max_v, current_area)

        if nums[l] > nums[r]:
            r -= 1
        else:
            l += 1

    return max_v


if __name__ == "__main__":

    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Result: {maxArea(nums)}")