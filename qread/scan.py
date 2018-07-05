# USAGE
# python barcode_scanner_video.py

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import pygame
import os
import os.path as op

def scan(_props):
    pygame.init()
    beepfile = op.join(op.dirname(op.dirname(__file__)), 'sound', 'beep.mp3')
    pygame.mixer.music.load(beepfile)
    fw, fh = _props['width'], _props['height']
    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    # vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True,resolution=(fw, fh)).start()
    time.sleep(2.0)

    csv = open(_props["output"], "w")
    detect = False

    while True:
        frame = vs.read()
        barcodes = pyzbar.decode(frame)
        if not detect:
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8").encode('ascii','ignore')
                barcodeType = barcode.type
                print(barcodeData, barcodeType)
                pygame.mixer.music.play(0)
                detect = True
                detect_time = time.time()
                text = "{}".format(barcodeData)
                cv2.putText(frame, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 1)
                csv.write("{},{}\n".format(datetime.datetime.now(), barcodeData))
                csv.flush()
        else:
            if time.time()-detect_time > _props['timeout']:
                detect = False

        # show the output frame
        cv2.imshow("QRead", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # close the output CSV file do a bit of cleanup
    print("[INFO] cleaning up...")
    csv.close()
    cv2.destroyAllWindows()
    vs.stop()
