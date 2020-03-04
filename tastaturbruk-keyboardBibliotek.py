import keyboard # https://pypi.org/project/keyboard/

try:    
    while True:
        if keyboard.is_pressed('a'):
            print("a!")
        if keyboard.is_pressed('s'):
            print("s!")
except KeyboardInterrupt:
        print("Avsluttar.")
