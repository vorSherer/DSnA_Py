import pytest

from dsna_py.challenges.cc_31_repeated_word import repeated_word


def test_make_word_list_exists():
    assert repeated_word.make_word_list


def test_detect_first_repeated_word_exists():
    assert repeated_word.detect_first_repeated_word

# [ - - - - - - TEST SAMPLE 1 - - - - - - ]
@pytest.fixture
def sample_str_1():
    return "Once upon a time, there was a brave princess who..."


def test_make_word_list_for_sample_1(sample_str_1):
    expected = ['once', 'upon', 'a', 'time', 'there', 'was', 'a', 'brave', 'princess', 'who']
    actual = repeated_word.make_word_list(sample_str_1)
    assert actual == expected


def test_text_sample_1_return_pass(sample_str_1):
    expected = "a"
    actual = repeated_word.detect_first_repeated_word(sample_str_1)
    assert actual == expected


def test_text_sample_1_return_cap_fail(sample_str_1):
    expected = "A"
    actual = repeated_word.detect_first_repeated_word(sample_str_1)
    assert actual != expected


def test_text_sample_1_return_wrong_word_fail(sample_str_1):
    expected = "dragon"
    actual = repeated_word.detect_first_repeated_word(sample_str_1)
    assert actual != expected


# [ - - - - - - TEST SAMPLE 2 - - - - - - ]
@pytest.fixture
def sample_str_2():
    return "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    

def test_make_word_list_for_sample_2(sample_str_2):
    expected = ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness', 'it', 'was', 'the', 'epoch', 'of', 'belief', 'it', 'was', 'the', 'epoch', 'of', 'incredulity', 'it', 'was', 'the', 'season', 'of', 'light', 'it', 'was', 'the', 'season', 'of', 'darkness', 'it', 'was', 'the', 'spring', 'of', 'hope', 'it', 'was', 'the', 'winter', 'of', 'despair', 'we', 'had', 'everything', 'before', 'us', 'we', 'had', 'nothing', 'before', 'us', 'we', 'were', 'all', 'going', 'direct', 'to', 'heaven', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 'way', '–', 'in', 'short', 'the', 'period', 'was', 'so', 'far', 'like', 'the', 'present', 'period', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 'insisted', 'on', 'its', 'being', 'received', 'for', 'good', 'or', 'for', 'evil', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only']
    actual = repeated_word.make_word_list(sample_str_2)
    assert actual == expected


def test_text_sample_2_return_pass(sample_str_2):
    expected = "it"
    actual = repeated_word.detect_first_repeated_word(sample_str_2)
    assert actual == expected


def test_text_sample_2_return_cap_fail(sample_str_2):
    expected = "It"
    actual = repeated_word.detect_first_repeated_word(sample_str_2)
    assert actual != expected


def test_text_sample_2_return_wrong_word_fail(sample_str_2):
    expected = "was"
    actual = repeated_word.detect_first_repeated_word(sample_str_2)
    assert actual != expected


# [ - - - - - - TEST SAMPLE 3 - - - - - - ]
@pytest.fixture
def sample_str_3():
    return "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."


def test_make_word_list_for_sample_3(sample_str_3):
    expected = ['it', 'was', 'a', 'queer', 'sultry', 'summer', 'the', 'summer', 'they', 'electrocuted', 'the', 'rosenbergs', 'and', 'i', 'didn’t', 'know', 'what', 'i', 'was', 'doing', 'in', 'new', 'york']
    actual = repeated_word.make_word_list(sample_str_3)
    assert actual == expected


def test_text_sample_3_return_pass(sample_str_3):
    expected = "summer"
    actual = repeated_word.detect_first_repeated_word(sample_str_3)
    assert actual == expected


def test_text_sample_3_return_comma_fail(sample_str_3):
    expected = "summer,"
    actual = repeated_word.detect_first_repeated_word(sample_str_3)
    assert actual != expected


def test_text_sample_3_return_wrong_word_fail(sample_str_3):
    expected = "was"
    actual = repeated_word.detect_first_repeated_word(sample_str_3)
    assert actual != expected

