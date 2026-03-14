def lengthOfLongestSubstring(s: str) -> int:
  last_seen = [-1] * 26

  max_len = 0
  left = 0 

  for right in range(len(s)):
    char_idx = ord(s[right]) - ord('a')
    if last_seen[char_idx] >= left:
      left = last_seen[char_idx] + 1
    
    last_seen[char_idx] = right

    current_len = right - left + 1
    if current_len > max_len:
      max_len = current_len
  
  return max_len


s = "abcbcade"

result = lengthOfLongestSubstring(s)
print(result)