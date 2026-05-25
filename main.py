import sys
import importlib
from dotenv import load_dotenv
from datetime import datetime

from get_input import get_input

load_dotenv()

def main():
    if len(sys.argv) < 3:
        raise Exception("Provide year and day")

    year = int(sys.argv[1])
    if year < 2015 or year > datetime.now().year:
        raise Exception("Invalid year")
    
    day = int(sys.argv[2])
    if day < 1 or day > 25:
        raise Exception("Invalid date")

    module = importlib.import_module(f"{year}.day{day}")
    part1, part2 = module.part1, module.part2

    input = get_input(year, day)
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

if __name__ == "__main__":
    main()