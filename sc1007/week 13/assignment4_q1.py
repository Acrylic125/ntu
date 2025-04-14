# TABLESIZE = 37
# PRIME = 13
TABLESIZE = 7
PRIME = 13
# TABLESIZE = 37
# PRIME = 13
EMPTY = 0
USED = 1

class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY
        self.next = -1

def hash_func(key):
    return key % TABLESIZE
#
# def hash_insert(key, hash_table):
#     prev_used = None
#     for i in range(TABLESIZE):
#         index = hash_func(hash_func(key) + i)
#         value = hash_table[index]
#         if value.indicator == USED: 
#             if value.key == key:
#                 return -1
#             prev_used = value 
#             continue 
#         if value.indicator == EMPTY: 
#             if prev_used != None:
#                 prev_used.next = index
#             value.key = key 
#             value.indicator = USED 
#             return index 
#     return TABLESIZE + 69
#

def hash_insert(key, hash_table):
    prev_index = None
    for i in range(TABLESIZE):
        index = hash_func(hash_func(key) + i)
        value = hash_table[index]
        if value.indicator == USED:
            if value.key == key:
                return -1  
            if prev_index == None:
                prev_index = index
            continue
        if value.indicator == EMPTY:
            value.key = key
            value.indicator = USED
            if prev_index is not None:
                while True:
                    prev_value = hash_table[prev_index]
                    if prev_value.next == -1:
                        prev_value.next = index
                        break
                    prev_index = prev_value.next
            return index
    return TABLESIZE + 69 

def hash_find(key, hash_table):
    for i in range(TABLESIZE):
        index = hash_func(hash_func(key) + i)
        value = hash_table[index] 
        if value.indicator == EMPTY:
            return -1 
        if value.indicator == USED and value.key == key:
            return index
    return -1

def print_menu():
    print("============= Hash Table ============")
    print("|1. Insert a key to the hash table  |")
    print("|2. Search a key in the hash table  |")
    print("|3. Print the hash table            |")
    print("|4. Quit                            |")
    print("=====================================")
    print("Enter selection: ", end="")


def main():
    # import sys
    # input = sys.stdin.read


    st = "1 14 1 7 1 5 1 15 1 13 1 19 3"
    # data = []
    # with open("./assignment_q1_input.txt", "r") as f:
    #     data = f.readlines()
    # st = "1 1 1 2 1 5 1 41 1 42 3"
    # st = "1 1 1 2 1 5 1 41 1 42 3 1 4 2 4 2 10 1 10 3 1 11 1 37 1 30 1 45 1 17 1 9 1 13 2 14 2 13 1 38 1 39 1 40 1 77 1 79 1 56 1 58 2 59 2 5 3 4"
    # st = "1 1 1 2 1 5 1 41 1 42 3 1 4 1 4 1 10 1 10 3 1 11 1 37 1 30 1 45 1 17 1 9 1 13 1 14 1 13 1 38 1 39 1 40 1 77 1 79 1 56 1 58 1 59 1 5 3 1 17 1 53 1 52 1 51 1 50 1 49 4"
    data = list(map(int, st.split(' ')))

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
