import time
for hour in range (24):
    for minutes in range (60):
        for seconds in range(60):
            print( end="\r")
            print(hour,":", minutes,":",seconds, end=" ")
            time.sleep(1)
