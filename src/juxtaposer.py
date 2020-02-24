from PIL import Image
from src.outputter import Outputter


class Juxtaposer(Outputter):
    """
    Plops an arbitrary number of images side by side in a single output image

    Args:
        directory (string): Path to input image files
    """

    def __init__(self, directory):
        super().__init__(directory, width=0)
        self.juxtapose()

    def preprocessor(self, pic):
        """
        Check the height of a pic so the maximum height of all pics is known
        Args:
            pic (str): Path to image file
        """
        img = Image.open(pic)
        img_width, img_height = img.size[0], img.size[1]
        if self.max_height is None or img_height > self.max_height:
            self.max_height = img_height
        self.width += img_width
        return img

    def juxtapose(self):
        """
        Combine pics side by side and save an output
        """
        self.out_image = Image.new("RGBA", (self.width, self.max_height))
        width_position = 0
        for img in self.pics:
            img_width, img_height = img.size[0], img.size[1]
            self.out_image.paste(img, (width_position, (self.max_height - img_height) // 2))
            width_position += img_width
        super().save_output(style="juxtaposed", format="PNG")
