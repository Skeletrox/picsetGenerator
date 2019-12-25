import cv2
import os


def write(chunks, dsetType, label):
    path = "dataset/{}/{}".format(label, dsetType)
    if not os.path.exists(path):
        os.makedirs(path)
    for i,c in enumerate(chunks):
        cv2.imwrite("{}/{}.png".format(path, "{}_{}_{}".format(label, dsetType, i)), c)