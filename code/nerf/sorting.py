import os

path = os.getcwd() + '/data/nerf_synthetic/ship/train/'
print(path)
for file in os.listdir(path):
    img_type = file.split('.')
    if not img_type[1] == 'png-composite':
        os.remove(path + file)
    if img_type[1] == 'png-composite':
        os.rename(path+file, path+img_type[0]+'.png')
