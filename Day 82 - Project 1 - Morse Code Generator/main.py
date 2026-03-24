import pygame
import time
import numpy as np

# 1. Initialize Pygame Audio
pygame.mixer.init(frequency=44100, size=-16, channels=1)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def play_tone(duration, volume=0.5):
    f = 800
    sample_rate = 44100
    n_samples = int(duration * sample_rate)

    t = np.linspace(0, duration, n_samples, False)
    tone = np.sin(f * t * 2 * np.pi)

    sound_array = (tone * 32767 * volume).astype(np.int16)
    stereo_signal = np.column_stack((sound_array, sound_array))

    sound = pygame.sndarray.make_sound(stereo_signal)
    sound.play()
    time.sleep(duration)

def play_morse(morse_string):
    dot_duration = 0.1  # The "Unit" speed

    for symbol in morse_string:
        print(symbol, end='', flush=True) # Shows the symbol as it plays
        if symbol == '.':
            play_tone(dot_duration)
            time.sleep(dot_duration)  # Gap between dits/dahs
        elif symbol == '-':
            play_tone(dot_duration * 3)
            time.sleep(dot_duration)  # Gap between dits/dahs
        elif symbol == ' ':
            time.sleep(dot_duration * 3)  # Gap between letters
        elif symbol == '/':
            time.sleep(dot_duration * 7)  # Gap between words
    print() # New line after finished


user_input = input("Enter text to convert: ").strip().upper()


encoded_list = []
for char in user_input:
    code = MORSE_CODE_DICT.get(char, "")
    if code:
        encoded_list.append(code)


final_string = " ".join(encoded_list)

print(f"\nTranslating to Morse: {final_string}")
print("Playing Sound: ", end='')
play_morse(final_string)
