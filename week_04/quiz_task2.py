import math

K = [27, 32, 15, 77, 6, 11, 22, 45, 99, 40]
M = 10

# Hash table open hashing with linked list at each index

# Calculate each slots number of elements

# Hash function
def hash_function(key):
    print(math.floor(key / M))
    return math.floor(key / M)

# Insert elements into hash table
def insert(hash_table, key, value):
    hash_key = hash_function(key)
    hash_table[hash_key].append(value)

# Print each hash table slot
def print_hash_table(hash_table):
    for i in range(len(hash_table)):
        print(i, end = " ")
        for j in hash_table[i]:
            print("-->", end = " ")
            print(j, end = " ")
        print()

# Create hash table
hash_table = [[] for _ in range(M)]

# Insert elements into hash table
for i in K:
    insert(hash_table, i, i)

# Print hash table
print_hash_table(hash_table)

# Calculate each slots number of elements
for i in range(len(hash_table)):
    print("Number of elements at index", i, "is", len(hash_table[i]))

# Print how many slots have 1, 2 and 3 elements
one = 0
two = 0
three = 0

for i in range(len(hash_table)):
    if len(hash_table[i]) == 1:
        one += 1
    elif len(hash_table[i]) == 2:
        two += 1
    elif len(hash_table[i]) == 3:
        three += 1

print("Number of slots with 1 element is", one)
print("Number of slots with 2 elements is", two)
print("Number of slots with 3 elements is", three)
