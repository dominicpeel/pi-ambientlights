from picamera import mmal, mmalobj as mo
from time import sleep
import numpy as np
import pigpio

pi = pigpio.pi()
R, G, B = 17, 22, 24 # GPIO pins

def setLights(r,g,b):
	pi.set_PWM_dutycycle(R, int(r))
	pi.set_PWM_dutycycle(G, int(g))
	pi.set_PWM_dutycycle(B, int(b))

def calibrate(r,g,b):
	rm, gm, bm = 2, 1, .4
	r = max(min(r*rm, 255), 0)
	g = max(min(g*gm, 255), 0)
	b = max(min(b*bm, 255), 0)
	return r,g,b

def image_callback(port, buf):
	image_data = np.frombuffer(buf.data, dtype=np.uint8)
	image = image_data.reshape((160, 320, 3))
	r,g,b = np.mean(image, axis=(0,1))
	r,g,b = calibrate(r,g,b)
	setLights(r,g,b)
	return False

camera = mo.MMALCamera()
preview = mo.MMALRenderer()

camera.outputs[0].framesize = (320, 160)
camera.outputs[0].framerate = 30
camera.outputs[0].format = mmal.MMAL_ENCODING_RGB24
camera.outputs[0].commit()

camera.outputs[0].enable(image_callback)

sleep(1e9)
camera.outputs[0].disable()
