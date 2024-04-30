from bank import value

def test_with_h():
    assert value("hi") == 20
    assert value("h") == 20

def test_with_hello():
    assert value("hello") == 0

def test_upper():
    assert value("HI") == 20
    assert value("HELLO") == 0

def test_tittled():
    assert value("Hi") == 20
    assert value("Hello") == 0

def test_not_h():
    assert value("what's up!") == 100

def test_sentence():
    assert value("hi, how are you?") == 20
    assert value("hello, what can i do?") == 0
    assert value("what can i do for you?") == 100