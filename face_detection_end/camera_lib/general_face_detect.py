import cv2
import os
from .post_search import post_search, get_face_token

# cam = cv2.VideoCapture(0)
# cam.set(3, 640) # set video width
# cam.set(4, 480) # set video height
#
# face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# count = 0
#
# # post_search.get_face_token("/Users/wangtianduo/Desktop/Python3/face_recoginition/dataset/User1.jpg")
#
# while(True):
#
#     ret, img = cam.read()
#
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(gray, 1.3, 5)
#     cv2.imwrite("ss" + str(count) + ".jpg", gray)
#
#     for (x,y,w,h) in faces:
#
#         cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
#         cv2.imwrite("ss" + str(count) + ".jpg", img)
#         count += 1
#         # Save the captured image into the datasets folder
#         file_name = "dataset/User" + str(count) + ".jpg"
#
#         cv2.imwrite(file_name, gray[y:y+h,x:x+w])
#         face_token = post_search.get_face_token(file_name)
#         user_id = post_search.post_search(face_token)
#         print(user_id)
#         # cv2.imshow('image', img)
#
#     k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
#     if k == 27:
#         break
#     elif count >= 5: # Take 30 face sample and stop video
#          break
#
#
# cam.release()
# # cv2.destroyAllWindows()
#
# post_search.get_face_token("/Users/wangtianduo/Desktop/Python3/face_recoginition/dataset/User1.jpg")

#
# def transform_pic_to_id(cvimg):
#
#     face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
#     gray = cv2.cvtColor(cvimg, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(gray, 1.3, 5)
#
#     output = []
#     if len(faces) == 0:
#         return output
#
#     for (x,y,w,h) in faces:
#
#         cv2.rectangle(cvimg, (x,y), (x+w,y+h), (255,0,0), 2)
#         file_name = "dataset/User" + ".jpg"
#         cv2.imwrite(file_name, gray[y:y + h, x:x + w])
#         face_token = post_search.get_face_token(file_name)
#         user_id = post_search.post_search(face_token)
#         output.append(user_id)
#         print(user_id)
#     return output

# if no faces, return empty list
# if detect faces, return list with faces in cvimg format
def check_has_face(cvimg):
    gray = cv2.cvtColor(cvimg, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier('camera_lib/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    output = []
    if len(faces) == 0:
        return output
    else:
        for (x, y, w, h) in faces:
            cut_face = gray[y:y + h, x:x + w]
            output.append(cut_face)
        return output

def get_id(face_list):
    output = []
    for face in face_list:
        file_name = "dataset/User" + ".jpg"
        cv2.imwrite(file_name, face)
        face_token = get_face_token(file_name)
        if face_token != "No face":
            user_id = post_search(face_token)
            output.append(user_id)
    return output