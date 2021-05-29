import unittest
from calculator import add, subtract

class calculator_test (unittest.TestCase):
    def test1(self):
        self.assertEqual(add(3,5), 8)

    def test2(self):
        self.assertEqual(subtract(8,7),1)

if __name__ == "__main__":
    #0: nothing
    #1: default setting, shows .F
    #2: Shows details - which cases are okay and which cases are failed
    unittest.main(verbosity=2)