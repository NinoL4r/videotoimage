import cv2
videoFile = '~/aa.h264'
outputFile = '~/frame/aa--'
vc = cv2.VideoCapture(videoFile)
c = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    print('openerror!')
    rval = False

timeF = 1  #frame interval
while rval:
    # print(1)
    rval, frame = vc.read()
    if c % timeF == 0:
        # print(2)
        cv2.imwrite(outputFile + str(int(c / timeF)) + '.jpg', frame)
    c += 1
    cv2.waitKey(1)
vc.release()
