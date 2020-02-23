import os
import random
import time
import logging
from src.image_downloader import ImageDownloader

dir_path = os.getcwd()
logging.getLogger().setLevel(logging.INFO)


class Poet:
    """
    Generates random poems from predefined terms, downloads related images

    Args:
        num_lines (int): Number of lines to generate after header
    """

    def __init__(self, num_lines=10):
        self.identifier = int(time.time())
        self.num_lines = num_lines
        self.poem = "She is" + "\n"
        self.subjects = open(f"{dir_path}/text/subject.txt").readlines()
        self.verbs = open(f"{dir_path}/text/verb.txt").readlines()
        self.adjectives = open(f"{dir_path}/text/adjective.txt").readlines()
        self.images = []
        self.author_poem()

    def author_poem(self):
        """
        Selects terms and outputs them as formatted poem
        """
        for i in range(self.num_lines):
            line = self.make_line()
            self.poem += line + "\n"
            self.images.append(line)
        logging.info(self.poem)
        out_path = f"{dir_path}/output/{str(self.identifier)}.txt"
        with open(out_path, "w") as output:
            output.write(self.poem)
        logging.info(f"Poem written to {out_path}")

    def get_images(self):
        """
        Pulls an image per line of poem
        """
        out_path = f"{dir_path}/cache/{self.identifier}"
        ImageDownloader(self.images, out_path)
        logging.info(f"All images downloaded to {out_path}")

    def make_line(self):
        """
        Selects terms to generate a single line of poetry
        """
        negation = random.choice([" not", ""])
        subject = random.choice(self.subjects)
        self.subjects.remove(subject)
        predicate = random.choice([self.verbs, self.adjectives])
        word_choice = random.choice(predicate)
        predicate.remove(word_choice)
        sentence = [negation, subject.strip(), word_choice.strip()]
        return " ".join(sentence).strip()
