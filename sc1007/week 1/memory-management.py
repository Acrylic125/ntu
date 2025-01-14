# Import required modules
from typing import List, Any
import sys # For checking reference counts
import gc

a = "abc"
b = "abc"
c = "abc_"

print(f"{id(a)}: {a}")
print(f"{id(b)}: {b}")
print(f"{id(c)}: {c}")
print("-----")

x = 69
print(f"{id(x)}: {x}")
y = x
print(f"{id(y)}: {y}")
y = y + 1
print(f"{id(y)}: {y}")
z = 69
print(f"{id(z)}: {z}")

print("-----")
x = [1, 2, 3]
print(f"{id(x)}: {x} refcount = {sys.getrefcount(x) - 1}")
y = x
print(f"{id(y)}: {y} refcount = {sys.getrefcount(y) - 1}")
y.append(4)
print("after mutation")
print(f"{id(x)}: {x} refcount = {sys.getrefcount(x) - 1}")
print(f"{id(y)}: {y} refcount = {sys.getrefcount(y) - 1}")

del y
print("after deleting y")
print(f"{id(x)}: {x} refcount = {sys.getrefcount(x) - 1}")

print("-----")
x: List[Any] = [1, 2, 3]
y: List[Any]  = [3, 4, 5]
x.append(y)
y.append(x)
print(f"{id(x)}: {x} refcount = {sys.getrefcount(x) - 1}")
print("after delete y")
del y
print(f"{id(x)}: {x} refcount = {sys.getrefcount(x) - 1}")
del x

# When GC runs, the references get wiped.
gc.collect()
gc_count = gc.get_count()
print(f"before alloc {gc_count}")
list1 = []
list2 = []
gc_count = gc.get_count()
print(f"after alloc {gc_count}")
list1.append(list2)
list2.append(list1)
# After appending, it increases the reference count for both lists.
gc_count = gc.get_count()
print(f"after append alloc {gc_count}")
del list1 
del list2
# Does not deref since theres a cyclical reference.
gc_count = gc.get_count()
print(f"after deletion alloc {gc_count}")

# When GC runs, the references get wiped.
gc.collect()
gc_count = gc.get_count()
print(f"after gc collect {gc_count}")

