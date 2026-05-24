import os
import urllib.request

SOUNDFONT_URL = (
    "https://member.keymusician.com/Member/"
    "FluidR3_GM/index.html"
)

SOUNDFONT_PATH = "soundfonts/FluidR3_GM.sf2"


def ensure_soundfont():

    if os.path.exists(SOUNDFONT_PATH):
        print("SoundFont already exists.")
        return

    os.makedirs("soundfonts", exist_ok=True)

    print("Please download FluidR3_GM.sf2 manually:")
    print(SOUNDFONT_URL)

    print(f"\nPlace it here:\n{SOUNDFONT_PATH}")
