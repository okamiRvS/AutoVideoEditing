import cv2
import numpy as np
from threading import Condition
import queue
import os
import pdb

class MyVideo():

    def __init__(self, que) -> None:
        
        # get path of all scenes
        self.pathVideos = []
        SCENES_PATH = os.path.join('media', 'scenes')
        for root, dirs, files in os.walk(SCENES_PATH, topdown=True):
            for file in files:
                pathVideo = os.path.join(root, file)
                self.pathVideos.append(pathVideo)
        
        # current scene
        self.idx = 0

        # Create a VideoCapture object and read from input file
        # If the input is the camera, pass 0 instead of the video file name
        # initialize with the first path
        self.cap = cv2.VideoCapture(self.pathVideos[self.idx])

        # suppose you want to start reading from frame no 500
        self.frame_set_no = 200 

        # capture is set to the desired frame
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_set_no)

        # set queue to share variable through threds
        self.que = que

        # to check update in the queue
        self.oldCount = -1

    def run(self):
        # Check if camera opened successfully
        if (self.cap.isOpened()== False): 
            print("Error opening video stream or file")

        condition_object = Condition()

        # Read until video is completed
        while(self.cap.isOpened()):

            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if ret == True:

                # resize
                width = 848
                height = 480
                dim = (width, height)
                frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

                condition_object.acquire() # get control of the thread
                counter = self.que.get()
                if counter != self.oldCount:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_set_no + (counter*50) )
                    #print(f"video {counter}")
                    self.oldCount = counter

                self.que.put(counter)
                condition_object.release() # release the lock

                # Display the resulting frame
                cv2.imshow('Frame',frame)

                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            elif self.idx < len(self.pathVideos)-1:
                print(f"Scene {self.idx} is finished")

                condition_object.acquire()

                # reset counter
                counter = self.que.get()
                self.que.put(0)

                # open next video
                self.idx += 1
                self.cap = cv2.VideoCapture(self.pathVideos[self.idx])

                condition_object.release()
            else:
                # Break the loop
                break 

        # When everything done, release the video capture object
        self.cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

def main():
    MyVideo().run()

if __name__ == "__main__":
    main()