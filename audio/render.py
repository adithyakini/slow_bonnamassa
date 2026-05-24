import subprocess


def render_wav():

    subprocess.run([
        "fluidsynth",
        "-ni",
        "soundfonts/FluidR3_GM.sf2",
        "generated/output.mid",
        "-F",
        "generated/output.wav",
        "-r",
        "44100"
    ])
