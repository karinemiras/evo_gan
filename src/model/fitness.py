import PIL

def brightimage(path="./images/Main4/Image_0.png"):
    fp = open(path,"rb")
    img = PIL.Image.open(fp)
    pix = img.load()

    brightness = 0
    for i in range(512):
        for j in range(512):
            brightness += pix[i,j][0] + pix[i,j][1] + pix[i,j][2]

    # meanbright = brightness/(3*512*512) # original
    meanbright = brightness/(3*512*512*255)

    # normalise (max 1 for all white picture)

    return meanbright
    # return meanbright, # IF ONLY EVALUATING ONE CHARACTERISTIC