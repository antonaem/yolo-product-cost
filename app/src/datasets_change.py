import glob, os
from math import *
from tqdm import tqdm
import shutil

input_folders = [
    '../../Cyrillic/Cyrillic/I/',
    '../../Cyrillic/Cyrillic/А/',
    '../../Cyrillic/Cyrillic/Б/',
    '../../Cyrillic/Cyrillic/В/',
    '../../Cyrillic/Cyrillic/Г/',
    '../../Cyrillic/Cyrillic/Д/',
    '../../Cyrillic/Cyrillic/Е/',
    '../../Cyrillic/Cyrillic/Ж/',
    '../../Cyrillic/Cyrillic/З/',
    '../../Cyrillic/Cyrillic/И/',
    '../../Cyrillic/Cyrillic/Й/',
    '../../Cyrillic/Cyrillic/К/',
    '../../Cyrillic/Cyrillic/Л/',
    '../../Cyrillic/Cyrillic/М/',
    '../../Cyrillic/Cyrillic/Н/',
    '../../Cyrillic/Cyrillic/О/',
    '../../Cyrillic/Cyrillic/П/',
    '../../Cyrillic/Cyrillic/Р/',
    '../../Cyrillic/Cyrillic/С/',
    '../../Cyrillic/Cyrillic/Т/',
    '../../Cyrillic/Cyrillic/У/',
    '../../Cyrillic/Cyrillic/Ф/',
    '../../Cyrillic/Cyrillic/Х/',
    '../../Cyrillic/Cyrillic/Ц/',
    '../../Cyrillic/Cyrillic/Ч/',
    '../../Cyrillic/Cyrillic/Ш/',
    '../../Cyrillic/Cyrillic/Щ/',
    '../../Cyrillic/Cyrillic/Ъ/',
    '../../Cyrillic/Cyrillic/Ы/',
    '../../Cyrillic/Cyrillic/Ь/',
    '../../Cyrillic/Cyrillic/Э/',
    '../../Cyrillic/Cyrillic/Ю/',
    '../../Cyrillic/Cyrillic/Я/'
]

BASE_DIR_ABSOLUTE = 'C:\\Users\Administrator\\IdeaProjects\\yolo-product-cost\\Cyrillic\\Cyrillic\\'
OUT_DIR = 'datasets/datasets_prepaired'

OUT_TRAIN = OUT_DIR + '/train/'
OUT_VAL = OUT_DIR + '/test/'

coeff = [80, 20]
excepstions = ['classes']

if int(coeff[0]) + int(coeff[1]) > 100:
    print('Error: coeffs must be less than 100')
    exit(1)

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

print(f'Preparing images data by {coeff[0]/coeff[1]} rule')
print(f'Source folders: {len(input_folders)}')
print('Preparing...')

source = {}

for sf in input_folders:
    source.setdefault(sf, [])

    os.chdir(BASE_DIR_ABSOLUTE)
    os.chdir(sf)

    for filename in glob.glob('*.png'):
        source[sf].append(filename)

train = {}
val = {}
for sk, sv in source.items():
    chunks = 10
    train_chunk = floor(chunks * (coeff[0]/ 100))
    val_chunk = chunks - train_chunk
    train.setdefault(sk, [])
    val.setdefault(sk, [])
    for item in chunker(sv, chunks):
        train[sk].extend(item[0:train_chunk])
        val[sk].extend(item[train_chunk:])

train_sum = 0
val_sum = 0

for sk, sv in train.items():
    train_sum += len(sv)

for sk, sv in val.items():
    val_sum += len(sv)

print(f'Overall TRAIN images count: {train_sum}')
print(f'Overall VAL images count: {val_sum}')

os.chdir(BASE_DIR_ABSOLUTE)
print(f'Copying TRAIN images')
for sk, sv in tqdm(train.items()):
    for item in tqdm(sv):
        imgfile_source = sk + item
        imgfile_dest = OUT_TRAIN + sk.split('/')[-2] + '/'

        os.makedirs(imgfile_dest, exist_ok=True)
        shutil.copyfile(imgfile_source, imgfile_dest + item)

os.chdir(BASE_DIR_ABSOLUTE)
print(f'Copying VAL images')
for sk, sv in tqdm(val.items()):
    for item in tqdm(sv):
        imgfile_source = sk + item
        imgfile_dest = OUT_VAL + sk.split('/')[-2] + '/'

        os.makedirs(imgfile_dest, exist_ok=True)
        shutil.copyfile(imgfile_source, imgfile_dest + item)

print('Done')