# test_metaloom.py
"""
Tests for MetaLoom module.
"""

import unittest
from metaloom import MetaLoom

class TestMetaLoom(unittest.TestCase):
    """Test cases for MetaLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaLoom()
        self.assertIsInstance(instance, MetaLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
