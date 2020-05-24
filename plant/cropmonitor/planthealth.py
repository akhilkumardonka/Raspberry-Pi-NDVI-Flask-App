# import the necessary packages
import numpy as np
import imutils
import cv2


class ComputeNdvi:
	def contrast_stretch(self, im):
		"""
		Performs a simple contrast stretch of the given image, from 5-95%.
		"""
		in_min = np.percentile(im, 5)
		in_max = np.percentile(im, 95)

		out_min = 0.0
		out_max = 255.0

		out = im - in_min
		out *= ((out_min - out_max) / (in_min - in_max))
		out += in_min

		return out
	
	def compute(self, frame):
		b, g, r = cv2.split(frame)
		bottom = (r.astype(float) + b.astype(float))
		bottom[bottom == 0] = 0.01  # Make sure we don't divide by zero!
		ndvi = (r.astype(float) - b) / bottom
		ndvi = self.contrast_stretch(ndvi)
		ndvi = ndvi.astype(np.uint8)
		frame = cv2.applyColorMap(ndvi, cv2.COLORMAP_JET);
		
		return frame
