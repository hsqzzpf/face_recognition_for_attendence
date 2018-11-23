import urllib.request
import urllib.error
import time
import socket
import requests
import json

def get_face_token(file_path):
    http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    key = "T7080cfMH824XsoWzR0v4QPc288iTWBu"
    secret = "iWLN8jiciOCMWidOKfzIufBW11I4fjl0"
    filepath = file_path

    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr = open(filepath, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data.append('0')
    data.append('--%s--\r\n' % boundary)

    for i, d in enumerate(data):
        if isinstance(d, str):
            data[i] = d.encode('utf-8')

    http_body = b'\r\n'.join(data)

    # build http request

    req = urllib.request.Request(url=http_url, data=http_body)

    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    try:
        # post data to server
        s = time.time()
        resp = urllib.request.urlopen(req, timeout=5)
        e = time.time()
        print("requst time: " + str(e - s))
        # get response
        qrcont = resp.read()
        json_data = json.loads(qrcont.decode('utf-8'))
        # if you want to load as json, you should decode first,
        # for example: json.loads(qrount.decode('utf-8'))
        print(qrcont.decode('utf-8'))
        return json_data['faces'][0]['face_token']
    except urllib.error.HTTPError as e:
        print(e.read().decode('utf-8'))
    except urllib.error.URLError:
        print("URL error")
    except socket.timeout:
        print("-------------!!!------------")

    #return face_token

def post_search(face_token):
    user_id = ""


    return user_id

# get_face_token("/Users/wangtianduo/Desktop/Python3/face_recoginition/dataset/workingSet/whitebbird.jpg")


s = time.time()

get_face_token('/Users/wangtianduo/Desktop/Python3/face_recoginition/dataset/User1.jpg')
e = time.time()

print(e-s)