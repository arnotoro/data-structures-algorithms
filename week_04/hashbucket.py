class HashBucket:
    def __init__(self, size, num_buckets):
        self.M = size
        self.B = num_buckets
        self.bucket_size = size // num_buckets
        self.table = [[] for _ in range(self.M)]
        self.overflow = [] * self.M


    def hash(self, data: str):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.B
    
    def insert(self, data: str):
        hash_key = self.hash(data)
        #print(hash_key, len(self.table[hash_key]), self.bucket_size)

        if len(self.table[hash_key]) < self.bucket_size:
            if data in self.table[hash_key]:
                #print("duplicate", data, "in table", hash_key)
                return
            self.table[hash_key].append(data)
            #print("inserted", data, "in table", hash_key)
        else:
            if data in self.table[hash_key]:
                #print("duplicate", data, "in table", hash_key)
                return
            self.overflow.append(data)
            #print("inserted", data, "in overflow", hash_key)



                
    def delete(self, data: str):
        hash_key = self.hash(data)
        #print(hash_key, len(self.table[hash_key]))

        if data in self.table[hash_key]:
            self.table[hash_key].remove(data)
            #print("deleted", data, "from table", hash_key)
        elif data in self.overflow:
            self.overflow.remove(data)
            #print("deleted", data, "from overflow", hash_key)

                
    def print(self):
        for table_index in range(self.M):
            if len(self.table[table_index]) > 0:
                for bucket_index in range(len(self.table[table_index])):
                    print(self.table[table_index][bucket_index], end=" ")

        for overflow_index in range(len(self.overflow)):
            if self.overflow[overflow_index] is not None:
                print(self.overflow[overflow_index], end=" ")
        print()



if __name__ == "__main__":
    # table = HashBucket(8, 4)
    # table.insert("BM40A1500")
    # table.insert("fOo")
    # table.insert("123")
    # table.insert("Bar1")
    # table.insert("10aaaa1")
    # table.insert("BM40A1500")
    # table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    # table.delete("fOo")
    # table.delete("Some arbitary string which is not in the table")
    # table.delete("123")
    # table.print()   # BM40A1500 Bar1 10aaaa1


    table = HashBucket(10, 5)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    table.print()
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    table.print()