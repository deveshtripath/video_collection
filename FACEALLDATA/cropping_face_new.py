
import cv2
from mtcnn.mtcnn import MTCNN
import os



#!pip install mtcnn

dire=r"E:\Actor\Meiyang Chang" # folder which has the frames or data

dire1=r"E:\Meiyang Chang\google" # folder where faces will be cropped and stored
os.makedirs(dire1, exist_ok = True)

detector = MTCNN()

def face_detect(path,save):
    image = cv2.imread(path,1)
    result=detector.detect_faces(image)
    if not result:
        print("Their is no any face: ",path)
    if result:
        b=result[0]['box']
        img1=image[b[1]-70:b[1]+b[3]+70,b[0]-70:b[0]+b[2]+70]
        face = cv2.resize(img1, (300, 300))
        cv2.imwrite(save,face)
        return(img)
        
for img in os.listdir(dire):
    try:
        path=dire+'/'+img
        save=dire1+"/"+img
        img2=face_detect(path,save)
    except Exception as e:
        print(e)
print("All is done.")

