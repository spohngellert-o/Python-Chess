import unittest
from Python_Chess import *
'''

---------------------------------------------------------
---------------------------------------------------------
----------------------- TESTS ---------------------------
---------------------------------------------------------
---------------------------------------------------------

'''
class TestPawnMethods(unittest.TestCase):

    def test_pawn_get_possible_moves_white_no_left(self):
    	pawn = Pawn()
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(0, 1))
    	expected_moves.append(Position(1, 1))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_white_no_right(self):
    	pawn = Pawn(Position(7, 2))
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(6, 3))
    	expected_moves.append(Position(7, 3))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_white_no_double(self):
    	pawn = Pawn(Position(5, 4))
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(4, 5))
    	expected_moves.append(Position(5, 5))
    	expected_moves.append(Position(6, 5))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_white_double(self):
    	pawn = Pawn(Position(3, 1))
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(2, 2))
    	expected_moves.append(Position(3, 2))
    	expected_moves.append(Position(3, 3))
    	expected_moves.append(Position(4, 2))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_black_double(self):
    	pawn = Pawn(Position(6, 6), False)
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(5, 5))
    	expected_moves.append(Position(6, 5))
    	expected_moves.append(Position(6, 4))
    	expected_moves.append(Position(7, 5))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_black_no_double(self):
    	pawn = Pawn(Position(6, 5), False)
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(5, 4))
    	expected_moves.append(Position(6, 4))
    	expected_moves.append(Position(7, 4))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_black_double_no_left(self):
    	pawn = Pawn(Position(0, 6), False)
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(0, 5))
    	expected_moves.append(Position(0, 4))
    	expected_moves.append(Position(1, 5))
    	self.assertListEqual(moves, expected_moves)

class TestIsPositionInBounds(unittest.TestCase):

    def test_is_origin_in_bounds(self):
        posOrigin = Position(0, 0)
        self.assertTrue(isPositionInBounds(posOrigin))

    def test_is_top_right_in_bounds(self):
        pos = Position(7, 7)
        self.assertTrue(isPositionInBounds(pos))

    def test_is_top_left_in_bounds(self):
        pos = Position(0, 7)
        self.assertTrue(isPositionInBounds(pos))

    def test_is_x_8_out_bounds(self):
        pos = Position(8, 4)
        self.assertFalse(isPositionInBounds(pos))

    def test_is_x_negative_out_bounds(self):
        pos = Position(-1, 4)
        self.assertFalse(isPositionInBounds(pos))

    def test_is_y_negative_out_bounds(self):
        pos = Position(1, -4)
        self.assertFalse(isPositionInBounds(pos))

    def test_is_both_negative_out_bounds(self):
        pos = Position(-1, -4)
        self.assertFalse(isPositionInBounds(pos))

    def test_is_y_8_out_bounds(self):
        pos = Position(2, 8)
        self.assertFalse(isPositionInBounds(pos))

class TestKnightGetAllMoves(unittest.TestCase):

    def test_knight_get_all_moves_from_middle(self):
        knight = Knight(Position(4, 4))
        expected_moves = knight.getAllMoves()
        moves = []
        moves.append(Position(3, 6))
        moves.append(Position(3, 2))
        moves.append(Position(5, 6))
        moves.append(Position(5, 2))
        moves.append(Position(2, 5))
        moves.append(Position(2, 3))
        moves.append(Position(6, 5))
        moves.append(Position(6, 3))
        for move in moves:
            self.assertTrue(move in expected_moves)

    def test_knight_get_all_moves_from_right(self):
        knight = Knight(Position(6, 4))
        expected_moves = knight.getAllMoves()
        moves = []
        moves.append(Position(7, 2))
        moves.append(Position(5, 2))
        moves.append(Position(7, 6))
        moves.append(Position(5, 6))
        moves.append(Position(4, 3))
        moves.append(Position(4, 5))
        for move in moves:
            self.assertTrue(move in expected_moves)

    def test_knight_get_all_moves_from_top_right(self):
        knight = Knight(Position(6, 6))
        expected_moves = knight.getAllMoves()
        moves = []
        moves.append(Position(4, 5))
        moves.append(Position(4, 7))
        moves.append(Position(5, 4))
        moves.append(Position(7, 4))
        for move in moves:
            self.assertTrue(move in expected_moves)

    def test_knight_get_all_moves_from_top_right_corner(self):
        knight = Knight(Position(7, 7))
        expected_moves = knight.getAllMoves()
        moves = []
        moves.append(Position(6, 5))
        moves.append(Position(5, 6))
        for move in moves:
            self.assertTrue(move in expected_moves)

    def test_knight_get_all_moves_from_left_side(self):
        knight = Knight(Position(0, 3))
        expected_moves = knight.getAllMoves()
        moves = []
        moves.append(Position(1, 5))
        moves.append(Position(1, 1))
        moves.append(Position(2, 4))
        moves.append(Position(2, 2))
        for move in moves:
            self.assertTrue(move in expected_moves)


    def test_knight_get_all_moves_from_bottom_side_left(self):
        knight = Knight(Position(1, 0))
        expected_moves = knight.getAllMoves()
        moves = []
        moves.append(Position(3, 1))
        moves.append(Position(0, 2))
        moves.append(Position(2, 2))
        for move in moves:
            self.assertTrue(move in expected_moves)

    def test_knight_get_all_moves_from_bottom_side_left_2(self):
        knight = Knight(Position(2, 0))
        expected_moves = knight.getAllMoves()
        moves = []
        moves.append(Position(4, 1))
        moves.append(Position(1, 2))
        moves.append(Position(3, 2))
        moves.append(Position(0, 1))
        for move in moves:
            self.assertTrue(move in expected_moves)

        

if __name__ == '__main__':
    unittest.main()