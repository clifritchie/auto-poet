from PIL import Image
from src.outputter import Outputter


class Superimposer(Outputter):
    """
    Blends an arbitrary number of images into a single output image

    Args:
        directory (str): Path to input image files
        width (int): Width in pixels of output image
        height (int): Height in pixels of output image
        maintain_ratio (bool): If set to True, images will be cropped rather
            than stretched to the output resolution
    """

    def __init__(self, directory, width=800, height=600, maintain_ratio=False):
        super().__init__(directory, width, height, maintain_ratio)
        # In case number of inputs is not a power of 2, this holds remainder to be blended
        self.leftover = []
        self.total = len(self.pics)
        self.superimpose()

    def superimpose(self):
        """
        Recursively iterates through images for combining, outputs the result
        """
        while len(self.pics) != 1:
            # Combine images in pairs until only 1 remains
            self.combine_pairs()
        self.out_image = self.pics[0]
        for image in self.leftover:
            self.out_image = self.blend(self.out_image, image, ratio=1 / self.total)
        self.save_image()

    def combine_pairs(self):
        """
        Iterates through a list of pics, blending in pairs
        """
        supers = []
        for chunk in self.chunks(self.pics):
            if len(chunk) > 1:
                supers.append(self.blend(chunk[0], chunk[1]))
            else:
                [self.leftover.append(img) for img in chunk]
        self.pics = supers

    def chunks(self, lst, size=2):
        """
        Yield successive sized chunks from a list
        Args:
            lst (list): List to be broken into chunks
            size (int): Number of elements each broken out list will contain
        """
        for pos in range(0, len(lst), size):
            yield lst[pos : pos + size]

    def preprocessor(self, pic):
        """
        Prepares an image to be blended with others.
        It will be cropped if maintain_ratio is True, otherwise stretched

        pic (str): Path to image file
        """
        if self.maintain_ratio:
            img = Image.open(pic)
            img_width, img_height = img.size[0], img.size[1]
            if self.min_height is None or img_height < self.min_height:
                self.min_height = img_height
            wpercent = self.width / float(img.size[0])
            hsize = int((float(img_height) * float(wpercent)))
            img = img.resize((self.width, hsize), Image.LANCZOS).convert("RGBA")
            img_width, img_height = img.size[0], img.size[1]
            new_img = Image.new("RGBA", (self.width, self.height))
            new_img.paste(
                img, ((self.width - img_width) // 2, (self.height - img_height) // 2)
            )
            return new_img
        else:
            return (
                Image.open(pic)
                .resize((self.width, self.height), Image.LANCZOS)
                .convert("RGBA")
            )

    def blend(self, image_a, image_b, ratio=0.5):
        """
        Blends two images

        Args:
            image_a (Image): First image to be blended
            image_b (Image): Second image to be blened
            ratio (float): Percentage of the first image to maintained in blend
        """
        return Image.blend(image_a, image_b, ratio)

    def save_image(self):
        """
        Save a resulting image blend
        """
        if self.maintain_ratio:
            top = (self.out_image.size[1] - self.min_height) // 2
            bottom = top + self.min_height
            self.out_image = self.out_image.crop((0, top, self.width, bottom))
        super().save_output(style="super", format="PNG")
