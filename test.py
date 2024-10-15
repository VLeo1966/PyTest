import pytest
from main import check
from main import isPalindrome
from main import sort_list
from main import init_db, add_user, get_user

def test_check():
    assert check(6) == True


def test_check2():
   assert check(3) == False


@pytest.mark.parametrize("number, expected", [
   (2, True),
   (5, False),
   (0, True),
   (56, True),
   (-3, False)
])
def test_check_with_param(number, expected):
   assert check(number) == expected


def test_isPalindrome1():
    assert isPalindrome('madam') == True
    assert isPalindrome('hello') == False


@pytest.mark.parametrize("test_input,expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])
def test_is_Palindrome(test_input, expected):
    assert isPalindrome(test_input) == expected


def test_sort1():
    assert sort_list([5, 6, 3, 1, 2]) == [1, 2, 3, 5, 6]
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()


def test_add_or_get_user(db_conn):
    add_user(db_conn, "Sasha", 30)
    user = get_user(db_conn, "Sasha")
    assert user == (1, "Sasha", 30)

if __name__ == "__main__":
    pytest.main()