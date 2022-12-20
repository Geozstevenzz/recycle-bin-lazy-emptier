import os
import time

while True:
    # Empty the recycle bin
    os.system("rd /s /q C:\\$Recycle.bin")

    # Wait 15 days before emptying the recycle bin again
    time.sleep(60 * 60 * 24 * 15)
