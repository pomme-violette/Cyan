# from FeatureExtract import Util
from music21 import stream
from music21 import chord
from music21 import note
from music21 import pitch
import pandas
import fractions


class PitchTransFeature:

    def __init__(self):
        pass

    @staticmethod
    def calc_pitch_diff(pitch_1, pitch_2) -> int:
        return pitch.Pitch(pitch_1).pitchClass - pitch.Pitch(pitch_2).pitchClass

    @staticmethod
    def extract(part: stream) -> pandas.DataFrame:
        """
        Args:
            part (music21.stream.Stream): 

        Return:
            collected_array (pandas.DataFrame):
        """
        # !FUTURE WORKS:
        pitch_list = ["C", "C#", "D", "D#", "E",
                      "F", "F#", "G", "G#", "A", "A#", "B"]
        melody_array = []
        collected_array = pandas.DataFrame(index=pitch_list,
                                           columns=pitch_list)
        collected_array.fillna(0, inplace=True)

        for measure in part:
            for in_measure_object in measure:
                if isinstance(in_measure_object, note.Note):
                    append_in_measure_object = in_measure_object.pitch.name
                    melody_array.append(append_in_measure_object)

                elif isinstance(in_measure_object, chord.Chord):
                    append_in_measure_object = in_measure_object.pitches[0].name
                    melody_array.append(append_in_measure_object)

        def collection(melody_array: list[str, str], *, collection_type: str) -> pandas.DataFrame:
            pitch_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

            if collection_type == "key":
                collected_array = pandas.DataFrame(index=pitch_list,
                                                   columns=pitch_list)
                collected_array.fillna(0, inplace=True)
                for melody in range(len(melody_array) - 1):
                    collected_array.loc[str(melody_array[melody]),
                                        str(melody_array[melody + 1])] += 1


            if collection_type == "absolute":
                collected_array = pandas.DataFrame(index=pitch_list,
                                                   columns=[i for i in range(-12, 12 + 1)])
                collected_array.fillna(0, inplace=True)
                for melody in range(len(melody_array) - 1):
                    for pitch_list_item in pitch_list:
                        if melody_array[melody] == pitch_list_item:
                            for pitch_list_item in pitch_list:
                                if melody_array[melody + 1] == pitch_list_item:
                                    pitch_diff = PitchTransFeature.calc_pitch_diff(melody_array[melody],
                                                                                   melody_array[melody + 1])
                                    collected_array.loc[melody_array[melody], pitch_diff] += 1

            return collected_array

        return collection(melody_array, collection_type="key")


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
                # 不要オブジェクトの除外()
                if isinstance(in_measure_object, note.Note):
                    append_in_measure_object = in_measure_object

                # コードオブジェクトからノートオブジェクトへの変換(最高音に置換)
                elif isinstance(in_measure_object, chord.Chord):
                    append_in_measure_object = in_measure_object[0]

                else:
                    continue

                # ノートオブジェクトから小説に対する相対位置, 音の長さを取得
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
