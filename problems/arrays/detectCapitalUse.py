def detectCapitalUse(word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()


def inbeetween(word, start, end):
    start, end = ord(start), ord(end)
    for s in word:
        s_ascii = ord(s)
        if not (s_ascii >= start and s_ascii <= end):
            return False
        
    return True

def isupper(word):
    return inbeetween(word, "A", "Z")

def islower(word):
    return inbeetween(word, 'a', 'z')


def detectCapitalUse42(word: str) -> bool:
    if isupper(word) or islower(word):
        return True
    
    return isupper(word[:1]) and islower(word[1:])

if __name__ == '__main__':
    word = "NODIR"

    result = detectCapitalUse42(word)
    print(result)