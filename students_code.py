class HashTable:
    def __init__(self, size=1000):
        self.size = size  # Number of buckets
        self.table = [[] for _ in range(size)]  # List of lists for storage
        self.collisions = 0  # Keep track of collisions

    def _hash(self, word):
        return hash(word) % self.size  # Just using mod for now

    def insert(self, word):
        index = self._hash(word)
        bucket = self.table[index]
        
        # Check if word is already in there
        for i in range(len(bucket)):
            if bucket[i][0] == word:
                bucket[i] = (word, bucket[i][1] + 1)  # Update count
                return
        
        # Collision happens if bucket isn't empty
        if bucket:
            self.collisions += 1
        
        bucket.append((word, 1))  # Add new word

    def lookup(self, word):
        index = self._hash(word)
        bucket = self.table[index]
        lookups = 0

        for w, count in bucket:
            lookups += 1
            if w == word:
                return count, lookups  # Found it
        
        return 0, lookups  # Not in table

    def get_stats(self):
        used_buckets = sum(1 for bucket in self.table if bucket)  # Count non-empty buckets
        return used_buckets, self.collisions


def words_in(word_list):
    global hash_table
    hash_table = HashTable()
    for word in word_list:
        hash_table.insert(word)
    return hash_table.get_stats()


def lookup_word_count(word):
    return hash_table.lookup(word)
