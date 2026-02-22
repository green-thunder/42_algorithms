def rotate(nums, k):
    n = len(nums)
    k = k % n  # k ni massiv uzunligiga moslash
    
    # 1. Butun massivni teskari qilish
    reverse(nums, 0, n - 1)
    # 2. Birinchi k ta elementni teskari qilish
    reverse(nums, 0, k - 1)
    # 3. Qolgan elementlarni teskari qilish
    reverse(nums, k, n - 1)


    return nums

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result = rotate(nums, k)

    print(result)
    


