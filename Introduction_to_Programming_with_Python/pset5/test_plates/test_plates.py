from plates import is_valid

def test_atlist_2_letter():
    assert is_valid("CS50") == True

def test_char_btn_2_6():
    assert is_valid("P") == False
    assert is_valid("PI3145678") == False
    assert is_valid("PI3145") == True

def test_not_number_inbtn():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

def test_start_nom_not_zero():
    assert is_valid("AAA022") == False

def test_other_not_alpanumeric():
    assert is_valid("AAA22.2") == False
    assert is_valid("AAA2!") == False

def test_onlynum():
    assert is_valid("11111") == False