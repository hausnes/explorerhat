# https://projects.raspberrypi.org/en/projects/explorer-hat-buggy/8
import explorerhat
from time import sleep
from guizero import App, PushButton
#from picamera import PiCamera

#kamera = PiCamera()
#kamera.rotation = 180
#kamera.resolution = (640, 480)

def forwards():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
    #kamera.start_preview()
    sleep(2)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    #kamera.stop_preview()


def backwards():
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

app = App("Buggy controller")

drive = PushButton(app, forwards, text="Framover")
reverse = PushButton(app, backwards, text="Revers")

app.display()