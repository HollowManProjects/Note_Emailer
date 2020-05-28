import sys

# Takes in txt file and makes new outputfile
fileToConvert = sys.argv[1]
newOutputFile = fileToConvert[:-4] + ".html"

# Open/create new html file
with open("./"+newOutputFile, "w") as htmlFile:
    htmlFile.write("<p>\n")

    # Grab data from txt file to convert
    with open("./"+fileToConvert, "r") as txtFile:
        data = txtFile.read().splitlines()

    # Makes poem's title as the header
    htmlFile.write("<h1>" + data[0].strip() + "</h1>\n")

    # Adds poem's body
    for line in data[1:]:
        htmlFile.write(line)

    # End note's section
    htmlFile.write("</p>")

    # Add post disclaimer
    htmlFile.write('\n<br><p><i>These notes are made by James Plank. I am attempting to own or say I made any of these notes. These are just condensed versions of his notes that I have created. Again this is not my work, but that of professor James Plank. To see his full notes and teachings click <a href="http://web.eecs.utk.edu/~jplank/plank/classes/teaching.html" target="_blank">here</a></p>')
