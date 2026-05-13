def part1(input: str) -> int:
    x = 0
    y = 0
    visited = set()
    for char in input:
        visited.add((x, y))
        if char == ">": x += 1
        if char == "<": x -= 1
        if char == "^": y += 1
        if char == "v": y -= 1
    return len(visited)

def part2(input: str) -> int:
    visited = set()
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    turn = 0
    for char in input:
        visited.add((x1, y1))
        visited.add((x2, y2))
        turn = not turn
        if turn:
            if char == ">": x1 += 1
            if char == "<": x1 -= 1
            if char == "^": y1 += 1
            if char == "v": y1 -= 1
        else:
            if char == ">": x2 += 1
            if char == "<": x2 -= 1
            if char == "^": y2 += 1
            if char == "v": y2 -= 1
    return len(visited)