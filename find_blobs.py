import imageio
import scipy.signal

def find_blobs(path):
    image = imageio.imread(path, as_gray=True)
    relative_maximiums = scipy.signal.argrelmax(image)
    blob_centres = []
    for index in range(len(relative_maximiums[0])):
        blob_centres.append([relative_maximiums[0][index], relative_maximiums[1][index]])
    return blob_centres



# ==================================================================================================================>8==
# the following code is for the unit tests
# you should not need to modify this code (unless you want to add more test cases)

import unittest
import os

class TestFindBlobs(unittest.TestCase):

    def test_points(self):
        blobs = find_blobs(self._asset_path('01_points.png'))
        self.assertEqual(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 122)
        self.assertAlmostEqual(blobs[0][1], 379)
        self.assertAlmostEqual(blobs[1][0], 175)
        self.assertAlmostEqual(blobs[1][1], 125)
        self.assertAlmostEqual(blobs[2][0], 381)
        self.assertAlmostEqual(blobs[2][1], 289)

    def test_black_and_white(self):
        blobs = find_blobs(self._asset_path('02_black_and_white.png'))
        self.assertEqual(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 129, delta=50)
        self.assertAlmostEqual(blobs[0][1], 123, delta=50)
        self.assertAlmostEqual(blobs[1][0], 243, delta=70)
        self.assertAlmostEqual(blobs[1][1], 370, delta=70)
        self.assertAlmostEqual(blobs[2][0], 400, delta=25)
        self.assertAlmostEqual(blobs[2][1], 245, delta=25)
        
    def test_gradient(self):
        blobs = find_blobs(self._asset_path('03_gradient.png'))
        self.assertEqual(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0],  77, delta=25)
        self.assertAlmostEqual(blobs[0][1], 126, delta=25)
        self.assertAlmostEqual(blobs[1][0], 103, delta=20)
        self.assertAlmostEqual(blobs[1][1], 417, delta=20)
        self.assertAlmostEqual(blobs[2][0], 302, delta=90)
        self.assertAlmostEqual(blobs[2][1], 172, delta=90)

    def test_noisy(self):
        blobs = find_blobs(self._asset_path('04_noisy.png'))
        self.assertEqual(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 148, delta=75)
        self.assertAlmostEqual(blobs[0][1], 312, delta=75)
        self.assertAlmostEqual(blobs[1][0], 236, delta=20)
        self.assertAlmostEqual(blobs[1][1], 121, delta=20)
        self.assertAlmostEqual(blobs[2][0], 325, delta=40)
        self.assertAlmostEqual(blobs[2][1], 300, delta=40)
    
    def bonus_perlin_noise(self):
        blobs = find_blobs(self._asset_path('05_bonus_perlin_noise.png'))
        self.assertEqual(len(blobs), 3)
        self.assertAlmostEqual(blobs[0][0], 139, delta=50)
        self.assertAlmostEqual(blobs[0][1], 92, delta=25)
        self.assertAlmostEqual(blobs[1][0], 177, delta=25)
        self.assertAlmostEqual(blobs[1][1], 414, delta=25)
        self.assertAlmostEqual(blobs[2][0], 345, delta=50)
        self.assertAlmostEqual(blobs[2][1], 385, delta=40)

    def _asset_path(self, file_name):
        return os.path.dirname(__file__) + '/assets/' + file_name

if __name__ == "__main__":
    import unittest
    unittest.main()