import imageio
import scipy.signal
import sys
import os

def find_blobs(path):
    image = imageio.imread(path, as_gray=True)
    relative_maximiums = scipy.signal.argrelmax(image)
    blob_centres = []
    for index in range(len(relative_maximiums[0])):
        blob_centres.append([relative_maximiums[0][index], relative_maximiums[1][index]])
    return blob_centres

if __name__ == "__main__":
    imagePath = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(__file__) + "/assets/01_points.png"
    print(find_blobs(imagePath))