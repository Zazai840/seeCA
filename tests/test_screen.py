import unittest
import numpy as np
from screen import Screen

class TestScreen(unittest.TestCase):
    def test_render(self):
        array = np.array([[0, 0, 0, 1, 0, 0, 0],
                         [0, 0, 1, 1, 1, 0, 0]])

        screen = Screen(array)
        rendered_screen = screen.render()
        self.assertEqual(rendered_screen, [[" ", " ", " ", "#", " ", " ", " "],
                                            [" ", " ", "#", "#", "#", " ", " "]])
