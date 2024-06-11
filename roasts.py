import time
import random

roasts = open('roasts.txt').readlines()


print(random.choice(roasts))
while True:
    for roast in roasts:
        print(random.choice(roasts))
        time.sleep(0.5)
