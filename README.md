# Selective Search

[![PyPI](https://img.shields.io/pypi/v/selective_search)](https://pypi.org/project/selective-search/)
[![Travis Build Status](https://travis-ci.org/ChenjieXu/selective_search.svg?branch=master)](https://travis-ci.org/ChenjieXu/selective_search)
[![Codacy grade](https://img.shields.io/codacy/grade/8d5b9ce875004d458bdf570f4d719472)](https://www.codacy.com/manual/ChenjieXu/selective_search)

This is a full implementation of selective search in Python. The implementation is typically based on this paper[[1]](#Uijlings). It have three selective search modes according to various diversification strategies as in the paper.

## Installation
Installing from [PyPI](https://pypi.org/project/selective-search/) is recommended :
```
$ pip install selective-search
```
It is also possible to install the latest version from [Github source](https://github.com/ChenjieXu/selective_search/):
```
$ git clone https://github.com/ChenjieXu/selective_search.git
$ cd selective_search
$ python setup.py install
```

## Quick Start

```python
import skimage.io
from selective_search import selective_search

# Load image as NumPy array from image files
image = skimage.io.imread('path/to/image')

# Run selective search using single mode
boxes = selective_search(image, mode='single')
```
For detailed examples, refer [this](https://github.com/ChenjieXu/selective_search/tree/master/examples) part of the repository.

## Search Mode
| Mode    | Color Spaces        | Similarity Measures | Starting Regions (k) | Number of Combinations |
|---------|---------------------|---------------------|----------------------|------------------------|
| single  | HSV                 | CTSF                | 100                  | 1                      |
| fast    | HSV, Lab            | CTSF, TSF           | 50, 100              | 8                      |
| quality | HSV, Lab, rgI, H, I | CTSF, TSF, F, S     | 50, 100, 150, 300    | 80                     |

## References
\[1\] <a name="Uijlings"> [J. R. R. Uijlings et al., Selective Search for Object Recognition, IJCV, 2013](https://ivi.fnwi.uva.nl/isis/publications/bibtexbrowser.php?key=UijlingsIJCV2013&bib=all.bib)
