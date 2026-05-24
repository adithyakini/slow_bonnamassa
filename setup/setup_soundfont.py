import os
import requests

SOUNDFONT_URL = (
    "https://github.com/FluidSynth/"
    "fluidsynth/raw/master/sf2/VintageDreamsWaves-v2.sf2"
)

SOUNDFONT_PATH = (
    "soundfonts/VintageDreamsWaves-v2.sf2"
)


def ensure_soundfont():

    if os.path.exists(SOUNDFONT_PATH):
        return

    os.makedirs("soundfonts", exist_ok=True)

    response = requests.get(SOUNDFONT_URL)

    with open(SOUNDFONT_PATH, "wb") as file:
        file.write(response.content)

    print("SoundFont downloaded.")
