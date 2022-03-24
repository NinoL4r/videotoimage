import cv2
videoFile = '~/2022-03-19-12-15-57_screen.h264'
outputFile = '~/frame/2022-03-19-12-15-57--'
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
