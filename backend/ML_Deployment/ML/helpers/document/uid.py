import re
import numpy as np
import pytesseract as ocr
from PIL import Image
import cv2

from .verhoeff import compute_checksum

def Regex_Search(bounding_boxes):

  possible_UIDs = []
  Result = ""

  for character in range(len(bounding_boxes)):
    if len(bounding_boxes[character])!=0:
      Result += bounding_boxes[character][0]
    else:
      Result += '?'

  matches = [match.span() for match in re.finditer(r'\d{12}',Result,overlapped=True)]

  for match in matches :

    UID = int(Result[match[0]:match[1]])
    
    if compute_checksum(UID)==0 and UID%10000!=1947:
       possible_UIDs.append([UID,match[0]])

  possible_UIDs = np.array(possible_UIDs)
  return possible_UIDs



# Mask found UIDs using OpenCV

def Mask_UIDs (image_path,possible_UIDs,bounding_boxes,rtype,SR=False,SR_Ratio=[1,1]):

  img = cv2.imread(image_path)

  if rtype==2:
    img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
  elif rtype==3:
    img = cv2.rotate(img,cv2.ROTATE_180)
  elif rtype==4:
    img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

  height = img.shape[0]

  if SR==True:
    height*=SR_Ratio[1]

  ########################### MASK EVERY DIGIT INDIVIDUALLY ############################

  # for UID in possible_UIDs:

  #   for i in range(8):

  #     digit = bounding_boxes[UID[1]+i].split()

  #     if SR==False:
  #       top_left_corner = (int(digit[1]),height-int(digit[4]))
  #       bottom_right_corner = (int(digit[3]),height-int(digit[2]))

  #     else:
  #       top_left_corner = (int(int(digit[1])/SR_Ratio[0]),int((height-int(digit[4]))/SR_Ratio[1]))
  #       bottom_right_corner = (int(int(digit[3])/SR_Ratio[0]),int((height-int(digit[2]))/SR_Ratio[1]))

  #     img = cv2.rectangle(img,top_left_corner,bottom_right_corner,(0,0,0),-1)

  ######################################################################################

  for UID in possible_UIDs:

    digit1 = bounding_boxes[UID[1]].split()
    digit8 = bounding_boxes[UID[1] + 7].split()

    h1 = min(height-int(digit1[4]),height-int(digit8[4]))
    h2 = max(height-int(digit1[2]),height-int(digit8[2]))

    if SR==False:
      top_left_corner = (int(digit1[1]),h1)
      bottom_right_corner = (int(digit8[3]),h2)

    else:
      top_left_corner = (int(int(digit1[1])/SR_Ratio[0]),int((h1)/SR_Ratio[1]))
      bottom_right_corner = (int(int(digit8[3])/SR_Ratio[0]),int((h2)/SR_Ratio[1]))

    img = cv2.rectangle(img,top_left_corner,bottom_right_corner,(0,0,0),-1)

  if rtype==2:
    img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
  elif rtype==3:
    img = cv2.rotate(img,cv2.ROTATE_180)
  elif rtype==4:
    img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

  file_name = image_path.split('/')[-1].split('.')[0]+"_masked"+"."+image_path.split('.')[-1]
  cv2.imwrite(file_name,img)
  return file_name

def Extract_and_Mask_UIDs (image_path,SR=False,sr_image_path=None,SR_Ratio=[1,1]):

  if SR==False:
    img = cv2.imread(image_path)
  else:
    img = cv2.imread(sr_image_path)

  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  rotations = [[gray,1],
               [cv2.rotate(gray,cv2.ROTATE_90_COUNTERCLOCKWISE),2],
               [cv2.rotate(gray,cv2.ROTATE_180),3],
               [cv2.rotate(gray,cv2.ROTATE_90_CLOCKWISE),4],
               [cv2.GaussianBlur(gray,(5,5),0),1],
               [cv2.GaussianBlur(cv2.rotate(gray,cv2.ROTATE_90_COUNTERCLOCKWISE),(5,5),0),2],
               [cv2.GaussianBlur(cv2.rotate(gray,cv2.ROTATE_180),(5,5),0),3],
               [cv2.GaussianBlur(cv2.rotate(gray,cv2.ROTATE_90_CLOCKWISE),(5,5),0),4]]

  settings = ('-l eng --oem 3 --psm 11')

  for rotation in rotations :
    
    cv2.imwrite(image_path + 'rotated_grayscale.png',rotation[0])
    bounding_boxes = ocr.image_to_boxes(Image.open('rotated_grayscale.png'),config=settings).split(" 0\n")

    possible_UIDs = Regex_Search(bounding_boxes)

    if len(possible_UIDs)==0:
      continue
    else:

      if SR==False:
        masked_img = Mask_UIDs (image_path,possible_UIDs,bounding_boxes,rotation[1])
      else:
        masked_img = Mask_UIDs (image_path,possible_UIDs,bounding_boxes,rotation[1],True,SR_Ratio)

      return (masked_img,possible_UIDs)

  return (None,None)