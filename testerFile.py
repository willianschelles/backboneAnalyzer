import os
import re

fileNames = ["www.pop-es.rnp.br"]

with open("./pops/" + fileNames[0] + ".txt") as x:
    for line in x:
        print line.rstrip()

        dateRegex = "[0-9]{2}:[0-9]{2}:[0-9]{2}"
        DateMatch = re.search(dateRegex, line, 0)
        # print dateRegex
        if DateMatch:
            print "IM THE"
            print line
            print DateMatch.group(0)