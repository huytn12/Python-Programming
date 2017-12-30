#!/bin/python
import os

xmen_file = open('xmen.txt', 'r+')

xmen_file.seek(-1, os.SEEK_END)
xmen_file.write("\nBeast\n")
xmen_file.write("Phoenix\n")

xmen_file.close()
