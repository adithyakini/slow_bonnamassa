MAJOR_KEYS = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"]
}

MINOR_KEYS = {
    "Am": ["Am", "Bdim", "C", "Dm", "Em", "F", "G"]
}

NOTE_MAP = {
    "C": 60,
    "C#": 61,
    "D": 62,
    "D#": 63,
    "E": 64,
    "F": 65,
    "F#": 66,
    "G": 67,
    "G#": 68,
    "A": 69,
    "A#": 70,
    "B": 71
}


def get_available_chords(key, scale_type):

    if scale_type == "Major":
        return MAJOR_KEYS.get(key, [])

    return MINOR_KEYS.get(key, [])


def chord_to_notes(chord):

    root = chord.replace("m", "").replace("dim", "")

    base_note = NOTE_MAP[root]

    if "dim" in chord:
        return [base_note, base_note + 3, base_note + 6]

    if "m" in chord:
        return [base_note, base_note + 3, base_note + 7]

    return [base_note, base_note + 4, base_note + 7]
