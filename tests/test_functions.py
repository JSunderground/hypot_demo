from hypot.functions import addition, squared, sqroot, hypot
import pytest

# test addition
## 4+7=11
def test_addition_int():
    assert addition(4,7) == 7
## 2.3 + 7.92 = 10.22 ## POSSIBLE ERROR
def  test_adittion_float():
    assert addition(2.3, 7.92) == pytest.approx(10.22, 0.01)
## "A" + "B" = "PLEASE USE INTEGERS OR FLOATS"
def test_addition_str():
    assert addition("A","B") == "PLEASE USE INTEGERS OR FLOATS"


# test squared

## 3^2 = 9 ## ODD NUMBERS
def test_squared_odd():
    assert squared(3) == 9
## (-2)^2 > 0 ## TEST FOR NEGATIVES
def test_squared_neg():
    assert squared(-2) == 4
# test squared root

## sqroot(9) = 3 ##
def test_sqroot_pos():
    assert sqroot(16) == 4


#test hypot

## 3,4 == 5
def test_hypot():
    assert hypot(3,4) == 5