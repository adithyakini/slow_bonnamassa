import subprocess
import os


def render_wav():

    os.makedirs("generated", exist_ok=True)

    command = [
        "fluidsynth",
        "-ni",
        "soundfonts/GeneralUser-GS.sf2",
        "generated/output.mid",
        "-F",
        "generated/output.wav",
        "-r",
        "44100"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode != 0:
        raise Exception(
            f"FluidSynth failed:\n{result.stderr}"
        )
