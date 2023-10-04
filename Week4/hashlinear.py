class HashLinear:
    def __init__(self, size):
        self.X = size
        self.table = [None] * size

    def hash(self, data: str):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        #print(sum," --> ", sum % self.X, end= " \n")
        return sum % self.X
    
    def insert(self, data: str):
        hash_key = self.hash(data)
        #print("hash_key = ", data)
        if self.table[hash_key] is None:
            #print("1")
            self.table[hash_key] = data
        else:
            orig_hash_key = hash_key
            while self.table[hash_key] is not None:
                hash_key = (hash_key + 1) % self.X
                if self.table[hash_key] == data:
                    return
                elif orig_hash_key == hash_key:
                    # avoid infinite loop
                    return
            self.table[hash_key] = data

        #print("Done")

    def delete(self, data: str):
        hash_key = self.hash(data)

        if self.table[hash_key] == data:
            #print("1")
            self.table[hash_key] = None
        else:
            orig_hash_key = hash_key
            while self.table[hash_key] != data:
                hash_key = (hash_key + 1) % self.X
                if self.table[hash_key] == data:
                    self.table[hash_key] = None
                elif orig_hash_key == hash_key:
                    # avoid infinite loop
                    return

        #print("Done")

    def print(self):
        for i in range(self.X):
            if self.table[i] is not None:
                print(self.table[i], end=" ")
        print()


if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1
