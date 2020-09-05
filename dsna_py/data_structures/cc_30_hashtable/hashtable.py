from dsna_py.data_structures.cc_05_linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        resulting_hash = 0

        for ch in key:
            spike = ord(ch)
            resulting_hash += ord(ch)

        return ((resulting_hash * spike) * 151) % self.size

    def add(self, key, value):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].append([key, value])

    def get(self, key):
        hashed_key = self._hash(key)

        bucket_list = self._buckets[hashed_key]

        current = bucket_list.head

        while current:
            if current.value[0] == key:
                return current.value[1]

    def contains(self, key):
        pass





if __name__ == "__main__":
    hasher = Hashtable()
    print("Bob= ", hasher._hash("Bob"))
    print("Dan= ", hasher._hash("Dan"))
    print("Ted= ", hasher._hash("Ted"))
    print("Ralph= ", hasher._hash("Ralph"))
    print("Dennis= ", hasher._hash("Dennis"))
    print("George= ", hasher._hash("George"))
    hasher.add("Bob", 5551212)
    hasher.add("Ralph", 5553333)
    hasher.add("Dennis", 5556789)
    sample = hasher.get("Bob")
    print(sample)
   
