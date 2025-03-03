class HashTable:
    def __init__(self, size=100):  # Initialize hash table with a fixed size
        self.size = size
        self.table = [None] * size  # Create empty slots
        self.collisions = 0  # Track collisions

    def _hash1(self, word):
        return sum(ord(c) for c in word) % self.size  # Basic hash function
    def _hash2(self, word):
        return (sum(ord(c) for c in word) % (self.size-1))+1  # Basic hash function

    def insert(self, word):
        index = self._hash1(word)
        step_size = self._hash2(word)
        original_index=index
        while self.table[index]is not None:
            if self.table[index][0]==word:
                self.table[index][1]+=1
                return
            self.collisions +=1
            index = (index + step_size) % self.size
            if index==original index:
                return
        self.table[index] = [word,1]
        
    def lookup(self, word):
        index = self._hash1(word)
        step_size = self._hash2(word)
        lookups=0

        while self.table[index] is not None:
            lookups +=1
            if self.table[index][0]==word:
                return self.table[index][1],lookups
                index = (index + step_size) % self_size
            return 0, lookups

    def get_stats(self):
        used_buckets = sum(1 for bucket in self.table if bucket)  # Count used slots
        return used_buckets, self.collisions  # Return stats


def words_in(word_list):
    global hash_table
    hash_table = HashTable()
    for word in word_list:
        hash_table.insert(word)  # Insert words
    return hash_table.get_stats()


def lookup_word_count(word):
    return hash_table.lookup(word)  # Lookup word count

