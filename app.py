#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response

# import camera driver
# if os.environ.get('CAMERA'):
#     Camera = import_module('camera_' + os.environ['CAMERA']).Camera
# else:
#     from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

from camera_lib.camera_opencv import Camera
#import camera_lib

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def update_status(camera):
    while True:
        status = camera.get_status()
        if status == 0:
            fr = open('/Users/wangtianduo/Desktop/Python3/face_recoginition/static/1.jpg', 'rb')
            output = b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + fr.read() + b'\r\n'
            fr.close()
        else:
            fr = open('/Users/wangtianduo/Desktop/Python3/face_recoginition/static/2.jpg', 'rb')
            output = b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + fr.read() + b'\r\n'
            fr.close()
        # yield (b'--frame\r\n'
        #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        yield (output)


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/update_status')
def update():
    return Response(update_status(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
