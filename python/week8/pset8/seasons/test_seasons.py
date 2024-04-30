from seasons import validate, to_minutes
import pytest

def test_validate():
    with pytest.raises(SystemExit):
        validate("29-1-2983")
def test_seasons():
    assert to_minutes(2003, 5, 17) == "Ten million, six hundred sixty-seven thousand, five hundred twenty minutes"
    assert to_minutes(2000, 2, 1) == "Twelve million, three hundred ninety-six thousand, nine hundred sixty minutes"