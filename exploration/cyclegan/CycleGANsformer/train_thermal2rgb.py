import torch
from cyclegansformer import CycleGANsformer, ImageDatasetLoader

img_ds = ImageDatasetLoader(
    '/home/lucrae/Uni/FIT2082/thermal2rgb/data/tufts_face_rgb_ir/train/b',
    '/home/lucrae/Uni/FIT2082/thermal2rgb/data/tufts_face_rgb_ir/train/a',
)
cgf = CycleGANsformer()

cgf.fit(img_ds, epochs=200, alpha_decay=True)