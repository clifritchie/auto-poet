# Auto-poet
```(\ 
\'\ 
 \'\     __________  
 / '|   ()_________)
 \ '/    \ ~~~~~~~~ \
   \       \ ~~~~~~   \
   ==).      \__________\
  (__)       ()__________)
  ```
Creates and visualizes verbal art

## Description

This project randomly selects from a set of predefined terms and puts them together to form a coherant poem.
Each line of the poem is run a public Google Image search. Those results are combined in various ways to show all images at once as a visual representation of the poem.

## Examples
Check out the `/examples` folder for an idea of what this does.

## Installation

1. From a Python 3.8.0 virtual environment, run `pip install -r requirements.txt`

## Usage
1. Run `python auto_poet.py` to generate a poem and associated images
2. Check `/output` folder to view results
3. To use alternative term sets, modify the text files in `/text`

* Notice output files are named according to epoch timestamps. This is both for uniqueness and to provide a convenient reference. Every image output you produce will begin with the same id as the `.txt` file of its associated poem. This also allows for reprocessing of previously generated poems. In case you want to use different image parameters, you can pass that id to any of the outputters for reproccessing.


## Known Issues

* As of late February 2020, Google has changed the format of image search results, breaking the `google_images_download` dependency of this project. That's just how webscraping goes. I'll implement a fix once available, but until then, image downloading isn't available.
* Some search terms won't yield results from Google Images. Still, most search terms will yield results, and whatever images do get downloaded will be combined.

## Overwrought Artsy Explanation

Code has a reputation for removing the human element from much of our lives. Automation, machine learning, and electronic communications force us to interface with devices rather than people. It can feel alienating and dehumanizing to imagine a future where computers make decisions for us, whether important or arbitrary. 

This overlooks the reality that code is an extension of ourselves. It’s another tool that we use, as complex and fraught as it may seem. We provide parameters, set rules, and make adjustments to code, with computers having no choice but to carry out exactly what we’ve instructed. The results are not magical nor mechanical like they’re often made out to be. They’re the precise consequence of human actions reaching an entirely logical conclusion, even if we can’t fully predict all outcomes.

As a simple demonstration, this project starts by randomly bringing together words from a curated list of phrases. The rules are set so that a grammatical pattern is met, resembling an organically produced poem. Code does the work of combining phrases in a way that the author may not intend or expect, but the available words are very intentionally provided by the author, as are the rules by which the code combines words. 

The code then performs a search of publicly available images for each phrase generated. Each image fetched is programmatically overlaid so that every phrase in the poem can be viewed at once. While the images are provided by a search engine without human curation, the relevance of search engine results is not the decision of computers. It’s driven by how human users have provided and interacted with content.
