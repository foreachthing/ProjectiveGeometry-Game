#!/usr/bin/env python
import os
import sys
import logging
from time import strftime
from PIL import Image, ImageOps
from glob import glob
import math
import random


def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, ((size - x) / 2, (size - y) / 2))
    return new_im


def generate_card_image(filenames, output_fn, width=2000, height=2000):
    '''
    :date: 12.11.2016
    :author: ghildebrand
    :info:
    :param:
    :return:
    '''
    # open all images
    images = [Image.open(filename) for filename in filenames]
    # create white background put color=(0,0,0,0) for transparent
    background = Image.new(mode='RGBA', size=(width, height), color=(255,255,255,0))
    num_images = len(images)-1 # substract the one in the center
    # angel to move images
    bg_w, bg_h = background.size
    # resize images
    # less than 4x4
    image_end_size = bg_w/4., bg_w/4.
    logging.debug("Resizing images to {} x {}!".format(image_end_size[0], image_end_size[1]))
    for i, img in enumerate(images):
        # replace images in place
        # make images symmetric

        # print(img.size)
        # add some randomness to size
        # add some randomness to rotation
        # rand_scaling = random.sample([0.9, 0.85, 0.95, 0.99], 1)[0]  # scale size
        rand_scaling = random.sample(range(50, 100), 1)[0]/100  # scale size
        rand_angel = random.sample(range(0, 360), 1)[0]  # select randoms from 360 degrees
        rand_size = int(image_end_size[0]*rand_scaling), int(image_end_size[1]*rand_scaling)
        # rotate expand resize
        img = img.rotate(rand_angel, expand=1).resize(rand_size)  # rotate
        # remove transparent backgrounds
        try:
            canvas = Image.new('RGBA', img.size, (255, 255, 255, 0))  # Empty canvas colour (r,g,b,a)
            # convert our image to RGB, so its masking
            img = img.convert("RGBA")
            canvas.paste(img, mask=img)  # Paste the image onto the canvas, using it's alpha channel as mask
            canvas.thumbnail([width, height], Image.ANTIALIAS)
            images[i] = canvas  # save back to array
            # inbetween save for debugging
            # img.save(filenames[i].split('/')[-1] + '.png')
        except ValueError:
            images[i] = img

    # icon image width and height
    # take first one as reference
    img_w, img_h = images[0].size
    # center of the iamge
    center_offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))
    for i, img in enumerate(images):
        # substract center image and move angle
        img_w, img_h = img.size
        angle = 360 / num_images * (i-1) # divide circle in arc that are fitting the number of images
        logging.debug("Modifying image {}".format(filenames[i]))
        if i == 0:
            # put image to center
            img_offset = center_offset
        else:
            # place image on circle around center
            # use rotation matrix for that
            # 1. determine angle per image
            # 2. apply rotation matrix and rotate the coordingtes against clock
            # around the origin --> commutativity of matrix mult...
            x, y = img_w/2+images[0].size[0]/2, img_h/2+images[0].size[1]/2 # add space center image from center current image
            x_new = math.cos(math.radians(angle))*x - math.sin(math.radians(angle))*y
            y_new = math.sin(math.radians(angle))*x + math.cos(math.radians(angle))*y
            # 3 add to center
            img_offset = (center_offset[0]+x_new, center_offset[1]+y_new)
            #print(filenames[i], img_offset)
        # save image, third param indicates the mask to be used
        # set background of the image
        background.paste(img, (int(img_offset[0]), int(img_offset[1])), mask=None)
        # add 10 % boarder
        #background_with_boarder = ImageOps.expand(background, border=int(background.size[0]/10), fill='white')
        background_with_boarder = ImageOps.expand(background, border=int(0), fill='white')
    #background = background.crop((0, 0, max_x, max_y))
    background_with_boarder.save(output_fn)
    return True
