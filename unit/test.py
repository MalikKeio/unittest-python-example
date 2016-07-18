import unittest
import mymodule

class TestMymodule(unittest.TestCase):

    def test_empty_input(self):
        inputString = ""
        self.assertEqual(mymodule.myfunction(inputString), "")

    def test_stupid_test_that_will_fail(self):
        inputString = ["Arrayを入力して意味あんの？", 3]
        self.assertEqual(mymodule.myfunction(inputString), "")
    def test_stupid_test_error(self):
        """あるはテストする価値のある不可欠な機能ですか？"""
        inputString = ["Arrayを入力して意味あんの？", 3]
        self.assertRaises(AttributeError, mymodule.myfunction, inputString)
