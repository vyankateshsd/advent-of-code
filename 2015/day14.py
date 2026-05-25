LIMIT = 2503

def part1(input: str) -> int:
    distances = list()
    for line in input.splitlines():
        line = line.split(" ")
        speed = int(line[3])
        time = int(line[6])
        period = time + int(line[-2])
        
        dist = (LIMIT // period) * speed * time
        if LIMIT % period > time: dist += speed * time
        distances.append(dist)
    return max(distances)

def part2(input: str) -> int:
    deers = dict()
    points = dict()
    lb = dict()
    for line in input.splitlines():
        line = line.split(" ")
        deer = {
            'name': line[0],
            'speed': int(line[3]),
            'stamina': int(line[6]),
            'rest': int(line[-2]),
            'state': ["flying", 0]
        }
        deers[line[0]] = deer
        points[line[0]] = 0
        lb[line[0]] = 0
    for timestamp in range(LIMIT):
        for deer in deers.values():
            if deer['state'][0] == 'flying':
                lb[deer['name']] += deer['speed']
                deer['state'][1] += 1
                if deer['state'][1] >= deer['stamina']:
                    deer['state'] = ["resting", 0]
            elif deer['state'][0] == 'resting':
                deer['state'][1] += 1
                if deer['state'][1] >= deer['rest']:
                    deer['state'] = ["flying", 0]
        items = list(lb.items())
        items.sort(key=lambda item: item[1], reverse= True)
        highest = items[0][1]
        for item in items:
            if item[1] != highest: break
            points[item[0]] += 1
    return max(points.values())