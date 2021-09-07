#For any query,Contact me at instagram.com/saaalick
from plyer import notification
import time
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "Alecive-Flatwoken-Apps-Notifications.ico",
        timeout = 1,
    )


if __name__=="__main__":
while(True):
    notifyMe("Notification","Take a deep breathe and relax")
    #you can adjust the time as per your need
    time.sleep(150)
    notifyMe("Notification","Psst!Take your eyes screen and blink thrice")
    time.sleep(150)
    notifyMe("Notification","Rotate neck ClockWise and counter ClockWise")
    time.sleep(150)
    notifyMe("Notification","Adjust Your posture")
    time.sleep(150)
 


