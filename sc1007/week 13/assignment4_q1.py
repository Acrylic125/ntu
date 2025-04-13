TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1

class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY
        self.next = -1

def hash_func(key):
    return key % TABLESIZE

def hash_insert(key, hash_table):
    original_index = hash_func(key)
    value = hash_table[original_index]
    prev_index = -1
    for i in range(TABLESIZE):
        index = original_index + i # hash_func(key) + i 
        index = hash_func(index)
        probed_value = hash_table[index]
        if probed_value.indicator == EMPTY:
            if prev_index != -1:
                value.next = index
            probed_value.key = key 
            probed_value.indicator = USED 
            return index
        if probed_value.indicator == USED and probed_value.key == key:
            return -1
        prev_index = index
    return len(hash_table) + 1

def hash_find(key, hash_table):
    index = hash_func(key)
    cur = hash_table[index]
    while True:
        if cur.indicator == EMPTY:
            return -1
        if key == cur.key:
            return index 
        if cur.next == -1:
            return -1
        index = cur.next
        cur = hash_table[index]

def print_menu():
    print("============= Hash Table ============")
    print("|1. Insert a key to the hash table  |")
    print("|2. Search a key in the hash table  |")
    print("|3. Print the hash table            |")
    print("|4. Quit                            |")
    print("=====================================")
    print("Enter selection: ", end="")


def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    hash_table = [HashSlot() for _ in range(TABLESIZE)]
    for slot in hash_table:
        slot.key = 0
        slot.indicator = EMPTY
        slot.next = -1

    i = 0
    print_menu()
    while i < len(data):

        opt = data[i]
        i += 1

        if opt == 1:  # Insert
            print("Enter a key to be inserted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_insert(key, hash_table)
            if index < 0:
                print("Duplicate key")
            elif index < TABLESIZE:
                print(f"Insert {key} at index {index}")
            else:
                print("Table is full.")
            print("Enter selection: ", end="")
        elif opt == 2:  # Search
            print("Enter a key for searching in the HashTable:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_find(key, hash_table)
            if index != -1:
                print(f"{key} is found at index {index}.")
            else:
                print(f"{key} is not found.")
            print("Enter selection: ", end="")
        elif opt == 3:  # Print table
            print("index:\t key \t next")
            for j in range(TABLESIZE):
                print(f"{j}\t{hash_table[j].key}\t{hash_table[j].next}")
            print("Enter selection: ", end="")
        elif opt == 4:
            break
        else:
            print("Enter selection: ", end="")
            continue


if __name__ == "__main__":
    main()
