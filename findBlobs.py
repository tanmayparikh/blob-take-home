import imageio
import scipy.signal
import sys
import os

def findBlobs(path):
    image = imageio.imread(path, as_gray=True)
    relativeMaximiums = scipy.signal.argrelmax(image)
    numberOfPeaks = len(relativeMaximiums[0])
    blobCentres = []
    for index in range(numberOfPeaks):
        blobCentres.append([relativeMaximiums[1][index], relativeMaximiums[0][index]])
    return blobCentres

if __name__ == "__main__":
    imagePath = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(__file__) + "/assets/01_points.png"
    print(findBlobs(imagePath))