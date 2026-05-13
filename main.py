import importlib
from dotenv import load_dotenv

from get_input import get_input

load_dotenv()

def solve(year: int, day: int):
    module = importlib.import_module(f"{year}.day{day}")
    part1, part2 = module.part1, module.part2

    input = get_input(year, day)
    print("Part 1:", part1(input))    
    print("Part 2:", part2(input))

def main():
    year = int(input("Enter year: "))
    day = int(input("Enter day: "))

    solve(year, day)

if __name__ == "__main__":
    main()