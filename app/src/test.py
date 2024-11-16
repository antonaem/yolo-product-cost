# import onnx2pytorch
# import torch
# import torch.onnx
#
# # Загрузите вашу модель PyTorch
# model = torch.load('runs/detect/train2/weights/best.pt', weights_only=False)
#
# # Задайте входные данные для вашей модели
# input_data = torch.randn(1, 3, 224, 224)
#
# # Преобразуйте модель в ONNX
# torch.onnx.export(model, input_data, "model.onnx")
#
# # Преобразуйте модель ONNX в PTL
# onnx2pytorch("model.onnx", "runs/detect/train2/weights/model.ptl")
#

import os

label_letter_latin = {
                        0: 'a', 1: 'b', 2: 'c', 3: 'd',
                        4: 'e', 5: 'f', 6:'g', 7: 'h',
                        8: 'i', 9: 'j', 10: 'k', 11: 'l',
                        12: 'm', 13: 'n', 14: 'o', 15: 'p',
                        16: 'q', 17: 'r', 18: 's', 19: 't',
                        20: 'u', 21: 'v', 22: 'w', 23: 'x',
                        24: 'y', 25: 'z'
                    }

label_map_cyrillic = {
    0: 'а', 1: 'б', 2: 'в', 3: 'г',
    4: 'д', 5: 'е', 6: 'ё', 7: 'ж',
    8: 'з', 9: 'и', 10: 'й', 11: 'к',
    12: 'л', 13: 'м', 14: 'н', 15: 'о',
    16: 'п', 17: 'р', 18: 'с', 19: 'т',
    20: 'у', 21: 'ф', 22: 'х', 23: 'ц',
    24: 'ч', 25: 'ш', 26: 'щ', 27: 'ъ',
    28: 'ы', 29: 'ь', 30: 'э', 31: 'ю',
    32: 'я'
}


label_map = "0.501799 0.501799 0.996403 0.996403"

mypath_train = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/images/train"
mypath_val = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/images/val"


mypath_label_train = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/train"
mypath_label_val = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/val"

def recursion_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))

def rename_dir(path):
    for key, value in label_map_cyrillic.items():
        for dirs in os.listdir(path):
            if str(dirs).lower() == str(value):
                print(f"Rename {dirs} to {value}")
                os.rename(os.path.join(path, dirs), os.path.join(path, value))

def make_label_dir(img_path, label_path):
    for root, dirs, files in os.walk(img_path):
        print(os.path.join(label_path, root.split('\\')[-1]))
        os.mkdir(os.path.join(label_path, root.split('\\')[-1]))




make_label_dir(mypath_val, mypath_label_val)
# import onnx2pytorch
# import torch
# import torch.onnx
#
# # Загрузите вашу модель PyTorch
# model = torch.load('runs/detect/train2/weights/best.pt', weights_only=False)
#
# # Задайте входные данные для вашей модели
# input_data = torch.randn(1, 3, 224, 224)
#
# # Преобразуйте модель в ONNX
# torch.onnx.export(model, input_data, "model.onnx")
#
# # Преобразуйте модель ONNX в PTL
# onnx2pytorch("model.onnx", "runs/detect/train2/weights/model.ptl")
#

import os

label_letter_latin = {
                        0: 'a', 1: 'b', 2: 'c', 3: 'd',
                        4: 'e', 5: 'f', 6:'g', 7: 'h',
                        8: 'i', 9: 'j', 10: 'k', 11: 'l',
                        12: 'm', 13: 'n', 14: 'o', 15: 'p',
                        16: 'q', 17: 'r', 18: 's', 19: 't',
                        20: 'u', 21: 'v', 22: 'w', 23: 'x',
                        24: 'y', 25: 'z'
                    }

label_map_cyrillic = {
    0: 'а', 1: 'б', 2: 'в', 3: 'г',
    4: 'д', 5: 'е', 6: 'ё', 7: 'ж',
    8: 'з', 9: 'и', 10: 'й', 11: 'к',
    12: 'л', 13: 'м', 14: 'н', 15: 'о',
    16: 'п', 17: 'р', 18: 'с', 19: 'т',
    20: 'у', 21: 'ф', 22: 'х', 23: 'ц',
    24: 'ч', 25: 'ш', 26: 'щ', 27: 'ъ',
    28: 'ы', 29: 'ь', 30: 'э', 31: 'ю',
    32: 'я'
}


label_map = "0.501799 0.501799 0.996403 0.996403"

mypath_train = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/images/train"
mypath_val = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/images/val"


mypath_label_train = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/train"
mypath_label_val = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/val"

def recursion_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))

def rename_dir(path):
    for key, value in label_map_cyrillic.items():
        for dirs in os.listdir(path):
            if str(dirs).lower() == str(value):
                print(f"Rename {dirs} to {value}")
                os.rename(os.path.join(path, dirs), os.path.join(path, value))

def make_label_dir(img_path, label_path):
    for root, dirs, files in os.walk(img_path):
        print(os.path.join(label_path, root.split('\\')[-1]))
        os.mkdir(os.path.join(label_path, root.split('\\')[-1]))




make_label_dir(mypath_val, mypath_label_val)
# import onnx2pytorch
# import torch
# import torch.onnx
#
# # Загрузите вашу модель PyTorch
# model = torch.load('runs/detect/train2/weights/best.pt', weights_only=False)
#
# # Задайте входные данные для вашей модели
# input_data = torch.randn(1, 3, 224, 224)
#
# # Преобразуйте модель в ONNX
# torch.onnx.export(model, input_data, "model.onnx")
#
# # Преобразуйте модель ONNX в PTL
# onnx2pytorch("model.onnx", "runs/detect/train2/weights/model.ptl")
#

import os

label_letter_latin = {
                        0: 'a', 1: 'b', 2: 'c', 3: 'd',
                        4: 'e', 5: 'f', 6:'g', 7: 'h',
                        8: 'i', 9: 'j', 10: 'k', 11: 'l',
                        12: 'm', 13: 'n', 14: 'o', 15: 'p',
                        16: 'q', 17: 'r', 18: 's', 19: 't',
                        20: 'u', 21: 'v', 22: 'w', 23: 'x',
                        24: 'y', 25: 'z'
                    }

label_map_cyrillic = {
    0: 'а', 1: 'б', 2: 'в', 3: 'г',
    4: 'д', 5: 'е', 6: 'ё', 7: 'ж',
    8: 'з', 9: 'и', 10: 'й', 11: 'к',
    12: 'л', 13: 'м', 14: 'н', 15: 'о',
    16: 'п', 17: 'р', 18: 'с', 19: 'т',
    20: 'у', 21: 'ф', 22: 'х', 23: 'ц',
    24: 'ч', 25: 'ш', 26: 'щ', 27: 'ъ',
    28: 'ы', 29: 'ь', 30: 'э', 31: 'ю',
    32: 'я'
}


label_map = "0.501799 0.501799 0.996403 0.996403"

mypath_train = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/images/train"
mypath_val = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/images/val"


mypath_label_train = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/train"
mypath_label_val = "../../Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/val"

def recursion_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))

def rename_dir(path):
    for key, value in label_map_cyrillic.items():
        for dirs in os.listdir(path):
            if str(dirs).lower() == str(value):
                print(f"Rename {dirs} to {value}")
                os.rename(os.path.join(path, dirs), os.path.join(path, value))

def make_label_dir(img_path, label_path):
    for root, dirs, files in os.walk(img_path):
        print(os.path.join(label_path, root.split('\\')[-1]))
        os.mkdir(os.path.join(label_path, root.split('\\')[-1]))




make_label_dir(mypath_val, mypath_label_val)