# all imports
import sys
import scipy.io.wavfile as scipwav
import numpy as np
import matplotlib.pyplot as  plt
from scipy import signal
import math

# main program
def kaiseki():
    # readfile
    rate ,data = scipwav.read(wavfile)

    # inv sound file
    data = data / 32768
    time = np.arange(0,data.shape[0]/rate,1/rate)
    inveddata = max(data)
    print("Point:"+str(inveddata))
    global nclass
    global pointdata
    pointdata = str(inveddata)

    print(wavfile)

    # self check
    if inveddata > 0.8:
        print("this nakisuna is 4 class")
        nclass = 4
    else:
        if inveddata > 0.7:
            print("this nakisuna is 3 class")
            nclass = 3
        else:
            if inveddata > 0.6:
                print("this nakisuna is 2 class")
                nclass = 2
            else:
                if inveddata > 0.4:
                    print("this nakisuna is 1 class")
                    nclass = 1
                else:
                    print("this nakisuna is 0 class")
                    nclass = 0

if __name__ == "__main__":
    # set sample file
    wavfile = "exit-sample.wav"
    kaiseki()
    print(nclass)