import face_recognition
import cv2


def recon():
    img = face_recognition.load_image_file("C:/Users/blasc/OneDrive/Imágenes/Saved Pictures/fotos/FotoDNI.jpg")
    encoding_img = face_recognition.face_encodings(img)[0]

    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('opencv_foto.png', image)
    del camera

    nxt_img = face_recognition.load_image_file("opencv_foto.png")
    try:
        encoding_nxt_img = face_recognition.face_encodings(nxt_img)[0]

        result = face_recognition.compare_faces([encoding_img], encoding_nxt_img)
    except IndexError:
        print("No se reconoce ninguna cara en la imagen")
        result = None

    return result[0]
