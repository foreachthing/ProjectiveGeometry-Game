Python Implementation to draw cards similar to "Dobble" game
=========

At one of these afternoons we were together with the family and someone had this children card game "Dobble".
After playing it for a while there was the idea that it would be an idea amazing to have the game with personalized pictures as christmas present.
So I went to the web and quickly found an related question on stackoverflow, with a nice python example implementation already on github.

How to run:
==========
Place 31 images in "input_images"

    python create_cards.py -d input_images_directory -o out_images_directory

You will get images like the examples in out_images.


Its tested with python 2.7 and order of 5 --> 31 cards. For other configs it might be neccessary to change the code in draw.py because it may create overlays etc.
You will find the cards of the game in the out_images folder.

For those interested in the Geometry behind: https://de.wikipedia.org/wiki/Fano-Ebene

References:

*   With thanks to: Neil G. shared example code for for the question http://stackoverflow.com/questions/6240113/what-are-the-mathematical-computational-principles-behind-this-game
*   there is also an version for block design on sage math: ftp://ftp.fu-berlin.de/unix/misc/sage/linux/64bit/index.html
*   Forked and modified from: https://github.com/WRadigan/pySpot-It
