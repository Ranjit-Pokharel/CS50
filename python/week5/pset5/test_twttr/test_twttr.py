from twttr import shorten

def test_single_word():
    assert shorten("Twitter") == "Twttr"

def test_sentence():
    assert shorten("what's your name?") == "wht's yr nm?"

def test_sentence_titled():
    assert shorten("What's Your Name?") == "Wht's Yr Nm?"

def test_capitalize():
    assert shorten("AEIOU") == ""

def test_lower():
    assert shorten("aeiou") == ""

def test_no_vowel():
    assert shorten("CS50") == "CS50"


def test_lower_case():
    assert shorten("hello, world") == "hll, wrld"

def test_with_number():
    assert shorten("12a34e5i6") == "123456"


