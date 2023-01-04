import formatter
import unittest

class Testing1(unittest.TestCase):
  
  def tests(self):
    test_text="LETTeRKENNY"
    result1=formatter.to_upper("test_text")
    self.assertEqual(result1,"lettjerkenny")

if __name__ == "__main__":
  unittest.main()
