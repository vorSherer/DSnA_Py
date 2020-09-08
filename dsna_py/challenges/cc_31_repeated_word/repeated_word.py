import string

from dsna_py.data_structures.cc_30_hashtable.hashtable import Hashtable


def make_word_list(_str):
    word_list = _str.lower().translate(str.maketrans('', '', string.punctuation)).split(' ')
    return word_list


def detect_first_repeated_word(input):
    source_list = make_word_list(input)
    dupe_list = Hashtable()
    
    for key in source_list:
        if not dupe_list.contains(key):
            value = 1
            dupe_list.add(key, value)
        else:
            return key




if __name__ == "__main__":
    str_in_1 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    # print(make_word_list(str_in_1))
    print(detect_first_repeated_word(str_in_1))
    str_in_2 = "Once upon a time, there was a brave princess who..."
    # print(make_word_list(str_in_2))
    print(detect_first_repeated_word(str_in_2))
    str_in_3 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    # print(make_word_list(str_in_3))
    print(detect_first_repeated_word(str_in_3))
