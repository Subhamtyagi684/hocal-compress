from PIL import Image
import PIL.Image
import os
import argparse
import sys


def getQuality(img):
    bytes = img.tobytes()
    quality = 60
    fileSize = sys.getsizeof(bytes);
    
    if(fileSize > 1024*1024):
        quality = 30;
    elif(fileSize > 1024*512):
        quality = 40;
    elif(fileSize > 1024*256):
        quality = 50;
    return quality;

     
def resize_image(origImage,reqWidth,reqHeight):
    srcWidth = origImage.size[0];
    srcHeight = origImage.size[1];
    scaleX = float(srcWidth / reqWidth);
    scaleY = float(srcHeight / reqHeight);
    scale =  scaleY if scaleX > scaleY else scaleX  
    finalHeight  = int(reqHeight*scale);
    finalWidth  = int(reqWidth*scale);
    x = int((srcWidth -finalWidth)/2);
    y = int((srcHeight -finalHeight)/2);
    vals = [x,y,finalWidth+x,finalHeight+y];
    return vals;

def get_image(obj):
    my_image = None;
    width = obj['width'];
    height = obj['height']
    image_path = obj['src'];
    ext = obj['type']
    file_path = obj['file'];
    folder_path = obj['folder']
    dest_path = './'
    if file_path:
        dest_path = file_path
        ext = getExtensionFrom(dest_path)
    elif folder_path:
        dest_path = folder_path
        if not dest_path.endswith('/'):
            dest_path+='/'
    
    image_name = str(image_path).split("/")[-1];
    try:
        with Image.open(image_path) as image:
            my_image = image.copy();
    except Exception as e:
        print("Something went wrong:",'{',e,'}');
        return;

    if(my_image!=None):
        if (width and height):
            getResizingDimensions = resize_image(my_image,int(width),int(height));
            print("[+] Original dimension: "+str(my_image.size)+str(" Resized dimension ")+str(getResizingDimensions));
            top = getResizingDimensions[0];
            upper = getResizingDimensions[1];
            fwidth = getResizingDimensions[2];
            fheight = getResizingDimensions[3];
            z = my_image.crop((top,upper,fwidth,fheight)).resize((int(width),int(height)),resample=PIL.Image.ADAPTIVE).convert("RGB");
            if file_path:
                z.save(f"{dest_path}",ext,quality=getQuality(z),optimize=True);
            else:
                filename, dext = os.path.splitext(image_name)
                z.save(f"{dest_path}{filename}.{ext}",ext,quality=getQuality(z),optimize=True);
        
        else:
            width = my_image.size[0];
            height = my_image.size[1];
            
            z = my_image.resize((int(width),int(height)),resample=PIL.Image.ADAPTIVE).convert("RGB")
            if file_path:
                z.save(f"{dest_path}",ext,quality=getQuality(z),optimize=True);
            else:
                filename, dext = os.path.splitext(image_name)
                z.save(f"{dest_path}{filename}.{ext}",ext,quality=getQuality(z),optimize=True);
        print("[+] New file saved");
    else:
        print("Something went wrong while using resizing function")
    return;

def getExtensionFrom(name):
    nExt =  os.path.splitext(name)[1];
    if nExt:
        x = str(nExt.split('.')[-1]);
        nExt = 'JPEG' if x.lower() == 'jpg' else x.upper();
    else:
        nExt = 'webp';
    return nExt;



if(__name__=="__main__"):
    parser = argparse.ArgumentParser(description="Simple Python script for compressing and resizing images")
    parser.add_argument("src", help="Target image to compress and/or resize")
    parser.add_argument("-file", "--file", type=str, help="name of the file as of same name it will saved")
    parser.add_argument("-folder", "--folder", type=str, help="folder in which it have to be saved")
    parser.add_argument("-t", "--type", type=str, help="Extension to save image after compression",default="webp")
    parser.add_argument("-width", "--width", type=int, help="The new width image, make sure to set it with the `height` parameter")
    parser.add_argument("-height", "--height", type=int, help="The new height for the image, make sure to set it with the `width` parameter")
    args = vars(parser.parse_args());
    width = args['width'];
    height = args['height'];

    if(args['type']!="webp" and (args['type'] not in ['jpg','jpeg','png'])):
        print("Please check your type of extension again, valid extensions are only jpg, jpeg, png ");
        exit();
    else:
        get_image(args);
