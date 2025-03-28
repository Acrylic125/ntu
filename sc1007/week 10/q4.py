from typing import List

maps: List[List[List[int]]] = []

with open("q4_input.txt", "r") as f:
    lines = f.readlines()
    should_create_entry = True
    for line in lines:
        if line == "\n":
            should_create_entry = True
            continue
        if should_create_entry:
            should_create_entry = False
            maps.append([])
            continue
        row = map(int, line.split(" "))
        maps[-1].append(list(row))

def dfs_paths(n = 0, 
                 cur_loc = 0,
                 explored_mask = 0):
    explored_mask = explored_mask | (1 << cur_loc)
    res = []
    for i in range(n):
        i_mask = 1 << i
        if (explored_mask & i_mask) != 0:
            continue
        sub_paths = dfs_paths(n, i, explored_mask)
        for sp in sub_paths:
            res.append(sp)
    if len(res) <= 0:
        return [[cur_loc]]
    return [[cur_loc, *path] for path in res]

for m in maps:
    size = len(m)
    if (size <= 0):
        print("Skipping map, no map.")
    paths = dfs_paths(size)

    lowest_path = None
    lowest_d = 0
    for path in paths:
        d = 0
        cur_i = 0
        for goto_i in path:
            d = d + m[cur_i][goto_i]
            cur_i = goto_i
        # Go back
        d = d + m[path[len(path) - 1]][0]
        
        if lowest_path == None or d < lowest_d:
            lowest_path = path 
            lowest_d = d

    print(f"{lowest_path} with d = {lowest_d}")

    # for row in m:
    #     print(row)
    # print()
    # print()
