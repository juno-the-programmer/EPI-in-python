def is_palindormic(s: str) -> bool:
    return all(s[i] == s[~i] for i in range(len(s) // 2))

print(is_palindormic('racacar'))