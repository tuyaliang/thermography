import unittest

import numpy as np

from thermography.utils import ID


class TestIDUtils(unittest.TestCase):
    def test_ID_generator(self):
        """Tests the values of the IDs generated by :func:`~thermography.utils.ID.next_id` and :func:`~thermography.utils.ID.reset_id`."""
        self.assertEqual(ID.next_id(), 0)

        num_tests = 10
        for i in range(num_tests):
            initial_id = np.random.randint(-100, 100)
            ID.reset_id(initial_id)
            num_steps = 100
            for step in range(num_steps):
                self.assertEqual(ID.next_id(), initial_id + step)


if __name__ == '__main__':
    unittest.main()
