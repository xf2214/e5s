import time

def countdown(timer):
    print("Focus started: 20 minutes")
    while timer > 0:
        print(timer // 60, ":", str(timer % 60).zfill(2), end='\r')
        time.sleep(1)
        timer -= 1
    print("\nTime's up! Good job.")

timer = 20*60
countdown(timer)
