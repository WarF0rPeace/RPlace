from turtle import position
from PIL import Image
import json


def add_pattern(position: tuple, pattern_img: Image, dest_img: Image):
    
    try:

        width, height = pattern_img.size
        
        for row_idx in range(height):
            
            for col_idx in range(width):
                
                px = position[0]+col_idx
                py = position[1]+row_idx
                dest_img.putpixel(
                    
                    (
                        
                        px*3+1,
                        py*3+1
                    
                    ),
                    
                    pattern_img.getpixel(
                        
                        (
                            
                            col_idx,
                            row_idx
                        
                        )
                    
                    )
                
                )

    except:
        
        pass

def getConfig():

    with open('config.json', 'r') as f:

        return json.loads(f.read())

def toBluePrint(config, output):
    
    dest_img = Image.new('RGBA', (6000, 6000))
    
    for key in config:
    
        pattern_img = Image.open(config[key]['file_path'])
    
        if config[key]["resize"]:

            pattern_img = pattern_img.resize((config[key]["resize_x"], config[key]["resize_y"]))

        position = (config[key]['position_x'], config[key]['position_y'])
        add_pattern(position, pattern_img, dest_img)
    
    dest_img.save(output)


config = getConfig()
toBluePrint(config, "blue_print.png")