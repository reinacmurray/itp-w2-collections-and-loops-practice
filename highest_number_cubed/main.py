def highest_number_cubed(limit):
    number = 0
    
    while True:
        number += 1
        if number ** 3 > limit:
            return number - 1


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
