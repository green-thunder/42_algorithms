def is_valid(s: str) -> bool:
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    return not stack


def is_valid_42(s: str) -> bool:
    balance = 0

    for bracket in s:
        if bracket == "(":
            balance += 1
        elif bracket == ")":
            if not balance:
                return False
            balance -= 1

    return balance == 0

if __name__ == "__main__":
    s = "()()"

    result = is_valid(s)

    print(result)
