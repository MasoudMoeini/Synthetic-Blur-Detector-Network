from PIL import Image
import glob
import os
import shutil
#new_path = 'blurDataset/train/images' 
#folder= 'blurDataset/images/' 
def resize_images(new_path,folder):
    temp = 'temp'
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    if not os.path.exists(temp):
        os.makedirs(temp)
    # loop over existing images and resize
    # change path to your path
    
    images_list=os.listdir(folder)
    i=0
    # the only solution to keep input/output with same orde is to make sure they
    # have the same names
    for item in images_list:
        im = Image.open(folder+item)
        im.save(temp +'/' + item[0:-6]+'.jpg', 'JPEG', quality=90)
        i+=1 
    for filename in glob.glob(temp+'/' +'*.jpg'): #path of raw images
        img = Image.open(filename).resize((224,224))
        # save resized images to new folder with existing filename
        img.save('{}{}{}'.format(new_path,'/',os.path.split(filename)[1]))
    shutil.rmtree(temp)
    
