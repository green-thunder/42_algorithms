# Algorithms Practice

Algorithm and data structure problems solved in Python, grouped by topic, plus a small helper for benchmarking different solutions.

## Problems

| Folder | Problems |
|---|---|
| `problems/arrays` | generate, leftRightDifference, maxArea, move_zeroes, productExceptSelf, rotate, sortedSquares |
| `problems/linked_list` | linked list implementation, addTwoNumbers, hasCycle, isPalindrome, mergeTwoLists, middle_node, removeNthFromEnd, reverse |
| `problems/strings` | detectCapitalUse, isValid, lengthOfLongestSubstring, longestCommonPrefix, longestPalindrome, reverseString |

## Benchmarking solutions

`performance_tester.py` runs several implementations on the same input and prints the average time of each, the fastest one, and how much slower the others are. It can run them one after another or in parallel processes.

```python
from performance_tester import PerformanceTester

tester = PerformanceTester(trials=20)
tester.compare_all([solution_a, solution_b], data_source)       # sequential
tester.compare_parallel([solution_a, solution_b], data_source)  # parallel
```

`data_source` is a list or a function that returns one. For parallel mode, the functions must be defined at module level.

## Setup

```bash
pip install -r requirements.txt
```
