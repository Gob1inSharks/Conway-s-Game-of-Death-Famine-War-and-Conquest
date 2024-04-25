""" 
FILENAME: utils.py 
AUTHOR:  gob1insharks
PURPOSE: make import and convert functions for convience 
""" 

import pygame 
import os 
import json 

BASE_IMAGE_PATH = 'assets//images//' 
BASE_MAP_PATH = 'assets//maps//' 
COLOUR_KEY = (0,0,0) 

def load_image(path): 

    image = pygame.image.load(BASE_IMAGE_PATH+path).convert() #convert it for better performance Uwu It helps a lot 
    image.set_colorkey(COLOUR_KEY) #changes this colour into transparent 

    return image 

def load_multiple_images(path): 

    images = [] 
    for image_name in sorted(os.listdir(BASE_IMAGE_PATH + path)): 
        images.append(load_image(path + '//' + image_name)) 

    return images 

def load_map(path): 

    with open(BASE_MAP_PATH+path,'r') as map_json: 
        tilemap = json.load(map_json) 

    return tilemap['tilemap']

