import cv2
from capturer import capture
from writer import write
from sklearn.model_selection import train_test_split
import numpy as np

rand = np.random


def main():
    numClasses = int(input("Enter number of classes: "))
    numExamples = int(input("Enter number of examples: "))
    monteCarlo = input("Use Monte Carlo method for splitting dataset into train and test? [y/n]: ").upper() == "Y"
    splitPercent = float(input("Enter the train-test ratio (default: 0.8): "))
    if splitPercent >= 1 or splitPercent <= 0:
        splitPercent = 0.8

    labels = []
    for i in range(numClasses):
        train = []
        test = []
        label = input("Enter label for class number {}: ".format(i+1))
        input("Press Enter when ready to begin capturing data for {}".format(label))
        for c in capture(numExamples):
            if monteCarlo:
                if rand.rand() > splitPercent:
                    test.append(c)
                else:
                    train.append(c)
            
            else:
                train.append(c)

        if not monteCarlo:
            train, test = train_test_split(train, test_size= 1 - splitPercent)
            

        write(train, "train", label)
        write(test, "test", label)
        labels.append(label)
    
    with open("./dataset/classes.txt", "w") as txtFile:
        txtFile.write("\n".join(labels))
                



main()