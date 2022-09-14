
# STEPS to RUN the script:

-> Create a virtual environment with command:
###    python3 -m venv venv     

-> Activate the venv using command:
###    source/bin/activate    

-> Find the requirements.txt file. This file holds the dependencies to run the script. RUN following command to install  dependencies.

    pip install -r requirements.txt    #this will install all dependencies and adds in venv folder

-> Now , run the script file to check usage.
###    python3 customCompress.py --help


## usage: customCompress.py  src dest [-h] [-t TYPE] [-width WIDTH] [-height HEIGHT]
                        

** Simple Python script for compressing and resizing images

positional arguments:
  src                   Target image to compress and/or resize
  dest                  Path to upload compressed and/or resized image

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  Extension to save image after compression
  -width WIDTH, --width WIDTH
            The new width image, make sure to set it with the
            `height` parameter
  -height HEIGHT, --height HEIGHT
            The new height for the image, make sure to set it with
            the `width` parameter


