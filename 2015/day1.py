def part1(input: str) -> int:
    result = 0
    count = 0
    for char in input:
        count += 1
        if char == "(": result += 1
        elif char == ")": result -= 1
    return result

def part2(input: str) -> int:
    result = 0
    count = 0
    for char in input:
        count += 1
        if char == "(": result += 1
        elif char == ")": result -= 1

        if result == -1:
            return count
