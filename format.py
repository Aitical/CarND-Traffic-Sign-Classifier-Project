import os
import cv2

folders = os.listdir('./')

for folder in folders:
    if folder =='test' or folder.endswith('.py'):
        continue
    files = os.listdir(folder)
    i = 0
    for f in files:
        if f.endswith('.csv'):
            continue
        print(folder, f)
        class_id = int(folder)
        img = cv2.imread(folder+'\\'+f)
        img = cv2.resize(img, (32, 32))
        i+=1
        cv2.imwrite('test/'+ str(i)+'_'+str(class_id)+'.jpg', img)
