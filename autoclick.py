

import pyautogui
import time
import threading
import keyboard

touches = ['w', 'd', 's', 'd', 'w', 'd', 's', 'a']

# Durées d'appui par touche (en secondes)
# Séquence: w 2.5s, d 1s, s 2.5s, d 1s, w 2.5s, d 1s, s 2.5s, a 3s
durations = {'w': 1.25, 'd': 0.5, 's': 1.25, 'a': 1.5}
# Temps entre deux appuis (en secondes)
gap_between_touches = 0

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
            # Récupère la durée d'appui pour la touche courante (par défaut 1s si manquant)
            duration = durations.get(touche, 1.0)
            keyboard.press(touche)
            time.sleep(duration)
            keyboard.release(touche)

            time.sleep(gap_between_touches)
except KeyboardInterrupt:
    stop_event.set()

print("Stopped (Ctrl+J or KeyboardInterrupt)")


