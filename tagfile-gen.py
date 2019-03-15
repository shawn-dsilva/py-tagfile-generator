import os
directory = '_posts/'

tagslist = []
finaltags = []

for file in os.listdir(directory):
    print (file)
    f = open('_posts/' + file)
    lines = f.read().splitlines()
    for index, line in zip(range(4), lines):
        if index == 3:
            print (line)
            line = line.split(':')
            line = line[1].split(' [')
            line = line[1].split(']')
            line = line[0].split(', ')
            tagslist.append(line)

for tags in tagslist:
    for tag in tags:
        if tag not in finaltags:
            finaltags.append(tag)


for final in finaltags:
    print( final )