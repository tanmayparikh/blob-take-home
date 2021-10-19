import unittest
from find_blobs import find_blobs

class TestFindBlobs(unittest.TestCase):

    def test_points(self):
        blobs = find_blobs('assets/01_points.png')
        self.assertEquals(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 122)
        self.assertAlmostEqual(blobs[0][1], 379)
        self.assertAlmostEqual(blobs[1][0], 175)
        self.assertAlmostEqual(blobs[1][1], 125)
        self.assertAlmostEqual(blobs[2][0], 381)
        self.assertAlmostEqual(blobs[2][1], 289)

    def test_black_and_white(self):
        blobs = find_blobs('assets/02_black_and_white.png')
        self.assertEquals(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 129, delta=50)
        self.assertAlmostEqual(blobs[0][1], 123, delta=50)
        self.assertAlmostEqual(blobs[1][0], 243, delta=70)
        self.assertAlmostEqual(blobs[1][1], 370, delta=70)
        self.assertAlmostEqual(blobs[2][0], 400, delta=25)
        self.assertAlmostEqual(blobs[2][1], 245, delta=25)
        
    def test_gradient(self):
        blobs = find_blobs('assets/03_gradient.png')
        self.assertEquals(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0],  77, delta=25)
        self.assertAlmostEqual(blobs[0][1], 126, delta=25)
        self.assertAlmostEqual(blobs[1][0], 103, delta=20)
        self.assertAlmostEqual(blobs[1][1], 417, delta=20)
        self.assertAlmostEqual(blobs[2][0], 302, delta=90)
        self.assertAlmostEqual(blobs[2][1], 172, delta=90)

    def test_noisy(self):
        blobs = find_blobs('assets/04_noisy.png')
        self.assertEquals(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 148, delta=75)
        self.assertAlmostEqual(blobs[0][1], 312, delta=75)
        self.assertAlmostEqual(blobs[1][0], 236, delta=20)
        self.assertAlmostEqual(blobs[1][1], 121, delta=20)
        self.assertAlmostEqual(blobs[2][0], 325, delta=40)
        self.assertAlmostEqual(blobs[2][1], 300, delta=40)

if __name__ == "__main__":
    unittest.main()