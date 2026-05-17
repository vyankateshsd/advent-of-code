def part1(input: str) -> int:
    on_lights = set()
    for instruction in input.splitlines():
        if (instruction == ""): continue
        
        instruction = instruction.split(" ")
        
        x2, y2 = instruction.pop().split(",")
        x2 = int(x2)
        y2 = int(y2)

        instruction.pop()
        
        x1, y1 = instruction.pop().split(",")
        x1 = int(x1)
        y1 = int(y1)
        
        command = instruction.pop()

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                match (command):
                    case "on":
                        on_lights.add((x, y))
                    case "off":
                        if (x, y) in on_lights: on_lights.remove((x, y))
                    case "toggle":
                        if (x, y) in on_lights: on_lights.remove((x, y))
                        else: on_lights.add((x,y))

    return len(on_lights)

def part2(input: str) -> int:
    brightness_store = dict()
    total_brightness = 0
    for instruction in input.splitlines():
        if (instruction == ""): continue
        
        instruction = instruction.split(" ")
        
        x2, y2 = instruction.pop().split(",")
        x2 = int(x2)
        y2 = int(y2)

        instruction.pop()
        
        x1, y1 = instruction.pop().split(",")
        x1 = int(x1)
        y1 = int(y1)
        
        command = instruction.pop()

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                light_coords = f"{x},{y}"
                match (command):
                    case "on":
                        brightness_store[light_coords] = brightness_store.get(light_coords, 0) + 1
                        total_brightness += 1
                    case "off":
                        curr_val = brightness_store.get(light_coords, 0)
                        if curr_val <= 0: continue
                        brightness_store[light_coords] = curr_val - 1
                        total_brightness -= 1
                    case "toggle":
                        brightness_store[light_coords] = brightness_store.get(light_coords, 0) + 2
                        total_brightness += 2
    return total_brightness