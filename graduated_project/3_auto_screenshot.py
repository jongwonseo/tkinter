import time
from PIL import ImageGrab

time.sleep(5) # 5초 대기

for i in range(1,11):
  img = ImageGrab.grab() #모니터 화면 자동 캡처
  img.save("image{}.png".format(i))
  time.sleep(2)