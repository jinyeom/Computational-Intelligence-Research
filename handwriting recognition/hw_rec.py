import os
import Image

# define an image scanner
class ImgScanner:
    def __init__(self):
        self.path = None
        self.image = None

    # import an image using
    def import_image(self, f_name):
        self.path = os.path.join(os.path.expanduser("~"), f_name)
        self.image = f.read()

    # quit using the image scanner
    def quit(self):
