import math
from PIL import Image
from src.outputter import Outputter


class SquareThumber(Outputter):
    """
    Combines an arbitrary number of images as thumbnails in a square output

    Args:
        directory (str): Path to input image files
        width (int): Width in pixels of output image
        height (int): Height in pixels of output image
    """

    def __init__(self, directory, width=900, height=900):
        super().__init__(directory, width, height)
        self.grid_size = math.ceil(math.sqrt(len(self.pics)))
        self.out_image = Image.new("RGBA", (self.width, self.height))
        self.current_pos = 0
        self.thumber()

    def thumber(self):
        """
        Iterates through pics, outputting result
        """
        for pic in self.pics:
            self.square_crop(pic)
        super().save_output(style='thumbed', format='PNG')

    def square_crop(self, pic):
        """
        Crops a given pic, adding it the grid at the current position
        Args:
            pic (str): Path to image file
        """
        img = Image.open(pic)
        out_width = int(self.width / self.grid_size)
        out_height = int(self.height / self.grid_size)
        img_width, img_height = img.size[0], img.size[1]
        offset = (img_width - img_height) // 2
        img = img.crop((offset, 0, offset + img_height, img_height))
        img = img.resize((out_width, out_height), Image.LANCZOS).convert("RGBA")
        img_width, img_height = img.size[0], img.size[1]
        x_pos = (self.current_pos % self.grid_size) * out_width
        y_pos = (self.current_pos // self.grid_size) * out_height
        self.current_pos += 1
        self.out_image.paste(img, (x_pos, y_pos))
