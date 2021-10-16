import unittest
from findBlobs import findBlobs

class TestFindBlobs(unittest.TestCase):

    def test_points(self):
        blobs = findBlobs('assets/01_points.png')
        self.assertEquals(blobs, [[379,122], [125,175], [289,381]])

    def test_black_and_white(self):
        blobs = findBlobs('assets/02_black_and_white.png')
        self.assertEquals(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 123, delta=50)
        self.assertAlmostEqual(blobs[0][1], 129, delta=50)
        self.assertAlmostEqual(blobs[1][0], 370, delta=70)
        self.assertAlmostEqual(blobs[1][1], 243, delta=70)
        self.assertAlmostEqual(blobs[2][0], 245, delta=25)
        self.assertAlmostEqual(blobs[2][1], 400, delta=25)
        
    def test_gradient(self):
        blobs = findBlobs('assets/03_gradient.png')
        self.assertEquals(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 126, delta=25)
        self.assertAlmostEqual(blobs[0][1],  77, delta=25)
        self.assertAlmostEqual(blobs[1][0], 417, delta=20)
        self.assertAlmostEqual(blobs[1][1], 103, delta=20)
        self.assertAlmostEqual(blobs[2][0], 172, delta=90)
        self.assertAlmostEqual(blobs[2][1], 302, delta=90)

    def test_noisy(self):
        blobs = findBlobs('assets/04_noisy.png')
        self.assertEquals(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 312, delta=75)
        self.assertAlmostEqual(blobs[0][1], 148, delta=75)
        self.assertAlmostEqual(blobs[1][0], 121, delta=20)
        self.assertAlmostEqual(blobs[1][1], 236, delta=20)
        self.assertAlmostEqual(blobs[2][0], 300, delta=40)
        self.assertAlmostEqual(blobs[2][1], 325, delta=40)

if __name__ == "__main__":
    unittest.main()