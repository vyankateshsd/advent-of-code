def look_and_say(num: str) -> str:
    ans = ""
    cr_digit = None
    cd_count = 0
    for digit in num:
        if cr_digit == None: cr_digit = digit
        if cr_digit == digit: cd_count += 1
        else:
            ans += str(cd_count) + str(cr_digit)
            cr_digit = digit
            cd_count = 1
    ans += str(cd_count) + str(cr_digit)
    return ans

def part1(input: str) -> int:
    for i in range(40): 
        input = look_and_say(input)
    return len(input)

def part2(input: str) -> int:
    for i in range(50): 
        input = look_and_say(input)
    return len(input)
    pass