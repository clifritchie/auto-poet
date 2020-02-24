import time
import os
import logging
from pathlib import Path

dir_path = os.getcwd()
logging.getLogger().setLevel(logging.INFO)


class Outputter:
    def __init__(self, directory, width, height=None, maintain_ratio=False):
        self.directory = directory
        self.width = width
        self.height = height
        self.min_height = None
        self.max_height = None
        self.maintain_ratio = maintain_ratio
        abs_path = f"{dir_path}/cache/{directory}"
        self.pics = [
            self.preprocessor(filename)
            for filename in Path(abs_path).rglob("*.*")
        ]
        if not self.pics:
            logging.error(f"No images found in {abs_path}")
            exit()

    def preprocessor(self, pic):
        return pic

    def save_output(self, style, format):
        cur = int(time.time())
        out_path = f"{dir_path}/output/{self.directory}-{cur}-{style}.{format}"
        self.out_image.save(out_path, format)
        logging.info(f"{style} image saved at {out_path}")
