#!/usr/bin/env python
import sys
import cv2
import pydicom
import os.path
import numpy as np


def save(src, out):
    ds = pydicom.dcmread(src, force=True)
    ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
    img = ds.pixel_array
    img = np.array(img, dtype = float)
    img = (img - img.min()) / (img.max() - img.min()) * 255.0
    img = img.astype(np.uint8)

    img_file = os.path.join(out, os.path.basename(src).replace('.dcm', '.png'))
    cv2.imwrite(img_file, img)


if __name__ == '__main__':
    save(sys.argv[1], sys.argv[2])
