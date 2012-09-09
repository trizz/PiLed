"""
Copyright (c) 2012 trizz

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 """
from random import randint
from multiprocessing import Pool
import ledstrip, time
import os
import sys

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

led = ledstrip.strand()

led.fill(0,0,0)

colorList = []

cls()
print "Fade Menu - choose color scheme"
print "-----------------"
print "1. Taste the Rainbow"
print "2. Fire"
print "3. Carribean Waters"
print "4. There's my Candy"
print "5. Patterns in Nature"
print "-----------------"

print "\n\nColor scheme:",
colorScheme = raw_input()

cls()
print "Fade Menu - choose mode"
print "-----------------"
print "1. In line"
print "2. Random"
print "3. Random per led"
print "-----------------"

print "\n\nMode:",
colorMode = raw_input()

cls()
print "Fade Menu - choose speed"
print "-----------------"
print "1. Fast"
print "2. Normal"
print "3. Slow"
print "4. Very slow"
print "-----------------"

print "\n\nMode:",
colorSpeed = raw_input()

cls()

if colorScheme == '1':
	# Rainbow - http://kuler.adobe.com/#themeID/937475
	print "Colorscheme:\tTaste the Rainbow"
	colorList = [[255,0,18],[255,125,0],[255,217,0],[91,227,0],[0,132,176]]

if colorScheme == '2':
	# Fire - http://kuler.adobe.com/#themeID/1051644
	print "Colorscheme:\tFire"
	colorList = [[105,12,7],[186,68,16],[229,130,34],[247,194,69],[255,240,128]]

if colorScheme == '3':
	# Water - http://kuler.adobe.com/#themeID/159292
	print "Colorscheme:\tCarribean Waters"
	colorList = [[70,120,232],[17,186,217],[43,75,250],[0,158,255],[77,221,255]]

if colorScheme == '4':
	# Candy - http://kuler.adobe.com/#themeID/2032630
	print "Colorscheme:\tThere's my Candy"
	colorList = [[254,162,53],[255,210,78],[51,172,147],[48,151,112],[204,74,108]]

if colorScheme == '5':
	# Nature - http://kuler.adobe.com/#themeID/2051653
	print "Colorscheme:\tPatterns in Nature"
	colorList = [[2,100,1],[70,115,2],[114,166,3],[171,217,4],[234,242,5]]

if colorMode == '1': print "Colormode:\tIn line"
if colorMode == '2': print "Colormode:\tRandom"
if colorMode == '3': print "Colormode:\tRandom per led"

if colorSpeed == '1': print "Speed:\t\tFast"
if colorSpeed == '2': print "Speed:\t\tNormal"
if colorSpeed == '3': print "Speed:\t\tSlow"
if colorSpeed == '4': print "Speed:\t\tVery slow"

print ""
print "Press control+C to exit"

prevID = 0
iRGB = 0

while True:
	r1 = colorList[prevID][0]
	g1 = colorList[prevID][1]
	b1 = colorList[prevID][2]

	if colorMode == '1':
		if prevID == 4:
			iRGB = 0
		else:
			iRGB = prevID + 1
	else: iRGB = randint(0,4)

	# Prevent the same color
	while iRGB == prevID: iRGB = randint(0,4)
	
	prevID = iRGB

	r2 = colorList[iRGB][0]
	g2 = colorList[iRGB][1]
	b2 = colorList[iRGB][2]	

	for i in xrange(1,255):	
		r = (i * r2 + (255 - i) * r1) / 255;
		g = (i * g2 + (255 - i) * g1) / 255;
		b = (i * b2 + (255 - i) * b1) / 255;

		if colorMode == '3':
			l = randint(0,31)
			led.set(l,r,g,b)
		else:
			led.fill(r,g,b)
		
		if colorSpeed == '1': time.sleep(0)
		if colorSpeed == '2': time.sleep(0.01)
		if colorSpeed == '3': time.sleep(0.1)
		if colorSpeed == '4': time.sleep(0.5)