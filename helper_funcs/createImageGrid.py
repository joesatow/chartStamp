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

    for file in os.listdir(f"{homePath}/images/{chartSaveFolder}"):
        if file.endswith(".png"):
            image = os.path.join(f"{homePath}/images/{chartSaveFolder}", file)
            transformed_tensor = transform(read_image(image))
            tensors.append(transformed_tensor)

    grid = make_grid(tensors, nrow=2, padding=2)

    save_image(grid, f"{homePath}/images/results/grid-{chartSaveFolder}.jpg")