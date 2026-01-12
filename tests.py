import unittest
from unittest.mock import patch, Mock
import unittest.mock
from main import (
    greet_person,
    is_cold_f,
    THRESHOLD_TEMP_F
)


class TestMainApp(unittest.TestCase):
    """
    Class for testing my code from main.py
    """
    @patch('builtins.input', side_effect = ['alice'])
    @patch('builtins.print')
    def test_greetperson(self, mock_print: Mock, _:Mock) -> None:
        """"
        Test to test greet_person function 
        from main.py
        """
        greet_person()
        except_calls = [
            unittest.mock.call("How you doing alice?")
        ]
        mock_print.assert_has_calls(except_calls)
    def test_is_cold_belowthresh(self) -> None:
        "test is for is_cold_f for below Threshold "
        self.assertTrue(is_cold_f(THRESHOLD_TEMP_F-10))
        
    def test_is_cold_thresh(self) -> None:
        "test is for is_cold_f for Threshold"
        self.assertFalse(is_cold_f(THRESHOLD_TEMP_F))
        
    def test_is_cold_overthresh(self) -> None:
        "test is for is_cold_f for above Threshold "
        self.assertFalse(is_cold_f(THRESHOLD_TEMP_F+10))

if __name__ == "__main__":
    unittest.main()
