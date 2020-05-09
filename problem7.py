print("\t\t\t\t\"Caching\"")
inp=int(input("Enter the number of values you want to cache:"))
import time

from functools import lru_cache
@lru_cache (maxsize=inp)
def video_streaming(n):
    #for first time video takes n time for streaming
    time.sleep(n)
    return(n)

if __name__== '__main__':
    print("Start the video and watch to the end.")
    video_streaming(5)
    video_streaming(10)
    print("Start the video again from beginning")
    video_streaming(5)
    video_streaming(5)
    print("Start the video from mid ")