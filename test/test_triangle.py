import unittest
from src.triangle import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_area_positive_values(self):
        """Test positive values"""
        self.assertAlmostEqual(triangle_area(10, 5), 25.0)
        self.assertAlmostEqual(triangle_area(8, 2), 8.0)

    def test_area_zero_values(self):
        """Test zero values"""
        self.assertAlmostEqual(triangle_area(0, 5), 0.0)
        self.assertAlmostEqual(triangle_area(10, 0), 0.0)
        self.assertAlmostEqual(triangle_area(0, 0), 0.0)

    def test_area_negative_values(self):
        """Test negative values"""
        with self.assertRaises(ValueError):
            triangle_area(-10, 5)
        with self.assertRaises(ValueError):
            triangle_area(10, -5)
        with self.assertRaises(ValueError):
            triangle_area(-10, -5)

if __name__ == "__main__":
    unittest.main()
