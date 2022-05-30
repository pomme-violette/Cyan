import matplotlib.pyplot as plt
import seaborn as sns
from music21 import stream
from music21 import midi


class Util:
    def __init__(self):
        pass

    def generate_feature_heatmap(self, input) -> None:
        plt.figure()
        sns.heatmap(input, annot=True, cmap='Greys')
        plt.xlabel("To")
        plt.ylabel("From")
        plt.show()
        plt.close('all')

    @classmethod
    def midi_to_stream(cls, midi_file_path) -> stream:
        """
        Args:
            midi_file_path (str): Input file path.

        Return:
            stream_object (music21.stream): Return object which type is stream of music21.
        """
        mf = midi.MidiFile()
        mf.open(midi_file_path)
        mf.read()
        stream_object = midi.translate.midiFileToStream(mf)
        return stream_object

    @classmethod
    def extract_melody_part(cls, stream_object: stream, melody_part_index: int) -> stream:
        """
        Args:
            stream_object (music21.stream): Input stream object.

        Return:
            melody_part (music21.stream): Return stream object which type is stream of music21.
        """
        return stream_object[melody_part_index]

    @staticmethod
    def convert_note_dulation_to_string(note_dulation: int) -> str:
        match note_dulation:
            case 0.0625:
                note_dulation = '64th'
            case 0.0125:
                note_dulation = "32nd"
            case 0.25:
                note_dulation = "16th"
            case 0.5:
                note_dulation = "eighth"
            case 1.0:
                note_dulation = "quarter"
            case 2.0:
                note_dulation = "half"
            case 4.0:
                note_dulation = "whole"
            case 8.0:
                note_dulation = "breve"
            case 16.0:
                note_dulation = "longa"
            case 32.0:
                note_dulation = "maxima"
            case 64.0:
                note_dulation = "duplex-maxima"

        return note_dulation
