import streamlit as st
from theory.chords import get_available_chords
from theory.genres import GENRE_PROGRESSIONS
from audio.arranger import create_band_midi
from audio.render import render_wav

st.set_page_config(
    page_title="Guitar Practice Tool",
    layout="wide"
)

st.title("🎸 Guitar Practice Tool")

if "progression" not in st.session_state:
    st.session_state.progression = []

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.header("Song Settings")

    genre = st.selectbox(
        "Genre",
        list(GENRE_PROGRESSIONS.keys())
    )

    key = st.selectbox(
        "Key",
        ["C", "G", "D", "A", "E", "Am"]
    )

    scale_type = st.selectbox(
        "Scale Type",
        ["Major", "Minor"]
    )

    bpm = st.slider(
        "Tempo (BPM)",
        60,
        180,
        120
    )

    beats_per_chord = st.selectbox(
        "Beats Per Chord",
        [2, 4, 8],
        index=1
    )

    st.divider()

    st.header("Band Instruments")

    enable_drums = st.checkbox("🥁 Drums", True)
    enable_bass = st.checkbox("🎸 Bass", True)
    enable_piano = st.checkbox("🎹 Piano", True)
    enable_strings = st.checkbox("🎻 Strings", True)
    enable_keys = st.checkbox("🎛️ Keys", True)

# ---------------- CHORDS ----------------

available_chords = get_available_chords(key, scale_type)

st.subheader("Available Chords")

cols = st.columns(len(available_chords))

for i, chord in enumerate(available_chords):
    with cols[i]:
        if st.button(chord):
            st.session_state.progression.append(chord)

st.divider()

# ---------------- PROGRESSION ----------------

st.subheader("Chord Progression")

progression_display = " | ".join(st.session_state.progression)

st.code(progression_display if progression_display else "No chords selected")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Remove Last"):
        if st.session_state.progression:
            st.session_state.progression.pop()

with col2:
    if st.button("🧹 Clear"):
        st.session_state.progression = []

with col3:
    if st.button("✨ Load Genre Preset"):
        st.session_state.progression = GENRE_PROGRESSIONS[genre]

st.divider()

# ---------------- GENERATE ----------------

if st.button("🎵 Generate Band Playback"):

    if not st.session_state.progression:
        st.warning("Please add chords first.")
    else:

        create_band_midi(
            chords=st.session_state.progression,
            bpm=bpm,
            beats_per_chord=beats_per_chord,
            drums=enable_drums,
            bass=enable_bass,
            piano=enable_piano,
            strings=enable_strings,
            keys=enable_keys,
            genre=genre
        )

        render_wav()

        st.success("Band track generated!")

        audio_file = open("generated/output.wav", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/wav")

        with open("generated/output.mid", "rb") as file:
            st.download_button(
                label="⬇ Download MIDI",
                data=file,
                file_name="progression.mid"
            )

        with open("generated/output.wav", "rb") as file:
            st.download_button(
                label="⬇ Download WAV",
                data=file,
                file_name="progression.wav"
            )
