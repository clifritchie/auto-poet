import os
from google_images_download import google_images_download

dir_path = os.getcwd()


class ImageDownloader:
    """
    Wrapper to pull a Google Image per search term into an output dir

    Args:
        queries (list): Search terms to be fed into Google Images
        output_dir (string): Path to save downloaded images
    """

    def __init__(self, queries, output_dir):
        self.queries = queries
        self.output_dir = output_dir
        self.response = google_images_download.googleimagesdownload()
        self.downloadimages()

    def downloadimages(self):
        """
        Downloads one publicly usable and modifyable image from Google Images
        per search term
        """
        for query in self.queries:
            arguments = {
                "keywords": query,
                "usage_rights": "labeled-for-reuse-with-modifications",
                "output_directory": self.output_dir,
                "format": "jpg",
                "limit": 1,
                "print_urls": False,
                "size": "medium",
                "aspect_ratio": "wide",
                "silent_mode": True,
            }
            self.response.download(arguments)
