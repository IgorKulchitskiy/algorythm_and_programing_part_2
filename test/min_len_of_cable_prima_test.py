import unittest

from src.min_len_of_cable_prima import read_input, prim
class TestGraph(unittest.TestCase):
    def test_read_input(self):
        input_data = "K1, K2, 1500\nK1, K3, 2000\nK1, K4, 1800\nK2, K3, 2200\nK2, K4, 2500\nK3, K4, 1700\nK4, K5, 1900"
        expected_output = {
            'K1': [('K2', 1500), ('K3', 2000), ('K4', 1800)],
            'K2': [('K1', 1500), ('K3', 2200), ('K4', 2500)],
            'K3': [('K1', 2000), ('K2', 2200), ('K4', 1700)],
            'K4': [('K1', 1800), ('K2', 2500), ('K3', 1700), ('K5', 1900)],
            'K5': [('K4', 1900)]
        }
        file_path = "test_input.csv"

        with open(file_path, 'w') as file:
            file.write(input_data)

        output = read_input(file_path)

        self.assertEqual(output, expected_output)

    def test_prim(self):
        graph = {
            'K1': [('K2', 1500), ('K3', 2000), ('K4', 1800)],
            'K2': [('K1', 1500), ('K3', 2200), ('K4', 2500)],
            'K3': [('K1', 2000), ('K2', 2200), ('K4', 1700)],
            'K4': [('K1', 1800), ('K2', 2500), ('K3', 1700), ('K5', 1900)],
            'K5': [('K4', 1900)]
        }
        expected_output = 6900
        
        output = prim(graph)
        
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
