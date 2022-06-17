from music21 import stream
from music21 import chord
from music21 import note
from music21 import pitch
from music21 import midi
import pandas
import fractions
import matplotlib.pyplot as plt
import seaborn as sns


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
            case 0.001953125:
                note_dulation = "2048th"
            case 0.00390625:
                note_dulation = "1024th"
            case 0.0078125:
                note_dulation = "512th"
            case 0.015625:
                note_dulation = "256th"
            case 0.03125:
                note_dulation = "128th"
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


class PitchTransFeature:

    def __init__(self):
        pass

    @staticmethod
    def calc_pitch_diff(pitch_1, pitch_2) -> int:
        return pitch.Pitch(pitch_2).midi - pitch.Pitch(pitch_1).midi

    @staticmethod
    def extract(part: stream) -> list[str]:
        """
        Args:
            part (music21.stream.Stream):

        Return:
            melody_pitch_list (list[str]):
        """
        melody_pitch_list = []

        for measure in part:
            for in_measure_object in measure:
                if isinstance(in_measure_object, note.Note):
                    append_in_measure_object = in_measure_object.nameWithOctave
                    melody_pitch_list.append(append_in_measure_object)
                elif isinstance(in_measure_object, chord.Chord):
                    append_in_measure_object = in_measure_object.pitches[-1].nameWithOctave
                    melody_pitch_list.append(append_in_measure_object)

        return melody_pitch_list

    def collection(melody_pitch_list: list[str, str], *, collection_type: str) -> pandas.DataFrame:
        pitch_list = ["C", "C#", "D", "D#", "E",
                      "F", "F#", "G", "G#", "A", "A#", "B"]
        if collection_type == "key":
            collected_array = pandas.DataFrame(index=pitch_list,
                                               columns=pitch_list)
            collected_array.fillna(0, inplace=True)
            for melody in range(len(melody_pitch_list) - 1):
                collected_array.loc[str(melody_pitch_list[melody]),
                                    str(melody_pitch_list[melody + 1])] += 1
        # !DO NOT DELETE
        # if collection_type == "absolute":
        #     collected_array = pandas.DataFrame(index=pitch_list,
        #                                        columns=[i for i in range(-12, 12 + 1)])
        #     collected_array.fillna(0, inplace=True)
        #     for melody in range(len(melody_array) - 1):
        #         for pitch_list_item in pitch_list:
        #             if melody_array[melody] == pitch_list_item:
        #                 for pitch_list_item in pitch_list:
        #                     if melody_array[melody + 1] == pitch_list_item:
        #                         pitch_diff = PitchTransFeature.calc_pitch_diff(melody_array[melody],
        #                                                                        melody_array[melody + 1])
        #                         collected_array.loc[melody_array[melody], pitch_diff] += 1
        if collection_type == "absolute":
            pitch_diff_column = [str(i) for i in range(-12, 12+1)]
            pitch_index = ["C", "C#", "D", "D#", "E",
                           "F", "F#", "G", "G#", "A", "A#", "B"]
            melody_pitch_trans_df = pandas.DataFrame(
                index=pitch_index, columns=pitch_diff_column)
            melody_pitch_trans_df.fillna(0, inplace=True)

            for melody_pitch_index in range(len(melody_pitch_list) - 1):
                # print(melody_pitch_list[melody_pitch_index], melody_pitch_list[melody_pitch_index + 1])
                for pitch_ in pitch_index:
                    if melody_pitch_list[melody_pitch_index][:-1] == pitch_:
                        pitch_diff = PitchTransFeature.calc_pitch_diff(melody_pitch_list[melody_pitch_index],
                                                                       melody_pitch_list[melody_pitch_index + 1])
                        melody_pitch_trans_df.loc[melody_pitch_list[melody_pitch_index][:-1], str(
                            pitch_diff)] += 1

        return melody_pitch_trans_df


class RhythmTransFeature:

    def __init__(self):
        pass

    @staticmethod
    def extract(part_object: stream.Part) -> pandas.DataFrame:
        """
        """
        countable_array = []
        collected_array = pandas.DataFrame(
            index=[0.0, fractions.Fraction(1, 3), 0.5, fractions.Fraction(2, 3), 1.0, fractions.Fraction(4, 3), 1.5,
                   2.0, 2.5, 3.0, 3.5, 4.0],
            columns=['duplex-maxima', 'maxima', 'longa', 'breve', 'whole', 'half', 'quarter', 'eighth', '16th', '32nd',
                     '64th', '128th', '256th', '512th', '1024th', '2048th'])
        collected_array.fillna(0, inplace=True)

        for measure in part_object:
            for in_measure_object in measure:
                # Exclusion unwanted objects
                if isinstance(in_measure_object, note.Note):
                    append_in_measure_object = in_measure_object

                # コードオブジェクトからノートオブジェクトへの変換(最高音に置換)
                elif isinstance(in_measure_object, chord.Chord):
                    append_in_measure_object = in_measure_object[:-1]

                else:
                    continue

                # ノートオブジェクトから小節に対する相対位置, 音の長さを取得
                countable_array.append(
                    [append_in_measure_object.offset, append_in_measure_object.quarterLength])

        for i in countable_array:
            for offset in collected_array.index:
                if i[0] == offset:
                    for duration in collected_array.columns:
                        if i[0] == 0.0:
                            continue

                        if Util.convert_note_dulation_to_string(i[1]) == duration:
                            collected_array.loc[offset, duration] += 1

        return collected_array
