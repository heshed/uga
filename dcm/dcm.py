#!/usr/bin/env python
import sys
import cv2
import pydicom
import os.path
import numpy as np
import wget


def save(src, out):
    ds = pydicom.dcmread(src, force=True)
    ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
    img = ds.pixel_array
    img = np.array(img, dtype = float)
    img = (img - img.min()) / (img.max() - img.min()) * 255.0
    img = img.astype(np.uint8)

    img_file = os.path.join(out, os.path.basename(src).replace('.dcm', '.png'))
    # resize
    # img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    img = cv2.resize(img, (0, 0), fx=0.9545, fy=0.9545, interpolation = cv2.INTER_NEAREST)
    cv2.imwrite(img_file, img)


def download(url, output_directory):
    filename = wget.download(url, out=output_directory)
    return filename

if __name__ == '__main__':
    filename = download(sys.argv[1], sys.argv[2])
    save(filename, sys.argv[2])
    print('remove file... ', filename)
    os.remove(filename)
