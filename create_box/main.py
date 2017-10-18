def create_box(height, width, character):
    row = character * width
    box = ""
    
    if height < 1 or width < 1:
        return "Height and width values must be greater than 1, please try again"
    else:
          box += (row + "\n") * height
    return box

"""
Bonus challenge: make it so only the outer border of the box shows and it is not filled in. Make this a separate function and add unit tests for it
"""


def create_outline(height, width, character):
    line = 1
    first_last_row = character * width
    other_rows = (character + (" " * (width-2)) + character)
    box = ""
    
    if height < 1 or width < 1:
        return "Height and width values must be greater than 1, please try again"
    else:
        if line == 1:
          box += first_last_row + "\n"
          line += 1
        while line > 1 and line < height:
          box += other_rows + "\n"
          line += 1
        if line == height:
          box += first_last_row + "\n"
    return box

# Tests:

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

first_outline_box_expected = """
xxx
x x
xxx
""".lstrip()

second_outline_box_expected = """
*****
*   *
*   *
*****
""".lstrip()


def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

def test_third_box():
    assert create_box(3, 24, 'x') == third_box_expected

def test_first_outline():
    assert create_outline(3, 3, "x") == first_outline_box_expected
    
def test_second_outline():
    assert create_outline(4, 5, "*") == second_outline_box_expected