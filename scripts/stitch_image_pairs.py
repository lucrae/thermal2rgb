from pathlib import Path


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def stitch_image_pairs(dir_a: Path, dir_b: Path, dir_save: Path):

    for (path_a, path_b) in zip(dir_a.glob('*.jpg'), dir_b.glob('*.jpg')):

        print(f'Processing {path_a} & {path_b}...')

        # check pairing
        assert path_a.name == path_b.name

        # stitch images
        image_a = np.array(Image.open(path_a))
        image_b = np.array(Image.open(path_b))
        image_both = np.hstack([image_a, image_b])

        # save
        Image.fromarray(image_both).save(dir_save / path_a.name)



if __name__ == '__main__':

    DIR_ROOT = Path('../data/tufts_face_rgb_ir_v2/train')
    DIR_A = DIR_ROOT / 'a'
    DIR_B = DIR_ROOT / 'b'
    DIR_SAVE = Path('../data/tufts_face_rgb_ir_v2_stitched/train')

    stitch_image_pairs(DIR_A, DIR_B, DIR_SAVE)





