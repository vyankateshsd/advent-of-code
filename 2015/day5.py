def part1(input: str) -> int:
    valid_count = 0

    for string in input.splitlines():
        vowel_count = 0
        double_count = 0
        fails = False

        last_char: str = None
        for char in string:
            if char in ("a", "e", "i", "o", "u"): vowel_count += 1
            if last_char == None: 
                last_char = char
                continue
            if (last_char + char) in ("ab", "cd", "pq", "xy"): fails = True

            if fails: break
            if last_char == char: double_count += 1
            last_char = char
        if vowel_count > 2 and double_count >0 and fails == 0:
            valid_count += 1
    return valid_count
    

def part2(input: str) -> int:
    valid_count = 0
    for string in input.splitlines():
        cd1 = False
        cd2 = False
        pairs = list()

        for index, char in enumerate(string):
            if index > len(string) - 2: continue
            c_pair = char  + string[index+1]
            pairs.append((c_pair, index))
            matching_pairs = [pair for pair in pairs if pair[0] == c_pair and index - pair[1] >= 2]
            if len(matching_pairs) != 0: 
                cd1 = True

            if (cd1 and cd2):
                valid_count += 1
                break
            if index > len(string) - 3: continue
            if char == string[index+2]: cd2 = True
    return valid_count

