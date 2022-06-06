import pytest


from hypothesis import given, assume, settings
from hypothesis.strategies import integers, lists, text

from app.calc.common import addition, subtraction, multiplication, division, sum


@given(x=integers(), y=integers())
@settings(max_examples=1000)
def test_addition(x, y):
    assert addition(x, y) == x + y


@given(x=integers(), y=integers())
def test_subtraction(x, y):
    assert subtraction(x, y) == x - y


@given(x=integers(), y=integers())
def test_multiplication(x, y):
    assert multiplication(x, y) == x * y


@given(x=integers(), y=integers())
def test_division(x, y):
    assume(y != 0)
    assert division(x, y) == x / y


@given(li=lists(integers()))
def test_sum(li):
    result = 0
    for i in li:
        result += i
    assert sum(li) == result
