import cv2
from .base_camera import BaseCamera
from .general_face_detect import check_has_face, get_id


class Camera(BaseCamera):

    status = 0
    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')
        
        while True:
            # read current frame
            _, img = camera.read()
            
            face_list = check_has_face(img)
            if len(face_list) != 0:
                Camera.status = 1 # status=1 means it is detecting
            else:
                Camera.status = 0
            #id_list = get_id(face_list)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()

    @staticmethod
    def get_status():
        return Camera.status
