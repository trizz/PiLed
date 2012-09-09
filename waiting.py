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
import ledstrip, time, collections

led = ledstrip.strand()

print ""
print "\"Chase\" a color through the strip with fade-out (looped)"
print "Press control+C to exit"
print ""

led.fill(0,0,0)

colorList = [[0,0,250],[0,0,225],[0,0,200],[0,0,175],[0,0,150],[0,0,125],[0,0,100],[0,0,75],[0,0,50],[0,0,25],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

p = collections.deque(xrange(len(colorList)))

method = "wheel"

if method == "wheel":
	while True:
		for x in xrange(0,32):		
			p.rotate(1)
			led.set(x,colorList[p[0]][0],colorList[p[0]][1],colorList[p[0]][2])
		p.rotate((len(p)-1))