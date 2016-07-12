

import os
from threading import Timer
import time


while(1):
	
        start_time = time.time()
  
        time.sleep(900)

        start_time1 = time.time()
        
        while(time.time() - start_time1 <=30):
            os.system("xset dpms force off")

        os.system("xset dpms force on")
# t.start();