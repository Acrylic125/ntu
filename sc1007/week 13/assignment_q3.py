TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1
DELETED = 2

class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY

def hash1(key):
    return key % TABLESIZE

def hash2(key):
    return (key % PRIME) + 1

def hash_insert(key, hash_table):
    available_slot = None 

    key_comparisons = 0
    for i in range(TABLESIZE):
        index = (hash1(key) + i * hash2(key)) % TABLESIZE
        value = hash_table[index]
        if value.indicator == USED:
            key_comparisons = key_comparisons + 1
            if value.key == key:
                return -1
        if value.indicator == DELETED:
            if available_slot == None:
                available_slot = value 
        if value.indicator == EMPTY:
            if available_slot != None:
                available_slot.key = key
                available_slot.indicator = USED
                return key_comparisons
            value.key = key
            value.indicator = USED
            return key_comparisons
    if available_slot != None:
        available_slot.key = key
        available_slot.indicator = USED
        return key_comparisons
    return TABLESIZE

def hash_delete(key, hash_table):
    key_comparisons = 0
    for i in range(TABLESIZE):
        index = (hash1(key) + i * hash2(key)) % TABLESIZE
        value = hash_table[index]
        if value.indicator == EMPTY:
            return -1 
        if value.indicator == USED:
            key_comparisons = key_comparisons + 1
            if value.key == key:
                value.indicator = DELETED
                return key_comparisons
    return -1
def print_menu():
    print("============= Hash Table ============")
    print("|1. Insert a key to the hash table  |")
    print("|2. Delete a key from the hash table|")
    print("|3. Print the hash table            |")
    print("|4. Quit                            |")
    print("=====================================")
    print("Enter selection: ", end="")
    
def main():
    # import sys
    # input = sys.stdin.read
    st = "2 3 3"
    # st = "1 5 1 42 2 5 1 5 1 42 3"
    # st = "1 5 1 41 1 42 3 1 9 1 72 1 73 1 42 1 79 2 42 3 2 42 1 43 1 37 1 36 1 27 1 22 1 15 1 77 1 66 1 22 1 45 1 79 1 23 1 5 1 38 1 39 1 40 1 443 1 468 1 98 2 45 2 79 3 1 99 1 605 1 74 1 28 1 91 1 92 1 27 1 28 1 29 1 30 1 31 1 32 1 33 1 35 1 27 1 26 1 55 2 55 1 56 1 57 3 1 32 2 57 1 57 1 26 1 45 2 56 3 4 "
    # st = "1 5 1 10 1 7 1 9 1 11 2 7 1 69 3"
    data = list(map(int, st.split()))
    
    print("Done")

    hash_table = [HashSlot() for _ in range(TABLESIZE)]
    i = 0
    print_menu()
    while i < len(data):
        opt = data[i]
        i += 1

        if opt == 1:
            print("Enter a key to be inserted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            comparison = hash_insert(key, hash_table)
            if comparison < 0:
                print("Duplicate key")
            elif comparison < TABLESIZE:
                print(f"Insert: {key} Key Comparisons: {comparison}")
            else:
                print(f"Key Comparisons: {comparison}. Table is full.")
            print("Enter selection: ", end="")
        elif opt == 2:
            print("Enter a key to be deleted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            comparison = hash_delete(key, hash_table)
            if comparison < 0:
                print(f"{key} does not exist.")
            elif comparison <= TABLESIZE:
                print(f"Delete: {key} Key Comparisons: {comparison}")
            else:
                print("Error")
            print("Enter selection: ", end="")
        elif opt == 3:
            for j in range(TABLESIZE):
                marker = '*' if hash_table[j].indicator == DELETED else ' '
                print(f"{j}: {hash_table[j].key} {marker}")
            print("Enter selection: ", end="")
        elif opt == 4:
            break
        else:
            continue

if __name__ == "__main__":
    main()
