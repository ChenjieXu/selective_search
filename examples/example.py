import skimage
import selective_search

image = skimage.data.astronaut()

# Propose boxes
boxes = selective_search.selective_search(image, mode='single')

# Filter box proposals
boxes_filter = selective_search.box_filter(boxes, min_size=20, topN=80)