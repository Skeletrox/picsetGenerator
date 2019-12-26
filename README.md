# PicSetGenerator

I wrote this because of the many, *many* different ways image datasets were used for image classification / object detection / whatever. Decided to build one for myself that I think scales well and makes sense.

## How does it work?

`capturer.py` holds code that captures webcam input and stores values. You can modify that to suit your needs, say if you're taking from an image stream or whatever.

## What is Monte Carlo? Do I get to meet Charles LeClerc?

The Monte Carlo method goes under the axiom that given a sufficiently large number, enough data points from a distribution will exhibit characteristics of the same distribution. Named after the Monte Carlo Casino in Monaco, where one can get the probability of making bank by repeatedly trying to win and observing the pattern of victory over thousands of examples.

In this context, the Monte Carlo method of splitting train and test simply generates a random number each time a picture is taken and places it in the appropriate "train" or "test" datasets. This is useful when you want to work with large datasets so that you don't have to worry about again splitting over train and test. I wouldn't recommend this for smaller datasets (again, my version of small is <20 images).

Unfortunately you don't get to meet Charles LeClerc.

## Can I write my own collector?

Be my guest. Multiple sources are always better and inputs are always welcome.
