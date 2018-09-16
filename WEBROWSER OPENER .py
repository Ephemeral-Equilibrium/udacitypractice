import time
import webbrowser

breakcount = 5
breakstaken = 0 

while(breakcount > breakstaken):
    time.sleep(60*60)
    webbrowser.open("https://www.youtube.com/watch?v=sAMvv8kvG5M")
    breakstaken + 1
