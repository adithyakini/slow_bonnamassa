def add_drum_pattern(
    midi,
    track,
    start_time,
    beats,
    genre
):

    channel = 9

    for beat in range(beats):

        current_time = start_time + beat

        # Kick
        if beat in [0, 2]:
            midi.addNote(
                track,
                channel,
                36,
                current_time,
                1,
                110
            )

        # Snare
        if beat in [1, 3]:
            midi.addNote(
                track,
                channel,
                38,
                current_time,
                1,
                100
            )

        # Hi Hat
        midi.addNote(
            track,
            channel,
            42,
            current_time,
            1,
            70
        )
