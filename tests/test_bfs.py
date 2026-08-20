import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'algorithms', 'breath_first_search'))

from count_islands import count_islands


class TestCountIslands:
    def test_basic(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        assert count_islands(grid) == 3

    def test_single_island(self):
        grid = [
            [1, 1, 1],
            [0, 0, 0],
            [1, 1, 1]
        ]
        assert count_islands(grid) == 2

    def test_no_islands(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        assert count_islands(grid) == 0

    def test_all_land(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1]
        ]
        assert count_islands(grid) == 1

    def test_single_cell(self):
        grid = [[1]]
        assert count_islands(grid) == 1

    def test_diagonal_not_connected(self):
        grid = [
            [1, 0],
            [0, 1]
        ]
        assert count_islands(grid) == 2
