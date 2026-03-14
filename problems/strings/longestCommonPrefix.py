def longestCommonPrefixmy1(words: list) -> str:
    if not words:
        return ""

    first_word = words[0]

    for i in range(len(first_word)):
        char = first_word[i]

        for word in words[1:]:
            if i == len(word) or word[i] != char:
                return first_word[:i]

    return first_word


def longestCommonPrefixmy2(words: list) -> str:
    if not words: return ""

    words.sort()
    first = words[0]
    last = words[-1]

    i = 0 
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

if __name__ == "__main__":

    words = ['flower', 'flow', 'flight']

    longest_common_prefix = longestCommonPrefixmy2(words)

    print(longest_common_prefix)