# test_volumejolt.py
"""
Tests for VolumeJolt module.
"""

import unittest
from volumejolt import VolumeJolt

class TestVolumeJolt(unittest.TestCase):
    """Test cases for VolumeJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VolumeJolt()
        self.assertIsInstance(instance, VolumeJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VolumeJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
