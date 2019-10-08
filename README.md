# selective_search  
This is a full implementation of selective search in Python. The implementation is typically based on [this paper](https://staff.fnwi.uva.nl/th.gevers/pub/GeversIJCV2013.pdf). It have three selective search modes according to various diversification strategies as in the paper.

## Installation

```
$ pip install selective-search
```

## Demo  

```python
import skimage.data
from selective_search import selective_search

image = skimage.data.astronaut()
boxes = selective_search(image, mode='single')
```

## Search Mode
* single
    * HSV
    * CTSF
    * k = 100
* fast
    * HSV, Lab
    * CTSF, TSF
    * k = 50, 100
* quality
    * HSV, Lab, rgI, H, I
    * C+T+S+F, T+S+F, F, S 
    * k = 50, 100, 150, 300
