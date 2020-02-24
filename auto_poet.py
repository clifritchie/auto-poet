#!/usr/bin/python3

"""
Simple runnner script to demonstrate Auto-poet functionality
"""

from src.poet import Poet
from src.superimposer import Superimposer
from src.juxtaposer import Juxtaposer
from src.square_thumber import SquareThumber

my_poem = Poet()
my_poem.get_images()

Superimposer(my_poem.identifier, maintain_ratio=True)
Juxtaposer(my_poem.identifier)
SquareThumber(my_poem.identifier)