import unittest
import calculator_program
class TestCalculator(unittest.TestCase):
    def test_calculate(self):
        # 测试加法运算
        calculator_program.entry.get = lambda: "3 + 4"
        calculator_program.calculate()
        self.assertEqual(calculator_program.history.get('1.0', 'end'), "3 + 4 = 7\n")
        self.assertEqual(calculator_program.history.get_file(), "3 + 4 = 7\n")
        # 测试减法运算
        calculator_program.entry.get = lambda: "10 - 6"
        calculator_program.calculate()
        self.assertEqual(calculator_program.history.get('1.0', 'end'), "10 - 6 = 4\n")
        self.assertEqual(calculator_program.history.get_file(), "3 + 4 = 7\n10 - 6 = 4\n")
        # 测试乘法运算
        calculator_program.entry.get = lambda: "5 * 2"
        calculator_program.calculate()
        self.assertEqual(calculator_program.history.get('1.0', 'end'), "5 * 2 = 10\n")
        self.assertEqual(calculator_program.history.get_file(), "3 + 4 = 7\n10 - 6 = 4\n5 * 2 = 10\n")
        # 测试除法运算
        calculator_program.entry.get = lambda: "8 / 2"
        calculator_program.calculate()
        self.assertEqual(calculator_program.history.get('1.0', 'end'), "8 / 2 = 4\n")
        self.assertEqual(calculator_program.history.get_file(), "3 + 4 = 7\n10 - 6 = 4\n5 * 2 = 10\n8 / 2 = 4\n")
        # 测试错误提示
        calculator_program.entry.get = lambda: "3 / 0"
        calculator_program.calculate()
        self.assertEqual(calculator_program.history.get('1.0', 'end'), "Error: Zero division error\n")
        self.assertEqual(calculator_program.history.get_file(), "3 + 4 = 7\n10 - 6 = 4\n5 * 2 = 10\n8 / 2 = 4\nError: Zero division error\n")
if __name__ == '__main__':
    unittest.main()