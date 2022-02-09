import multiprocessing
from fileParser import Mbase
from main import getQueue
from pynput import keyboard

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=Mbase)
    p1.start()


def on_release(key):
    if key == keyboard.Key.esc:
        p1.terminate()
        f = open("workingFile", "r")
        file = f.read()
        f = open(file, "a")
        f.write("TERMINAZIONE ANTICIPATA")
        f.write("\n")
        f.close()
        f = open("Complessita_"+file, "a")
        f.write("TERMINAZIONE ANTICIPATA")
        f.write("\n")
        f.close()
        f = open("Complessita_" + file + "OPTIMIZED", "a")
        f.write("TERMINAZIONE ANTICIPATA")
        f.write("\n")
        f.close()
        f = open(file + "OPTIMIZED", "a")
        f.write("TERMINAZIONE ANTICIPATA")
        f.write("\n")
        f.close()
        exit()
        return False

listener = keyboard.Listener(
    on_release=on_release)
listener.start()