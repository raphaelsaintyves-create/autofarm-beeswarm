

import pyautogui
import time
import threading
import keyboard

touches = ['w', 'a', 's', 'd']

# Event utilisé pour demander l'arrêt propre du programme
stop_event = threading.Event()

# Fonction pour cliquer avec la souris toutes les 0,1 s
def clic_souris():
    while not stop_event.is_set():
        pyautogui.click()
        time.sleep(0.1)


print("Attente 10 secondes avant le lancement...")
time.sleep(10)
print("Lancement")
# Lance le clic souris dans un autre thread
threading.Thread(target=clic_souris, daemon=True).start()

# Enregistre la combinaison Ctrl+J pour arrêter proprement
keyboard.add_hotkey('ctrl+j', lambda: stop_event.set())


try:
    # Boucle principale des touches — s'arrête si stop_event est défini
    while not stop_event.is_set():
        print("Pression des touches...")
        for touche in touches:
            if stop_event.is_set():
                break
            keyboard.press(touche)
            time.sleep(2.5)
            keyboard.release(touche)

            time.sleep(1)
except KeyboardInterrupt:
    stop_event.set()

print("Stopped (Ctrl+J orq KeyboardInterrupt)")


