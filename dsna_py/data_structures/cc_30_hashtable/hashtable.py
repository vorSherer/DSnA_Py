from dsna_py.data_structures.cc_05_linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def hash(self, key):
        resulting_hash = 0

        for ch in key:
            spike = ord(ch)
            resulting_hash += ord(ch)

        return ((resulting_hash * spike) * 151) % self.size

    def add(self, key, value):
        pass

    def get(self, key):
        pass

    def contains(self, key):
        pass





if __name__ == "__main__":
    hasher = Hashtable()
    print("Bob= ", hasher.hash("Bob"))
    print("Dan= ", hasher.hash("Dan"))
    print("Ted= ", hasher.hash("Ted"))
    print("Ralph= ", hasher.hash("Ralph"))
    print("Dennis= ", hasher.hash("Dennis"))
    print("George= ", hasher.hash("George"))
