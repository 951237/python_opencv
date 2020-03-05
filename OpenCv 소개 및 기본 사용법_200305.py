import cv2

img_basic = cv2.imread('cat.png', cv2.IMREAD_COLOR) # 이미지 파일 컬러로 불러오기
cv2.imshow('Image Basic', img_basic) # 'Image Basic'는 그림창 타이틀
cv2.waitKey(0) # 창 기다리기
cv2.imwrite('result1.png', img_basic) # 이미지파일 저장하기

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY) #이미지 파일을 회색조로 지정하기
cv2.imshow('Image Gray', img_gray) # 이미지창 파일 불러오기
cv2.waitKey(0)
cv2.imwrite('result2.png', img_gray) #이미지 파일 저장하기

cv2.destroyAllWindows() # 이미지 닫기?

