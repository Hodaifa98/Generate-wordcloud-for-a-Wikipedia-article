# -*- coding: utf-8 -*-

import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

#Request the user to input the topic for the wordcloud
topic = input("Enter a topic to generate a wordcloud for: ")
color = input("Enter the color of background: ")
num = int(input("Enter the number of words in the wordcloud: "))

#Firt entry when we search for the topic in wikipedia
title = wikipedia.search(topic)[0]
#Get the page fo the title
page = wikipedia.page(title)
#Text content from the page
text = page.content

#Get the background for the wordcloud
try:
    background = np.array(Image.open("background.png"))
except:
    background = None

#Remove stopwords
stopwords = set(STOPWORDS)

#Generate the wordcloud
wc = WordCloud(background_color=color, mask=background, stopwords=stopwords, max_words=num)
wc.generate(text)
fileName = f"{title} - WordCloud.png"
wc.to_file(fileName)
print("\nWordcloud generated. The name of the file is: \"" + fileName + "\"")