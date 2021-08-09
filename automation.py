import cv2
import dropbox
import time 
import random

startTime = time.time()
def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while (result):
        ret,frame = videoCaptureObject.read()
        imageName ="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime = time.time()
        result = False

    return imageName
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
 access_token = "A-6BvMN99AgAAAAAAAAAAbfsPJhXX1vpsW9sNmXZErTpxIqfvtTpGo9LyKZgDnQj"
 file_from = imageName
 file_to ="/automation/"+ imageName

 dbx = dropbox.Dropbox(access_token)

 with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to)

def main():
    while True :
        if (time.time()-startTime)>30 :
            name = takeSnapshot()
            upload_file(name)
 
main()

