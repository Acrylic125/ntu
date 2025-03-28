from typing import List, Tuple

class Entry:
    def __init__(self):
        self.weight = 0
        self.artifacts = []

entries: List[Entry] = []
with open("q3_input.txt", "r") as f:
    lines = f.readlines()
    should_create_entry = True
    for line in lines:
        if line == "\n":
            print("Test")
            should_create_entry = True
            continue
        if should_create_entry:
            should_create_entry = False
            entry = Entry()
            entry.weight = int(line)
            entries.append(entry)
            continue
        weight, value = map(int, line.split(" "))
        entries[-1].artifacts.append((weight, value))

def findMostValue(weight_capacity: int, artifacts: List[Tuple[int, int]]):
    valid_subsets: List[List[Tuple[int, int]]] = [[]]
    for artifact in artifacts:
        temp = []
        for subset in valid_subsets:
            temp.append([*subset, artifact])
        for t in temp:
            valid_subsets.append(t)

    highest_index = -1;
    highest_value = 0;
    for si in range(len(valid_subsets)):
        total_weight = sum(map(lambda entry: entry[0], valid_subsets[si]))
        total_value = sum(map(lambda entry: entry[1], valid_subsets[si]))
        if total_value > highest_value and total_weight <= weight_capacity:
            highest_index = si
            highest_value = total_value

    print(valid_subsets[highest_index])

for entry in entries:
    # print(len(entry.artifacts))
    findMostValue(entry.weight, entry.artifacts)

