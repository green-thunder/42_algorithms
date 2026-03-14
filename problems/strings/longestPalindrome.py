def expand_42(s, i, j):
    n = len(s)

    while i >= 0 and j < n and s[i] == s[j]:
        i -= 1
        j += 1

    return s[i + 1: j]

def expand_around_center(s, left, right):
  while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1

  return right - left - 1

def longestPalindrome_my(s: str) -> str:
  if not s:
    return ""  
  start, end = 0, 0

  for i in range(len(s)):
    len1 = expand_around_center(s, i, i)
    len2 = expand_around_center(s, i, i + 1)

    max_len = max(len1, len2)

    if max_len > (end - start + 1):
      start = i - (max_len - 1) // 2
      end = i + max_len // 2

  return s[start : end + 1]


def longestPalindrome_42(s):
    n = len(s)
    answer = ''

    for i in range(n):
        pal_odd = expand_42(s, i, i)
        pal_even = expand_42(s, i, i + 1)

        answer = max([answer, pal_odd, pal_even], key = len)

    return answer

def manacher_algorithm(s: str) -> str:
    if not s:
        return ""


    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    P = [0] * n  
    C = 0  
    R = 0  

    for i in range(1, n - 1):
        mirror = 2 * C - i

        if i < R:
            P[i] = min(R - i, P[mirror])

        while t[i + (1 + P[i])] == t[i - (1 + P[i])]:
            P[i] += 1   

        if i + P[i] > R:
            C = i
            R = i + P[i]

    max_len = max(P)
    center_index = P.index(max_len)
    

    start = (center_index - max_len) // 2
    return s[start : start + max_len]



if __name__ == '__main__':
    s = "babad"
    longest_pal = manacher_algorithm(s)

    print(longest_pal)