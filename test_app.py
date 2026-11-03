import unittest
from app import hello_world


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(hello_world(), "Hello, DevOps!")
    
    def test_hello_world_returns_string(self):
        assert isinstance(hello_world(), str)


if __name__ == "__main__":
    unittest.main()