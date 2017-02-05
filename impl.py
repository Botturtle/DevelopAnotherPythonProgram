""" Class: CIS 640 ZA
    Assignment: Develop Another Python Program
    Author: Zachary Cleary """


def tic_tac_toe_check(board):
    """Returns the winner of the board if one exists, else returns None"""
    test_board_is_not_none(board)
    test_board_is_a_list(board)
    test_board_contains_nine_strings(board)
    test_board_contains_valid_chars(board)
    test_board_strings_is_none_or_one(board)
    test_board_contains_no_more_than_one_winner(board)
    return get_winner(board)


def test_board_is_not_none(board):
    """asserts that TypeError is raised if the board is None"""
    try:
        assert board is not None
    except:
        raise TypeError


def test_board_is_a_list(board):
    """asserts that ValueError is raised if the board is not a list"""
    try:
        assert isinstance(board, list)
    except:
        raise ValueError


def test_board_contains_nine_strings(board):
    """asserts that ValueError is raised if the board does not contain exactly nine strings"""
    try:
        assert len(board) == 9
        for s in board:
            assert isinstance(s, str)
    except:
        raise ValueError


def test_board_contains_valid_chars(board):
    """asserts that ValueError is raised if the board contains any character other than 'x', 'o', or ''"""
    try:
        validChars = ['x', 'o', '']
        for s in board:
            assert s in validChars
    except:
        raise ValueError


def test_board_strings_is_none_or_one(board):
    """asserts that ValueError is raised if the board contains any non-empty strings more than one char in length"""
    try:
        for s in board:
            if s != '':
                assert len(s) == 1
    except:
        raise ValueError


def test_board_contains_no_more_than_one_winner(board):
    """asserts that ValueError is raised if the board has more than one winner"""
    try:
        number_of_winners = get_number_of_horizontal_winners(board)
        number_of_winners += get_number_of_vertical_winners(board)
        number_of_winners += get_number_of_diagonal_winners(board)
        assert number_of_winners <= 1
    except:
        raise ValueError


# helper functions:

def get_number_of_vertical_winners(board):
    """returns the number of winners in vertical columns of the board"""
    v0 = set(board[0:9:3])
    v1 = set(board[1:9:3])
    v2 = set(board[2:9:3])
    x = set('x')
    o = set('o')
    count = 0
    count = count + 1 if v0 == x or v0 == o else count
    count = count + 1 if v1 == x or v1 == o else count
    count = count + 1 if v2 == x or v2 == o else count
    return count


def get_number_of_horizontal_winners(board):
    """returns the number of winners in horizontal columns of the board"""
    h0 = set(board[0:3])
    h1 = set(board[3:6])
    h2 = set(board[6:9])
    x = set('x')
    o = set('o')
    count = 0
    count = count + 1 if h0 == x or h0 == o else count
    count = count + 1 if h1 == x or h1 == o else count
    count = count + 1 if h2 == x or h2 == o else count
    return count


def get_number_of_diagonal_winners(board):
    """returns the number of winners in diagonal rows of the board"""
    d0 = set(board[0:9:4])
    d1 = set(board[2:7:2])
    x = set('x')
    o = set('o')
    count = 0
    count = count + 1 if d0 == x or d0 == o else count
    count = count + 1 if d1 == x or d1 == o else count
    return count


def get_winner(board):
    """returns the winner of the board if exists, else returns None"""
    v0 = set(board[0:9:3])
    v1 = set(board[1:9:3])
    v2 = set(board[2:9:3])
    h0 = set(board[0:3])
    h1 = set(board[3:6])
    h2 = set(board[6:9])
    d0 = set(board[0:9:4])
    d1 = set(board[2:7:2])
    possible_winners = [v0, v1, v2, h0, h1, h2, d0, d1]
    for index, row in enumerate(possible_winners):
        if row == set('x'):
            return 'x'
        elif row == set('o'):
            return 'o'
    return None
        board = ['x','x','o','','','','','','1']