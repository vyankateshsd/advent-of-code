import re

def part1(input: str) -> int:
    diff = 2*len(input.splitlines())
    diff += len(re.findall("(\\\\\")|(\\\\\\\\)", input))
    diff += 3*len(re.findall("(\\\\x[\\da-f]{2})", input))
    return diff
        

def part2(input: str) -> int:
    diff = 2*len(input.splitlines())
    diff += len(re.findall("(\\\\)|(\")", input))
    return diff