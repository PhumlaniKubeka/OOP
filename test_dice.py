from Dice import Die
import pytest

def test_roll():
    rand_instance = Die(6)
    assert rand_instance.value == True

def test_negative():
    with pytest.raises(Exception):
        error = Exception('negative probabilities not allowed')
        rand_instance = Die(6,[1,-1,1,1,1,1])
        assert rand_instance.value == error

def test_greater_than():
    with pytest.raises(Exception):
        error = Exception("probability sum must be greater than 0")
        rand_instance = Die(6,[0,0,0,0,0,0])
        assert rand_instance.value == error

def test_no_values():
    with pytest.raises(Exception):
        error = Exception("only integer values allowed")
        rand_instance = Die(7,[0,2,3.2,5,0.6,5])
        assert rand_instance.value == error


       