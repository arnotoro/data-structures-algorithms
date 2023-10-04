class HashBucket:
    def __init__(self, size, num_buckets):
        self.M = size
        self.B = num_buckets
        self.bucket_size = size // num_buckets
        self.table = [[None, None]] * size
        self.overflow = [None] * size

    def hash(self, data: str):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.B
    
    def insert(self, data: str):
        hash_key = self.hash(data)
        bucket = self.table[hash_key]
        print("hash_key = ", hash_key, "bucket = ", bucket)
        
        for i in range(self.bucket_size):
            if self.table[hash_key + i] == data:
                return
        else:
            # find the first empty slot in the bucket
            for i in range(self.bucket_size):
                if self.table[hash_key + i] is None:
                    self.table[hash_key + i] = data
                    return
            # if no empty slot in the bucket, insert to overflow
            for i in range(self.bucket_size):
                if self.overflow[hash_key + i] is None:
                    self.overflow[hash_key + i] = data
                    return
                
    def delete(self, data: str):
        hash_key = self.hash(data)

        if self.table[hash_key] == data:
            self.table[hash_key] = None
        else:
            # find the data in the bucket
            for i in range(self.bucket_size):
                if self.table[hash_key + i] == data:
                    self.table[hash_key + i] = None
                    return
            # if not found, find in overflow
            for i in range(self.bucket_size):
                if self.overflow[hash_key + i] == data:
                    self.overflow[hash_key + i] = None
                    return
                
    def print(self):
        for i in range(self.M):
            print(self.table[i], end=" ..")
        for i in range(self.M):
            print(self.overflow[i], end=" ....")
        print()
        



if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # BM40A1500 Bar1 10aaaa1