
Background
==========

At one of these afternoons we were together with the family and someone had this children card game "Dobble".
After playing it for a while there was the idea that it would be an amazing idea to have the game with personalized pictures as christmas present.
So I went to the web and quickly found an related question on stackoverflow, with a nice python example implementation already on github.

The game:
========
* On each card are O unique pictures (i.e. a card can't have 2 of the same picture)
* Given any 2 cards chosen from the deck, there is 1 and only 1 matching picture.
* Matching pictures may be scaled differently on different cards but that is only to make the game harder (i.e. a small tree still matches a larger tree)
* You can produce a deck of N cards with N images. N must be prime so there is an order O (also prime number) that satisfies:  N = O² + O + 1. Eg if you want to have a deck with 30+ images you have to have 31 images and 5 images per card. 31 = 5² + 5 +1

Number of Images and Cards:
==========

You can produce a deck of N cards with a number of O + 1 images. O (order) must be prime so the total number of cards is: N = O² + O + 1 . Eg if you want to have a deck with 30+ images you have to have 31 images and 5 images per card. 31 = 5² + 5 +1.


How to run:
==========
Place 31 images in "input_images"

Requirements:
=========

You need the pillow package installed

    pip install pillow

Than run:

    python create_cards.py -d input_images_directory -o out_images_directory -O number_of_images_per_card

Make sure that the number of images per card matches: N = O² + O + 1 (O: number of images per card, N: number of cards). Otherwise you don't create a finite geometric plane. 

You will get images like the examples in out_images like these:

<img high=400, width=400 src="https://github.com/georghildebrand/ProjectiveGeometry-Dobble-Game/blob/master/out_images/Card-0.png"></img>


Its tested with python 2.7 and order of 5 --> 31 cards. For other configs it might be neccessary to change the code in draw.py because it may create overlays etc.
You will find the cards of the game in the out_images folder.

For those interested in the Geometry behind: https://de.wikipedia.org/wiki/Fano-Ebene
Discussion on the combinatorics: [link](https://math.stackexchange.com/questions/1303497/what-is-the-algorithm-to-generate-the-cards-in-the-game-dobble-known-as-spo)

References:

*   With thanks to: Neil G. shared example code for for the question http://stackoverflow.com/questions/6240113/what-are-the-mathematical-computational-principles-behind-this-game
*   there is also an version for block design on sage math: ftp://ftp.fu-berlin.de/unix/misc/sage/linux/64bit/index.html
*   Forked and modified from: https://github.com/WRadigan/pySpot-It
