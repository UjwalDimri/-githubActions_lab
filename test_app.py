import unittest
from app import hello_world
from app import welcome_message


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(hello_world(), "Hello, DevOps!")
    
    def test_hello_world_returns_string(self):
        assert isinstance(hello_world(), str)
    def test_welcome_message(self):
        self.assertEqual(welcome_message("Ujwal"),"Welcome to DevOps, Ujwal!")
    def test_welcome_message_hanu(self):
        self.assertEqual(welcome_message("Hanu"),"Welcome to DevOps, Hanu!")
            

if __name__ == "__main__":
    unittest.main()