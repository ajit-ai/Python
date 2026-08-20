from algorithms.matrix.rotate_image import rotate
from algorithms.matrix.spiral_traversal import spiral_traversal


class TestRotateImage:
    def test_basic(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]
        assert rotate(matrix) == expected

    def test_single(self):
        assert rotate([[1]]) == [[1]]

    def test_2x2(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[3, 1], [4, 2]]
        assert rotate(matrix) == expected

    def test_empty(self):
        assert rotate([]) == []


class TestSpiralTraversal:
    def test_basic(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        assert spiral_traversal(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_single_row(self):
        matrix = [[1, 2, 3]]
        assert spiral_traversal(matrix) == [1, 2, 3]

    def test_single_col(self):
        matrix = [[1], [2], [3]]
        assert spiral_traversal(matrix) == [1, 2, 3]

    def test_empty(self):
        assert spiral_traversal([]) == []

    def test_2x2(self):
        matrix = [[1, 2], [3, 4]]
        assert spiral_traversal(matrix) == [1, 2, 4, 3]
