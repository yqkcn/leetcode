def isHappy(n: int) -> bool:
    if n == 1:
        return True
    processed = set()
    while True:
        if n in processed:
            break
        processed.add(n)
        n = sum(int(_) * int(_) for _ in str(n))
        if n == 1:
            return True
    return False


if __name__ == '__main__':
    print(isHappy(19))
