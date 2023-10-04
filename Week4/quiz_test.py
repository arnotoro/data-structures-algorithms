# Hash table size and number of buckets
M = 10
B = 5

# Keys
K = [91, 103, 79, 247, 9]

# Hash function with string keys
def hash_function(key):
    print(key % 10)

# Print result of hash function
for i in K:
    hash_function(i)



