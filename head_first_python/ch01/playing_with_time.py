from datetime import datetime
import time
import random
runMe = True
while runMe:
    second_of_minute = datetime.today().second
    if second_of_minute % 2 == 0:
        print(str(second_of_minute) +" is even")
    else:
        print(str(second_of_minute) +" is odd")
    rnd = random.randint(1,10)
    if rnd<=9:
        print("pausing for " + str(rnd) + " seconds")
        time.sleep(rnd)
    else:
        print("we've hit " + str(rnd) + " so that's all folks")
        runMe = False

    


