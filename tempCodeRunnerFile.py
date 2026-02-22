import random
from performance_tester import PerformanceTester



def move_zeroes_gemini(nums: list):
    none_zeroes = [x for x in nums if x != 0]
    zeroes = [0] * (len(nums) - len(none_zeroes))

    return none_zeroes + zeroes


def move_zeroes_trash(nums: list):
    zeroes = nums.count(0)

    for i in range(zeroes):
        nums.remove(0)
        nums.append(0)

    return nums

def move_zeroes_42(nums):
    count = 0 
    for i, num in enumerate(nums):
        if num == 0:
            count += 1
            continue
        nums[i], nums[i - count] = nums[i - count], nums[i]
    return nums

def move_zeroes_my(nums):
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
    return nums

size = 10000
trials = 50

tester = PerformanceTester(trials)
methods = [move_zeroes_42, move_zeroes_my, move_zeroes_trash, move_zeroes_gemini]

data = [random.choice([0, 0, 1, 2, 3, 4, 5]) for _ in range(size)]


tester.compare_all(methods, data)