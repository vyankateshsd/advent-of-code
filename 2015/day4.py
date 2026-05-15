from hashlib import md5

def part1(input: str) -> int:
    input = input.strip()
    ans = 0
    while True:
        key = input + str(ans)
        hex_hash = md5(key.encode()).hexdigest()
        if hex_hash.startswith("00000"): break
        else: ans += 1
    return ans

def part2(input: str) -> int:
    input = input.strip()
    ans = 0
    while True:
        key = input + str(ans)
        hex_hash = md5(key.encode()).hexdigest()
        if hex_hash.startswith("000000"): break
        else: ans += 1
    return ans