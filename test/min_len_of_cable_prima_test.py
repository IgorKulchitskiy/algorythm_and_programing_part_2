import unittest

from src.min_len_of_cable_prima import read_input, prim


class TestGraph(unittest.TestCase):
    def test_read_input(self):
        input_data = "K1, K2, 900\nK1, K3, 1000\nK2, K3, 1500\nK2, K4, 4000\nK3, K4, 100"
        expected_output = {
            'K1': [('K2', 900), ('K3', 1000)],
            'K2': [('K1', 900), ('K3', 1500), ('K4', 4000)],
            'K3': [('K1', 1000), ('K2', 1500), ('K4', 100)],
            'K4': [('K2', 4000), ('K3', 100)]
        }
        file_path = "test_input.csv"

        with open(file_path, 'w') as file:
            file.write(input_data)

        output = read_input(file_path)

        self.assertEqual(output, expected_output)

    def test_prim(self):
        graph = {
            'K1': [('K2', 900), ('K3', 1000)],
            'K2': [('K1', 900), ('K3', 1500), ('K4', 4000)],
            'K3': [('K1', 1000), ('K2', 1500), ('K4', 100)],
            'K4': [('K2', 4000), ('K3', 100)]
        }
        expected_output = 6500

        output = prim(graph)

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
