import os
import glob

path = './'
listing = os.listdir(path)

name = raw_input("Enter a name:")
filename = name + '.xhtml'

FILE = open(filename,'w')
FILE.write('<?xml version="1.0" encoding="utf-8" standalone="no"?>')
FILE.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">')
FILE.write('<html xmlns="http://www.w3.org/1999/xhtml">')
FILE.write('<head>')
FILE.write('<title>' + name + '</title>')
FILE.write('<style type="text/css">')
FILE.write('body {background: #000; color: #fff;text-align: center;}')
FILE.write('img {margin: 0 auto; text-align: center;}')
FILE.write(' p.sgc-1 {text-align: center;}')
FILE.write('</style>')
FILE.write('</head>')
FILE.write('<body>')
FILE.write('<h1 id="heading_id_2">' + name + '</h1>')
for infile in listing:
   if infile[-3:].lower() == 'jpg':
	FILE.write( '<p>&nbsp;<img src="../Images/' +  infile + '"/></p>')

FILE.write('</body>')
FILE.write('</html>')

FILE.close()
