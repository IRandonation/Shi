import os
import exifread

for file in os.listdir('.'):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    if file[-2: ] == 'py':
        continue   #过滤掉改名的.py文件
    img=exifread.process_file(open(file,'rb'))
    time=img['Image DateTime']
    #print(time)
    Time=str(time)
    new_name = Time+'.jpg'  #选择名字中需要保留的部分
    print(new_name)
    os.rename(file, new_name)