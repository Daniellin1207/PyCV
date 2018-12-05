"""
@author:Daniel
@file: readVideo.py
@time: 2018/12/05
"""

import cv2
import datetime
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(paper, (x, y), 10, (255, 0, 0),-1)


cap = cv2.VideoCapture(0)
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 20 # cap.get(cv2.CAP_PROP_FOURCC)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

vout = cv2.VideoWriter()
vout.open('output.mp4',fourcc,fps,sz,True)

paper=np.zeros((int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 3), np.uint8)
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', draw_circle)


while True:
    ret, frame = cap.read()
    # Our operations on the frame come here
    temp = cv2.cvtColor(paper, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    # temp=cv2.threshold(temp,100,255,cv2.THRESH_BINARY_INV)
    # frame=cv2.bitwise_and(frame,temp)
    # frame=np.multiply(frame,temp)
    # dst=cv2.add(frame,paper)
    dst = cv2.addWeighted(frame, 0.5, paper, 0.5, 0)
    # k=frame*cv2.threshold(paper,50,(1,1,1),cv2.THRESH_BINARY_INV)

    cv2.putText(dst, "Maker: {}".format("Daniel"), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(dst, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    k=cv2.waitKey(20)
    if k==ord(' '):
        cv2.waitKey(0)
    elif k==ord('q'):
        break
    cv2.imshow('frame', dst)
    vout.write(dst)
# When everything done, release the capture
vout.release()
cap.release()
cv2.destroyAllWindows()
