import cv2
import numpy as np;
import face_recognition;
import os;


def findEncodings(images):

  encodeList=[]
  for img in images:
    img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    #encodeList[i for i if i not in classNames]
    encodeList.append(encode)
  return encodeList

def predictFace(recievedImage):
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
  encodeListKnown = findEncodings(images)
  print(len(encodeListKnown))
  # load input image and grab its spatial dimensions
  nparr = np.fromstring(raw_image.data, np.uint8)
  # decode image
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  # img =recievedImage
  # image = cv2.imread(recievedImage)
  # img = np.array(image)
  # np.array(img)
  # # print(img)
  #  imgs= cv2.resize(img , (0,0) , None , 0.25,0.25)

  img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  # cv2_imshow(img)

  faces_curr_frame = face_recognition.face_locations(img)
  print("faces",faces_curr_frame)
  encode_curr_frame = face_recognition.face_encodings(img , faces_curr_frame)

  for encodeface , faceloc in zip(encode_curr_frame , faces_curr_frame ):
    match = face_recognition.compare_faces(encodeListKnown , encodeface)
    facedist= face_recognition.face_distance(encodeListKnown , encodeface)
    print("Face distance",facedist)
        # if(facedist <0.6):
        # {
        #       cv2.putText(img ,"Unknown",(x1+6 , y2-6),  cv2.FONT_HERSHEY_COMPLEX , 1 ,(255,255,255), 2 )
        # }
    facedist2= min(facedist)
    print("FACE DISTANCE",facedist2)
    if(facedist2>=0.5):
      y1,x2,y2,x1 = faceloc
      y1,x2,y2,x1 =  y1*4,x2*4,y2*4,x1*4

      cv2.rectangle(img , (x1,y1) , (x2,y2), (0,255,0) , 2 )
      cv2.rectangle(img , (x1,y2-35) , (x2,y2), (0,255,0) , cv2.FILLED )
      cv2.putText(img ,"UNKNOWN",(x1+6 , y2-6),  cv2.FONT_HERSHEY_COMPLEX , 1 ,(255,255,255), 2 )
      print("Unknown" )
      return "Unknown"
      # cv2_imshow(img )
      # cv2.waitKey(1)
    else:
      matchIndex = np.argmin(facedist)

    if(match[matchIndex]):
      name = classNames[matchIndex].upper()
      print("Name",name)
      return name
      # y1,x2,y2,x1 = faceloc
      # y1,x2,y2,x1 =  y1*4,x2*4,y2*4,x1*4
      # cv2.rectangle(img , (x1,y1) , (x2,y2), (0,255,0) , 2 )
      # cv2.rectangle(img , (x1,y2-35) , (x2,y2), (0,255,0) , cv2.FILLED )
      # cv2.putText(img ,name,(x1+6 , y2-6),  cv2.FONT_HERSHEY_COMPLEX , 1 ,(255,255,255), 2 )
      # cv2_imshow(img )
      # cv2.waitKey(1)