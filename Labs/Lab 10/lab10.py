import cImage as image

def duplicate(input_img, output_img):
    img = image.Image(input_img)
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width,height)

    for col in range(width):
        for row in range(height):
            px = img.getPixel(col,row)
            newimg.setPixel(col,row,px)

    newimg.saveTk(output_img)    

def flip_horizontal(input_img, output_img):
    img = image.Image(input_img)
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width,height)
    
    for col in range(width):
        for row in range(height):
            px = img.getPixel(width - 1 - col,row)
            newimg.setPixel(col,row,px)
    
    newimg.saveTk(output_img)    
    
def flip_vertical(input_img, output_img):
    img = image.Image(input_img)
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width,height)
    
    for col in range(width):
        for row in range(height):
            px = img.getPixel(col,height - 1 - row)
            newimg.setPixel(col,row,px)
    
    newimg.saveTk(output_img)  

def enlarge(input_img, output_img):
    img = image.Image(input_img)
    
    scale = ""
    while scale == "":
        try:
            scale = int(input("How big do you want the new picture compared to the original? "))
        except ValueError:
            print("Error: You must enter an integer!")
            
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width*scale,height*scale)    

    for col in range(width):
        for row in range(height):
            px = img.getPixel(col,row)
            newimg.setPixel(col*scale,row*scale,px)
            for x in range(1,scale):
                for y in range(1, scale):
                    newimg.setPixel(col*scale + x,row*scale,px)
                    newimg.setPixel(col*scale,row*scale + y,px)
                    newimg.setPixel(col*scale + x,row*scale + y,px)

    newimg.saveTk(output_img)

#name = input("Input the image file name to edit: ")
name = "beepbeep.gif"
splitName = name.split(".")
print("How do you want to work with the image?")
print("1. Duplicate\n2. Flip Horizontally\n3. Flip Vertically\n4. Change Size")
prompt = ""
while prompt not in ['1', '2', '3', '4']:
    prompt = input("Enter your option: ")
    if prompt not in ['1', '2', '3', '4']:
        print("You must enter an integer (1 to 4) to choose an option!")
if prompt == '1':
    duplicate(name, splitName[0]+"_duplicate."+splitName[1])
elif prompt == '2':
    flip_horizontal(name, splitName[0]+"_hFlip."+splitName[1])
elif prompt == '3':
    flip_vertical(name, splitName[0]+"_vFlip."+splitName[1])
else:
    enlarge(name, splitName[0]+"_enlarge."+splitName[1])