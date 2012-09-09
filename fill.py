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
import ledstrip, time

led = ledstrip.strand()

led.fill(0,0,0)

print ""
print "Fill the strip and empty it.."
print "Press control+C to exit"
print ""

while True:
	time.sleep(0.5)

	print "Filling it up..."
	for x in xrange(0,32):
		led.set(x,28, 69, 135)
		time.sleep(0.05)

	print "Empty it..."
	for x in xrange(1,33): # <-- one extra led, to get to 0
		led.set((32-x),0,0,0)
		time.sleep(0.05)

	print "Filling it up..."
	for x in xrange(0,32):
		led.set(x,158, 0, 0)
		time.sleep(0.05)

	print "Empty it (from the beginning)..."
	for x in xrange(0,32):
		led.set(x,0, 0, 0)
		time.sleep(0.05)

	print "Filling it up..."
	for x in xrange(0,32):
		led.set(x,196, 162, 57)
		time.sleep(0.05)

	print "Overwrite fill with another color..."
	for x in xrange(0,32):
		led.set(x,147, 196, 125)
		time.sleep(0.05)