from itertools import *
import logging
import random
import argparse
import sys
from draw import *


def create_cards(order):
    for min_factor in range(2, 1 + int(order ** 0.5)):
        if order % min_factor == 0:
            break
    else:
        min_factor = order
    cards = []
    for i in range(order):
        cards.append(set([i * order + j for j in range(order)] + [order * order]))
    for i in range(min_factor):
        for j in range(order):
            cards.append(set([k * order + (j + i * k) % order
                              for k in range(order)] + [order * order + 1 + i]))

    cards.append(set([order * order + i for i in range(min_factor + 1)]))
    return cards, order * order + order + 1


def check_cards(cards):
    for card, other_card in combinations(cards, 2):
        if len(card & other_card) != 1:
            print("Cards", sorted(card), "and", sorted(other_card),
                  "have intersection", sorted(card & other_card))


def make_card_pictures(cards, npics, order,imagedir, out_dir):

    # Print out the cards in a picture
    for CardNum, card in enumerate(cards):
        # Make a box to define each card]
        logging.info("Card: {} {}".format(CardNum, str(card)))
        basename = "Card-{}.png".format(CardNum)
        outfilename = os.path.join(out_dir, basename)
        files = glob(imagedir+"/*")
        # shuffle images
        card = list(card)
        random.shuffle(card)
        generate_card_image([files[i] for i in card], outfilename)
    return

if __name__ == "__main__":
    # setup logging
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
    # setup cmd line parser
    parser = argparse.ArgumentParser(description="""
        Plots the card games of the Dobble Card game.
        Original code of block algorithm forked and modified from: https://github.com/WRadigan/pySpot-It
        more information can be found here: https://de.wikipedia.org/wiki/Fano-Ebene
        """)
    parser.add_argument('-d', '--input_image_directory' ,default='input_images', type=str, help="Takes required images from input dir. For order of 5 it will  take 31")
    parser.add_argument('-o', '--output_image_directory' ,default='out_images', type=str, help="output directory of images. Default is out_images/")
    parser.add_argument('-O', '--Order' ,default=5,type=int, help="Order of blocks to compute. Defalt 5 --> 31 cards ")
    args = parser.parse_args()
    logging.log(logging.INFO, "Starting...")
    #The algorythm only works for numbers where order is a prime number (E.g. [0, 1, 2, 3, 5, 7 , 11]
    order = args.Order
    logging.info("Set of cards of order {}".format(order))
    cards, num_pictures = create_cards(order)
    logging.info("There are {0} cards and {1} pictures\n\n".format(len(cards),num_pictures))
    check_cards(cards)
    make_card_pictures(cards, num_pictures,order,imagedir=args.input_image_directory, out_dir=args.output_image_directory)
