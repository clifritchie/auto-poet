import os
from google_images_download import google_images_download

dir_path = os.getcwd()


class ImageDownloader:
    def __init__(self, queries, output_dir):
        self.output_dir = output_dir
        self.response = google_images_download.googleimagesdownload()
        self.downloadimages(queries)

    def downloadimages(self, queries):
        for query in queries:
            arguments = {
                "keywords": query,
                "usage_rights": "labeled-for-reuse-with-modifications",
                "output_directory": self.output_dir,
                "format": "jpg",
                "limit": 1,
                "print_urls": False,
                "size": "medium",
                "aspect_ratio": "wide",
                "silent_mode": True
            }
            self.response.download(arguments)
