import sys

filereader = open("simple.txt", 'r')

for row in filereader:
    print(row.strip())

filereader.close()
