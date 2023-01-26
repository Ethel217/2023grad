# usage: check the result

import os
import shutil
import random

source_path_1 = os.path.abspath(r'inputs/pancreas_test/images')
source_path_2 = os.path.abspath(r'outputs/exp0/0')

images = os.listdir(source_path_1)
outputs = os.listdir(source_path_2)

test = []
count = 0

for i in images:
	portion = i.split('.',1)
	if (portion[0]+".jpg") not in outputs:
		count += 1
		test.append(i)
print(test)
print(count)