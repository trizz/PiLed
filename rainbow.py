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
print "Scroll rainbowcolors (with fade and looped)"
print "Press control+C to exit"
print ""

led.fill(0,0,0)

rainbow = [[126 , 1 , 0],[114 , 13 , 0],[102 , 25 , 0],[90 , 37 , 0],[78 , 49 , 0],[66 , 61 , 0],[54 , 73 , 0],[42 , 85 , 0],[30 , 97 , 0],[18 , 109 , 0],[6 , 121 , 0],[0 , 122 , 5],[0 , 110 , 17],[0 , 98 , 29],[0 , 86 , 41],[0 , 74 , 53],[0 , 62 , 65],[0 , 50 , 77],[0 , 38 , 89],[0 , 26 , 101],[0 , 14 , 113],[0 , 2 , 125],[9 , 0 , 118],[21 , 0 , 106],[33 , 0 , 94],[45 , 0 , 82],[57 , 0 , 70],[69 , 0 , 58],[81 , 0 , 46],[93 , 0 , 34],[105 , 0 , 22],[117 , 0 , 10]]

p = collections.deque(xrange(len(rainbow)))

while True:
	for x in xrange(0,32):		
		p.rotate(1)
		led.set(x,rainbow[p[0]][0],rainbow[p[0]][1],rainbow[p[0]][2])
	p.rotate((len(p)-1))