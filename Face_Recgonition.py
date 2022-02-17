import cv2
import numpy as np;
import face_recognition;
import os;

print("hello")
path='Images'
images=[]
classNames=[]
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    #cv2.imshow("Rao Burhan" , cl)


print(classNames)


def findEncodings(images):

  encodeList=[]
  for img in images:
    img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    #encodeList[i for i if i not in classNames]
    encodeList.append(encode)
  return encodeList

encodeListKnown = findEncodings(images)
print(len(encodeListKnown))

cap=cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    height,width = img.shape[:2] 
   # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgS=cv2.resize(img,(0,0) , None ,0.25,0.25)
    imgS = cv2.cvtColor(imgS , cv2.COLOR_BGR2RGB)
    faces_cur_frame= face_recognition.face_locations(imgS)
    encodes_cur_frame= face_recognition.face_encodings(imgS,faces_cur_frame)
    cv2.rectangle(img, (0,height-50) , (200,height) , (0,0,0) , thickness=cv2.FILLED )

    for encodeFace, faceLoc in zip(encodes_cur_frame,faces_cur_frame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        facedist2= min(faceDistance)
        print("FACE DISTANCE",facedist2)
        if(facedist2>=0.5):
          y1,x2,y2,x1 = faceLoc
          y1,x2,y2,x1 =  y1*4,x2*4,y2*4,x1*4
          cv2.rectangle(img , (x1,y1) , (x2,y2), (0,255,0) , 2 )
          cv2.rectangle(img , (x1,y2-35) , (x2,y2), (0,255,0) , cv2.FILLED )
          cv2.putText(img ,"UNKNOWN",(x1+6 , y2-6),  cv2.FONT_HERSHEY_COMPLEX , 1 ,(255,255,255), 2 )
        print(faceDistance)
        matchIndex= np.argmin(faceDistance)
        name = classNames[matchIndex].upper()
        y1,x2,y2,x1 = faceLoc
        y1,x2,y2,x1 =  y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img , (x1,y1) , (x2,y2), (0,255,0) , 2 )
        cv2.rectangle(img , (x1,y2-35) , (x2,y2), (0,255,0) , cv2.FILLED )
        cv2.putText(img ,name,(x1+6 , y2-6),  cv2.FONT_HERSHEY_COMPLEX , 1 ,(255,255,255), 2 )
        print(name)
    cv2.imshow("Webcam" , img)
    cv2.waitKey(1)