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
label_map_cyrillic_inverse = {
    "а": 0, "б": 1, "в": 2, "г": 3,
    "д": 4, "е": 5, "ё": 6, "ж": 7,
    "з": 8, "и": 9, "й": 10, "к": 11,
    "л": 12, "м": 13, "н": 14, "о": 15,
    "п": 16, "р": 17, "с": 18, "т": 19,
    "у": 20, "ф": 21, "х": 22, "ц": 23,
    "ч": 24, "ш": 25, "щ": 26, "ъ": 27,
    "ы": 28, "ь": 29, "э": 30, "ю": 31,
    "я": 32
}

label_map = "0.501799 0.501799 0.996403 0.996403"

mypath_train = "./Cyrillic/Cyrillic/datasets/datasets_prepaired/images/train"
mypath_val = "./Cyrillic/Cyrillic/datasets/datasets_prepaired/images/val"


mypath_label_train = "./Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/train"
mypath_label_val = "./Cyrillic/Cyrillic/datasets/datasets_prepaired/labels/val"

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

def make_label_dirs(img_path, label_path):
    for root, dirs, files in os.walk(img_path):
        for file in files:
            if file.endswith(".png"):
                label_name = file.split('.')[0] + ".txt"
                label_path_name = f"{label_path}/" + root.split('\\')[-1] + f"/{label_name}"
                print(label_path_name)
                print(label_map_cyrillic_inverse[root.split('\\')[-1]])
                os.makedirs(f"{label_path}/" + root.split('\\')[-1], exist_ok=True)
                with open(label_path_name, "w") as f:
                    f.write(str(label_map_cyrillic_inverse[root.split('\\')[-1]]) + " " + label_map)
                # for key, value in label_map_cyrillic.items():
                #     if root.split('\\')[-1] == value:
                #         print(root.split('\\')[-1], f"= {key} with value {value}")


    # print(os.path.abspath(img_path)[0:54])
    # for root, dirs, files in os.walk(img_path):
    #     dir_name = f"{label_path}/" + root.split('\\')[-1]
    #     print(f"{os.path.abspath(img_path)[0:54]}{label_path}/" + root.split('\\')[-1])
    #     os.mkdir(dir_name)

make_label_dirs(mypath_val, mypath_label_val)