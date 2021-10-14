# Find the blobs

## Significance of "Blobs" in NDE

Non-destructive examination could be oversimplified as using an insturment
(e.g. ultasonic transmitor or x-ray radiographer) to "look into" an object
without taking it apart and looking for "blobs" (i.e. signal) where you expect
there to be holes, seams, rivets, etc. You also look for there to be no "blobs"
where the object should be solid. Seeing a blob here could be an indication of
a crack, unexpected hole, poor welding seam, etc. Therefore, it is important in
NDE to find the blobs, so that you can then proceed to determine if it's a blob
you expected to, or a blob in an unexpected place indicating a defect.

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
  [7,3],
  [7,7]
]
```

You are provided with the a python project specifything a function
`FindBlobs(imagePage)` that can open an image and identify trivially simple
blobs. You are also provided with a (failing) test suite specifying more
complex images. Your goal is to improve `FindBlobs` so that it passes as many
of the test cases as possible.

### Running the tests

TODO...

### Resources The provided project imports the SciPy Python package, and you
are welcome to use any of its modules. You may specifically find
[`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html)
helpful.
