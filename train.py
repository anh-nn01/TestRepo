import torch
import torchvision
import torchvision.models as models
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import cv2

models = models.resnet34(pretrained=True)

