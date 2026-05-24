def part1(input: str) -> int:
    input = eval(input)
    while True:
        result = []
        if type(input) == dict:
            result = list(input.values())
        elif type(input) == list:
            for val in input:
                if type(val) == int:
                    result.append(val)
                elif type(val) == dict:
                    result.extend(val.values())
                elif type(val) == list:
                    result.extend(val)
        if input == result:
            break
        input = result
    return sum(input)

def part2(input: str) -> int:
    input = eval(input)
    while True:
        result = []
        if type(input) == dict:
            result.extend(input.values())
        elif type(input) == list:
            for val in input:
                if type(val) == int:
                    result.append(val)
                elif (
                    type(val) == dict and 
                    "red" not in val.values()
                ): 
                    result.extend(val.values())
                elif type(val) == list:
                    result.extend(val)
        if input == result:
            break
        input = result
    return sum(input)