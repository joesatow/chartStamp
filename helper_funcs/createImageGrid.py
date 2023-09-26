from torchvision.io import read_image
from torchvision.utils import make_grid, save_image
from torchvision.transforms import transforms
from torchvision import torch

import os

def createImage():
    tensors = []

    transform = transforms.Compose([
        transforms.ConvertImageDtype(dtype=torch.float),
    ])

    for file in os.listdir('/mnt/share'):
        if file.endswith(".png"):
            image = os.path.join('/mnt/share', file)
            transformed_tensor = transform(read_image(image))
            tensors.append(transformed_tensor)

    grid = make_grid(tensors, nrow=2, padding=2)

    save_image(grid, "grid.jpg")

createImage()