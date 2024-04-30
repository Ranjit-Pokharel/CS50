from numb3rs import validate

def test_true_ip():
    valid_ip = ["127.0.0.1", "255.255.255.255"]
    for ip in valid_ip:
        assert validate(ip) == True

def test_false_ip():
    invalid_ip = ["127.259.0.1", "512.512.512.512", "1.2.3.1000", "cat"]
    for ip in invalid_ip:
        assert validate(ip) == False