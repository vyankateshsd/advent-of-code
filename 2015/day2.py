def part1(input: str) -> int:
    input = input.splitlines()
    total_area = 0
    for line in input:
        line = line.split("x")
        l = int(line[0])
        b = int(line[1])
        h = int(line[2])
        areas = [2*l*b, 2*b*h, 2*l*h]
        areas.append(min(areas)/2)
        total_area += sum(areas)
    return int(total_area)

def part2(input: str) -> int:
    input = input.splitlines()
    total_length = 0
    for line in input:
        line = line.split("x")
        l = int(line[0])
        b = int(line[1])
        h = int(line[2])
        volume = l*b*h
        perimeters = [2*(l+b), 2*(b+h), 2*(l+h)]
        total_length += min(perimeters) + volume
    return total_length