from music21 import stream
from music21 import chord
from music21 import note
from music21 import midi
import pandas


class PitchTransExtract:
    def __init__(self, midi_file_path: str):
        self.midi_file_path = midi_file_path

    def midi_to_stream(self) -> stream:
        """
        Args:
            midi_file_path (str): Input file path.

        Return:
            stream_object (music21.stream): Return object which type is stream of music21.
        """
        mf = midi.MidiFile()
        mf.open(self.midi_file_path)
        mf.read()
        stream_object = midi.translate.midiFileToStream(mf)
        return stream_object

    def extract(self) -> pandas.DataFrame:
        """
        Args:
            midi_file_path (str): Input file path.

        Return:
            collected_array (pandas.DataFrame):
        """
        stream_object = self.midi_to_stream()
        target_part = stream_object[0]
        pitch_list = ["C", "C#", "D", "D#", "E",
                      "F", "F#", "G", "G#", "A", "A#", "B"]
        melody_array = []
        collected_array = pandas.DataFrame(index=pitch_list,
                                           columns=pitch_list)
        collected_array.fillna(0, inplace=True)

        for measure in target_part:
            for in_measure_object in measure:
                if isinstance(in_measure_object, note.Note):
                    append_in_measure_object = in_measure_object.pitch.name
                    melody_array.append(append_in_measure_object)

                elif isinstance(in_measure_object, chord.Chord):
                    append_in_measure_object = in_measure_object.pitches[0].name
                    melody_array.append(append_in_measure_object)

        for melody in range(len(melody_array)-1):
            collected_array.loc[str(melody_array[melody]),
                                str(melody_array[melody+1])] += 1

        return collected_array
