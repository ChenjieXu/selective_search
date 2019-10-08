import numpy as np
import json
from itertools import product

from skimage.segmentation import felzenszwalb
from skimage.color import rgb2hsv, rgb2lab, rgb2grey


def oversegmentation(img, k):
    """
        Generating various starting regions using the method of 
        Felzenszwalb.
        k effectively sets a scale of observation, in that 
        a larger k causes a preference for larger components.
        sigma = 0.8 which was used in the original paper.
        min_size = 100 refer to Keon's Matlab implementation.
    """
    img_seg = felzenszwalb(img, scale=k, sigma=0.8, min_size=100)
    
    return img_seg


def switch_color_space(img, target):
    """
        RGB to target color space conversion.
        I: the intensity (grey scale), Lab, rgI: the rg channels of 
        normalized RGB plus intensity, HSV, H: the Hue channel H from HSV
    """
    
    if target == 'HSV':
        return rgb2hsv(img)
    
    elif target == 'Lab':
        return rgb2lab(img)
    
    elif target == 'I':        
        return rgb2grey(img)
    
    elif target == 'rgI':
        img_rgI = np.zeros(img.shape)
        # r
        img_rgI[:,:,0] = img[:,:,0] / np.sum(img[:,:,0])
        # g
        img_rgI[:,:,1] = img[:,:,1] / np.sum(img[:,:,1])
        # I
        img_rgI[:,:,2] = rgb2grey(img)
        
        return img_rgI
    
    elif target == 'H':
        return rgb2hsv(img)[:,:,0]
    
    else:
        assert "{} is not suported.".format(target)
        
def load_strategy(mode):
    # TODO: Add support for customizing
    
    with open('./selective_search/mode.cfg','r') as f:
        cfg = json.load(f)
        
    assert mode in cfg.keys(), "{} mode is not supported".format(mode)
        
    colors, ks, sims = cfg[mode]['colors'], cfg[mode]['ks'], cfg[mode]['sims']
    
    return product(colors, ks, sims)