import urllib.request
import urllib.error
import time
import socket
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
        # s = time.time()
        resp = urllib.request.urlopen(req, timeout=5)
        # e = time.time()
        # print("requst time: " + str(e - s))
        qrcont = resp.read()
        json_data = json.loads(qrcont.decode('utf-8'))
        # print(qrcont.decode('utf-8'))
        if len(json_data['faces']) == 0:
            return "No face"
        return json_data['faces'][0]['face_token']
    except urllib.error.HTTPError as e:
        print(e.read().decode('utf-8'))
    except urllib.error.URLError:
        print("URL error")
    except socket.timeout:
        print("-------------!!!------------")

    #return face_token

def post_search(face_token):
    http_url = 'https://api-us.faceplusplus.com/facepp/v3/search'
    key = "T7080cfMH824XsoWzR0v4QPc288iTWBu"
    secret = "iWLN8jiciOCMWidOKfzIufBW11I4fjl0"

    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'face_token')
    data.append(face_token)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
    data.append("workingSet")
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
        # s = time.time()
        resp = urllib.request.urlopen(req, timeout=5)
        # e = time.time()
        # print("requst time: " + str(e - s))
        qrcont = resp.read()
        json_data = json.loads(qrcont.decode('utf-8'))
        print(qrcont.decode('utf-8'))
        user_id = json_data["results"][0]["user_id"]
        confidence = json_data["results"][0]["confidence"]
        if confidence > 60:
            return user_id
        else:
            return "cannot recognition"
    except urllib.error.HTTPError as e:
        print(e.read().decode('utf-8'))
    except urllib.error.URLError:
        print("URL error")
    except socket.timeout:
        print("-------------!!!------------")

#
# if __name__ == 'main':
#
#
#     s = time.time()
#
#     face_token = get_face_token('/Users/wangtianduo/Desktop/Python3/face_recoginition/dataset/User1.jpg')
#     print(post_search(face_token))
#     e = time.time()
#
#     print(e-s)