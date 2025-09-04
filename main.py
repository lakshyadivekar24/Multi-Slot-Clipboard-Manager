import pyperclip
from pynput import keyboard

slots = {}
current_keys = set()

def copy_to_slot(n):
    text = pyperclip.paste()
    slots[n] = text
    print(f"✅ Saved to slot {n}: {text}")

def set_clipboard_from_slot(n):
    if n in slots:
        pyperclip.copy(slots[n])
        print(f"📋 Slot {n} copied to clipboard: {slots[n]}")
    else:
        print(f"⚠️ Slot {n} is empty")

def on_press(key):
    try:
        if key == keyboard.Key.cmd:
            current_keys.add('cmd')
        elif key == keyboard.Key.ctrl:
            current_keys.add('ctrl')
        elif hasattr(key, 'char') and key.char:
            if key.char in '123456789':
                n = int(key.char)
                # Copy → Cmd+C+Num
                if 'cmd' in current_keys and 'c' in current_keys:
                    copy_to_slot(n)
                # Paste → Ctrl+Num
                elif 'ctrl' in current_keys:
                    set_clipboard_from_slot(n)
            elif key.char in ['c','v']:
                current_keys.add(key.char)
    except Exception as e:
        print("Error:", e)

def on_release(key):
    if key == keyboard.Key.cmd:
        current_keys.discard('cmd')
    elif key == keyboard.Key.ctrl:
        current_keys.discard('ctrl')
    elif hasattr(key, 'char') and key.char in ['c','v']:
        current_keys.discard(key.char)

print("🚀 Multi-Clipboard started!")
print("👉 Cmd+C+<num> = Copy to slot")
print("👉 Ctrl+<num> = Set slot to clipboard (then press Cmd+V manually)")

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
