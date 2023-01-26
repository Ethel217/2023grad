# usage: split test set from whole set

import os
import shutil
import random

source_path = os.path.abspath(r'inputs/lecdata/images')
target_path = os.path.abspath(r'inputs/pancreas/images')
target_path_1 = os.path.abspath(r'inputs/pancreas_test/images')

source_mask_path = os.path.abspath(r'inputs/lecdata/masks/0')
target_mask_path = os.path.abspath(r'inputs/pancreas/masks/0')
target_mask_path_1 = os.path.abspath(r'inputs/pancreas_test/masks/0')

images = os.listdir(source_path)
test_images = random.sample(images, 509)
test_images.sort()
# print(test_images)

for file in images:
	portion = file.split('.',1)
	if portion[1] != "png":
		continue
	src_file = os.path.join(source_path, file)
	mask_file = os.path.join(source_mask_path, file)
	if file not in test_images:
		shutil.copy(src_file, target_path)
		shutil.copy(mask_file, target_mask_path)
	else:
		shutil.copy(src_file, target_path_1)
		shutil.copy(mask_file, target_mask_path_1)

print('copy files finished!')