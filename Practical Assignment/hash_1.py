# class for hashtable nodes
class Node:
    def __init__ (self, key, value, next = None):
        self.key = key # hashkey of the node
        self.value = value # value of the node
        self.next = next # pointer to next node if there is there is multiple nodes with the same key

# class for hashtable 
class HashTable:
    def __init__ (self, size):
        self.size = size
        self.table = [None] * self.size
    
    # hash function using string folding with two letters at a time
    def hash(self, key):
        givenKey = str(key) # convert key to string regardless of the given type
        sum = 0
        multiplier = 1

        # go through the key and calculate the multiplier
        for char in range(0, len(givenKey)):
            multiplier = 1 if (char % 2 == 0) else multiplier * 256
            sum += multiplier * ord(givenKey[char])

        # return the calculated hashvalue
        return sum % self.size
    
    # insert function
    def insert(self, value):
        hashID = self.hash(value) # get the hashvalue of the key
        pos = self.table[hashID] # position in the table

        # if the slot with hashID is empty, create a new node 
        if pos is None:
            self.table[hashID] = Node(hashID, value) 
            return None

        # collision
        current = head = pos # pointers 
        # go to end of linked lsit at calculatd hash index
        while current is not None:
            if current.key == value:
                return None
            current = current.next

        # add new value to end of list
        self.table[hashID] = Node(hashID, value, head)

    # search function
    def search(self, value):
        hashID = self.hash(value) # get hashvalue of key
        pos = self.table[hashID] # position of calculated hash value in the table
        nodeCounter = 1 # number nodes at index position

        # if slot is empty, cannot find searched value
        if pos is None:
            print("Value " + str(value) + " not found in hash table")
            return None
        
        # iterate through the nodes at calculated index
        while pos is not None:
            # find the exact node
            if pos.value == value:
                print("Value " + str(pos.value) + " found at index " + str(pos.key) + " in node " + str(nodeCounter))
                return
            # next position
            pos = pos.next
            nodeCounter += 1

        # no value found
        print("Value " + str(value) + " not found in hash table")
        return None

 
    # delete function
    def delete(self, value):
        hashID = self.hash(value) # calculated hash
        current = self.table[hashID] # current position
        previous = None # initialize value for previous position

        # if the current position's value is the one we like to delete, do that
        if current.value == value:
            self.table[hashID] = current.next
            return

        # iterate through the nodes at calculated index
        while current is not None and current.value != value:
            previous = current
            current = current.next

        # node is not found, cannot delete
        if current is None:
            return None
        else:
            # delete the node
            if previous is None:
                current = None
            else:
                previous.next = previous.next.next
                