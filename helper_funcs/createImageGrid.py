from torchvision.io import read_image
from torchvision.utils import make_grid, save_image
from torchvision.transforms import transforms
from torchvision import torch
from . import constants

homePath = constants.HOME_PATH

import os

def createImage(chartSaveFolder):
    tensors = []

    transform = transforms.Compose([
        transforms.ConvertImageDtype(dtype=torch.float),
    ])
    
    rearrangedList = rearrangeFileList(os.listdir(f"{homePath}/images/{chartSaveFolder}"))

    for file in rearrangedList:
        if file.endswith(".png"):
            image = os.path.join(f"{homePath}/images/{chartSaveFolder}", file)
            transformed_tensor = transform(read_image(image))
            tensors.append(transformed_tensor)

    grid = make_grid(tensors, nrow=2, padding=1)

    save_image(grid, f"{homePath}/images/results/grid-{chartSaveFolder}.jpg")

def rearrangeFileList(fileList):
    newList = [None] * 4
    for filename in fileList:
        if "1w" in filename:
            newList[0] = filename
        if "1d" in filename:
            newList[1] = filename
        if "4h" in filename:
            newList[2] = filename
        if "1h" in filename:
            newList[3] = filename
    return newList
