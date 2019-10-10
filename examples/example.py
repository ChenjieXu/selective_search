import skimage
import selective_search

image = skimage.data.astronaut()

boxes = selective_search.selective_search(image, mode='quality')