# PiLed
This repo contains my personal tests and examples to control a digital RGB led strip with the Raspberry Pi.
Probably this code will work with another controllers/strips too, but I haven't tested that.

The strip I've used is from Adafruit (http://adafruit.com/products/306) and it is controlled with a Raspberry Pi (http://www.raspberrypi.org). The strip is connected to the Pi according to this article: http://learn.adafruit.com/light-painting-with-raspberry-pi/hardware. For the communication between the Pi and the strip, I've used the library provided by Sh4d (https://github.com/Sh4d/LPD8806) and modified it a bit.

If you want to use the Python scripts provided, please make sure you check the settings: my strip is just one meter, so it has 32 leds and this is hardcoded in most of the scripts (if not all). Also I've changed my output in `ledstrip.py` to `/dev/spidev0.1` instead of `/dev/spidev0.0`. Don't exactly know why, but 0 doesn't work and 1 does.

The `run` script is added because I'm lazy. Just give it exec permissions and you can run the examples just by typing `./run fade`.

### Please note!
This are just samples to make myself familier with Python and controlling the RGB strip. The scripts aren't free of bugs and aren't a complete product (more a proof of concept). I've published these so others can have a quick start, because, apart from the light-painting article mentioned earlier, I cound't find any good examples. Please feel free to do with it whatever you want. 

### License
The scripts are licensed under the MIT-license.