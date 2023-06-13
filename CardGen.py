#Make a folder with 20 blank image squares of random colors that are each named "Card(Number)".png"
#Then iterate over them and rename them.  Remake them as many times as you need.  In fact make a new card program.  Use Spacy.
#Write (in similar style to before) "The [noun] and the [noun]"


import spacy
from PIL import Image, ImageDraw, ImageFont
import os, glob
import random


#use Spacy to get certain words

#randomize placement of the words

#Randomize size of the words

nlp = spacy.load("en_core_web_sm")
nlp.max_length=4000000
cs=open("./Books/CanSuch.txt", "r")
cansuch=cs.read()
ps=open("./Books/Psmith.txt", "r")
psmith=ps.read()
mc=open("./Books/MonteCristo.txt", "r")
monte=mc.read()
allbooks=cansuch+psmith+monte
doc=nlp(cansuch)
doc2=nlp(psmith)
doc3=nlp(monte)

def fontsize():
    size=random.randint(20, 90)
    return size

font1 = ImageFont.truetype('BebasNeue-Regular.ttf', fontsize())
font2 = ImageFont.truetype('PopArt-Regular.ttf', fontsize())
font3 = ImageFont.truetype('All Things Must Pass.ttf', fontsize())
font4 = ImageFont.truetype('docktrin.ttf', fontsize())
font5 = ImageFont.truetype('Break.ttf', fontsize())
font6 = ImageFont.truetype('Neo-Writer.ttf', fontsize())
font7 = ImageFont.truetype('LEIXO-DEMO.ttf', fontsize())
font8 = ImageFont.truetype('Manta Style Sans DEMO.ttf', fontsize())
font9 = ImageFont.truetype('Smoke-Rasterized.ttf', fontsize())
fontlist=[font1,font2,font3,font4,font5,font6, font7, font8, font9]

nouns=[]
adpos=[]
gerunds=[]

for token in doc:
    if token.pos_=="NOUN":
        nouns.append(token.text)
    elif token.tag_=="VBG":
        gerunds.append(token.text)
    elif token.pos_=="ADP":
        adpos.append(token.text)    
print("Adpo = "+adpos[10])
        
print("Noun 400 = " +nouns[400])
for token in doc2:
    if token.pos_=="NOUN":
        nouns.append(token.text)
    elif token.tag_=="VBG":
        gerunds.append(token.text)
    elif token.pos_=="ADP":
        adpos.append(token.text)    
print("Noun 1200 = "+nouns[1200])
for token in doc3:
    if token.pos_=="NOUN":
        nouns.append(token.text)
    elif token.tag_=="VBG":
        gerunds.append(token.text)
    elif token.pos_=="ADP":
        adpos.append(token.text)    
print("Noun 4000 = "+nouns[4000])

def getnoun():
    word=random.choice(nouns)
    return word
def gerund():
    word2=random.choice(gerunds)
    return word2
def adpo():
    word3=random.choice(adpos)
    return word3

x=0
y=1
while x<100:
    try:
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        textcolors=["black", "white"]

        im=Image.new(mode="RGB", size=(400,400), color=(r,g,b))
        d1 = ImageDraw.Draw(im)
        d2 = ImageDraw.Draw(im)
        d3 = ImageDraw.Draw(im)
        d1text=gerund()
        print("this is d1text = "+d1text)
        d3text=getnoun()
        d2text=adpo()
        print(d2text)
        usefont=random.choice(fontlist)
        usefont2=random.choice(fontlist)
        print(usefont)
        width = int(d1.textlength(d1text, usefont))
        print(width)
        width2 = int(d2.textlength(d2text, usefont2))
        width3 = int(d3.textlength(d3text, usefont))
        print(width2)
        height =40
        xbound=int(400-width-15)
        print(xbound)
        ybound=200-height-15
        xbound2=int(400-width2-15)
        ybound3=400-15
        xbound3=int(400-width3-15)
        print(xbound2)
        ybound2=300-(height*2)
        randx1=random.randint(15, xbound)
        print(randx1)
        randy1=random.randint(15, ybound)
        randx2=random.randint(15, xbound2)
        randy2=random.randint(ybound, ybound2)
        randx3=random.randint(15, xbound3)
        randy3=random.randint(ybound2, ybound3)
        d1.text((randx1, randy1), d1text, font=usefont, fill=(random.choice(textcolors)))
        d2.text((randx2, randy2), d2text, font=usefont2, fill=(random.choice(textcolors)))
        d3.text((randx3, randy3), d3text, font=usefont, fill=(random.choice(textcolors)))
        print(width)
        im.show()
        x=x+1
        im.save("./TestCards/Card{}.jpg".format(x))
    except:
        print("Error {}, trying again".format(y))

