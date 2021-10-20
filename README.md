# Finding the blobs

## Significance of "Blobs" in NDE

Non-destructive examination could be oversimplified as using an insturment
(e.g. ultasonic transmitor or x-ray radiographer) to "look into" an object
without taking it apart and looking for "blobs" (i.e. signal) where you expect
there to be holes, seams, rivets, etc. You also might look for there to be no
blobs where the object should be solid. Seeing a blob here could be an
indication of a crack, unexpected hole, poor welding seam, etc. Of course,
before you can classify if a blob is expected or indicates a defect, you have
to pick them out of a potentially noisy image.
## Prompt

In this task, we are only concerned about identifying the blobs, not
classifying them as expected or defects. Your task is to make a function that
can identify white blobs on a black background. Each image will have exactly
three blobs. The function must return an array of (x,y) pairs where each pair
represent a point inside the blob (ideally roughly in the centre of the blob).
For example, given an image that looks like:

```
+---+---+---+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
+---+---+---+---+---+---+---+---+---+---+
| 1 |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
| 2 |   |▓▓▓▓▓▓▓|   |   |   |   |   |   |
+---+---|▓▓▓+---+---+---+---+---+---+---+
| 3 |   |▓▓▓|   |   |   |   |▓▓▓▓▓▓▓|   |
+---+---+---+---+---+---+---+---+---+---+
| 4 |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
| 5 |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
| 6 |   |   |   |   |   |▓▓▓|   |   |   |
+---+---+---+---+---+---+▓▓▓+---+---+---+
| 7 |   |   |   |   |   |▓▓▓|   |   |   |
+---+---+---+---+---+---+▓▓▓+---+---+---+
| 8 |   |   |   |   |   |▓▓▓|   |   |   |
+---+---+---+---+---+---+---+---+---+---+
| 9 |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
```

A valid result for the function would be:
```
[
  [2,2],
  [3,7],
  [7,7]
]
```

You are provided with the a python project specifything a function
`find_blobs(image_path)` that can open an image and identify trivially simple
blobs (i.e. blobs that are only a single pixel). You are also provided with a
(failing) test suite specifying more complex images. Your goal is to improve
`find_blobs` so that it passes as many of the test cases as possible.

### Running the tests

If you've applied to a position, and have been invited to complete this
challenge, then you should have been supplied with a link and credentials
online IDE and instructions on how to use it.

If you want to work on this on your own computer, follow these instructions.

#### Prerequisits
1. Python 3.7.10 (or higher)
1. Git

#### Building
##### Windows (Powershell)
```ps1
git clone https://github.com/FocalPointNDE/blob-take-home # clone the repo
cd blob-take-home               # move into the repo directory
python -m venv env              # make a virtual python environment
.\env\Scripts\activate          # activate the virtual python environment
pip install -r requirements.txt # install the required dependencies
python find_blobs.py            # runs the tests
# ... hack away on find_blobs.py (don't forget to save) ...
python find_blobs.py            # keep running tests to check your progress
# ... repeat ...
```

##### OSX, Linux, or Unix-like (bash)
```bash
git clone https://github.com/FocalPointNDE/blob-take-home # clone the repo
cd blob-take-home                # move into the repo directory
python3 -m venv env              # make a virtual python environment
./env/bin/activate               # activate the virtual python environment
pip3 install -r requirements.txt # install the required dependencies
python3 find_blobs.py            # runs the tests
# ... hack away on find_blobs.py (don't forget to save) ...
python3 find_blobs.py            # keep running tests to check your progress
# ... repeat ...
```

### Resources

The provided project imports the SciPy and NumPi Python package, and you
are welcome to use any of its modules. You may specifically find
[`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html) and
[`scipy.ndimage`](https://docs.scipy.org/doc/scipy/reference/ndimage.html)
helpful.

You can also e-mail `tdunlap` `AT` `utex` `DOT` `com` if you have any questions or get stuck.