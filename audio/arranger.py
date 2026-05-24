from midiutil import MIDIFile
from theory.chords import chord_to_notes
from audio.drums import add_drum_pattern

TRACK_PIANO = 0
TRACK_BASS = 1
TRACK_STRINGS = 2
TRACK_KEYS = 3
TRACK_DRUMS = 4


def create_band_midi(
    chords,
    bpm=120,
    beats_per_chord=4,
    drums=True,
    bass=True,
    piano=True,
    strings=True,
    keys=True,
    genre="Pop"
):

    midi = MIDIFile(5)

    for track in range(5):
        midi.addTempo(track, 0, bpm)

    # ---------------- INSTRUMENTS ----------------

    # Piano
    midi.addProgramChange(TRACK_PIANO, 0, 0, 0)

    # Bass
    midi.addProgramChange(TRACK_BASS, 1, 0, 33)

    # Strings
    midi.addProgramChange(TRACK_STRINGS, 2, 0, 48)

    # Keys
    midi.addProgramChange(TRACK_KEYS, 3, 0, 4)

    time = 0

    for chord in chords:

        notes = chord_to_notes(chord)

        # ---------------- PIANO ----------------

        if piano:
            for note in notes:
                midi.addNote(
                    TRACK_PIANO,
                    0,
                    note,
                    time,
                    beats_per_chord,
                    90
                )

        # ---------------- BASS ----------------

        if bass:
            midi.addNote(
                TRACK_BASS,
                1,
                notes[0] - 12,
                time,
                beats_per_chord,
                100
            )

        # ---------------- STRINGS ----------------

        if strings:
            for note in notes:
                midi.addNote(
                    TRACK_STRINGS,
                    2,
                    note + 12,
                    time,
                    beats_per_chord,
                    65
                )

        # ---------------- KEYS ----------------

        if keys:
            for note in notes:
                midi.addNote(
                    TRACK_KEYS,
                    3,
                    note,
                    time,
                    beats_per_chord,
                    55
                )

        # ---------------- DRUMS ----------------

        if drums:
            add_drum_pattern(
                midi,
                TRACK_DRUMS,
                time,
                beats_per_chord,
                genre
            )

        time += beats_per_chord

    with open("generated/output.mid", "wb") as output_file:
        midi.writeFile(output_file)
