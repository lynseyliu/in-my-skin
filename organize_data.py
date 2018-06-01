import os
import json
import shutil

root_dir = './data/test'
for filename in os.listdir(root_dir):
    if filename.endswith('.json'):
        filenum = filename.split('.')[0]
        annotation = os.path.join(root_dir, filename)
        image = os.path.join(root_dir, filenum + '.jpg')
        with open(annotation, 'r') as fp:
            print(annotation)
            classification = json.load(fp)['meta']['clinical']['benign_malignant']
            class_location = os.path.join(root_dir + '/' + classification, filenum + '.jpg')
            try:
                shutil.move(image, class_location)
            except:
                pass
