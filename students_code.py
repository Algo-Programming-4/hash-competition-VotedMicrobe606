class HashTable:
    def __init__(self, size=100):  # Initialize hash table with a fixed size
        self.size = size
        self.table = [None] * size  # Create empty slots
        self.collisions = 0  # Track collisions

    def _hash(self, word):
        return sum(ord(c) for c in word) % self.size  # Basic hash function

    def insert(self, word):
        index = self._hash(word)
        
        if self.table[index] is None:
            self.table[index] = [word, 1]  # Store new word
        else:
            if self.table[index][0] == word:
                self.table[index][1] += 1  # Increase count if word exists
            else:
                self.collisions += 1  # Count collision
                self.table[index] = [word, 1]  # Overwrite existing entry

    def lookup(self, word):
        index = self._hash(word)
        if self.table[index] is None:
            return 0, 1  # Word not found
        return (self.table[index][1], 1) if self.table[index][0] == word else (0, 1)  # Return count and lookup steps

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

