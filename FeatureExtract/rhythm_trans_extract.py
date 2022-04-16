from music21 import stream
from music21 import chord
from music21 import note
from music21 import midi
from music21 import instrument
import pandas

class TestTools:
    def __init__(self, midi_file_path):
        self.midi_file_path = midi_file_path

    # def midi_to_score(self) -> stream.Score:
    #     midi.MidiFile(self.midi_file_path).read()
    #     score = midi.translate.midiFilePathToStream(self.midi_file_path)
    #     score.show('text') if text else score.show()
    #     return score


class RhythmTransExtract:
    def __init__(self, midi_file_path):
        self.midi_file_path = midi_file_path
        self.stream_object = self.midi_to_stream()

    def midi_to_stream(self) -> stream.Score:
        """
        Args:
            midi_file_path (str): Input file path

        Return:
            stream_object (music21.stream): Return object which type is stream of music21.
        """
        mf = midi.MidiFile()
        mf.open(self.midi_file_path)
        mf.read()
        stream_object = midi.translate.midiFileToStream(mf)
        return stream_object

    def extract(self, *, quarter_length: bool = False):
        """
        Note:
            stream_object[0] is melody part.
        """

        stream_object = self.stream_object[0]

        element_offset = []
        element_quarter_length = []

        countable_array = []

        collection_array = []

        # 不要オブジェクトリスト
        remove_objects = [instrument.Piano]

        # stream_object.show("text")

        for measure_i, measure in enumerate(stream_object):
            # print(f"{measure_i}: {measure}")
            for element_i, element in enumerate(measure):
                # 不要オブジェクトの除外
                if type(element) in remove_objects:
                    continue

                # コードオブジェクトからノートオブジェクトへの変換(最高音に置換)
                if type(element) is chord.Chord:
                    element = element[0]

                # print(f"{element_i}: {element}")

                # ノートオブジェクトから小説に対する相対位置, 音の長さを取得
                # print(f"Offset: {element.offset} QuarterLength: {element.quarterLength}")
                # element_offset_list.append(element.offset)
                # element_quarter_length_list.append(element.quarterLength)

                countable_array.append([element.offset, element.quarterLength])

        # 出現した相対位置でイテレーション
        # element_offset_counter = collections.Counter(element_offset)
        # element_quarter_length_counter = collections.Counter(element_quarter_length)
        # print(countable_array)

        collected_array = pandas.DataFrame(index=["0.0", "1/3", "0.5", "2/3", "1.0", "4/3", "1.5", "2.0", "2.5", "3.0", "3.5"],
                                           columns=["0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0"])
        collected_array.fillna(0, inplace=True)

        for i in countable_array:
            # print(i)

            # DO NOT DELETE!
            # if i[0] == 0.0:
            #     if i[1] == 0.5:
            #         collected_array.loc["0.0", "0.5"] += 1
            #     elif i[1] == 1.0:
            #         collected_array.loc["0.0", "1.0"] += 1
            #     elif i[1] == 1.5:
            #         collected_array.loc["0.0", "1.5"] += 1
            #     elif i[1] == 2.0:
            #         collected_array.loc["0.0", "2.0"] += 1
            #     elif i[1] == 2.5:
            #         collected_array.loc["0.0", "2.5"] += 1
            #     elif i[1] == 3.0:
            #         collected_array.loc["0.0", "3.0"] += 1
            #     elif i[1] == 3.5:
            #         collected_array.loc["0.0", "3.5"] += 1

            # DO NOT DELETE!
            # if i[0] == 0.0:
            #     for dulation in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]:
            #         if i[1] == dulation:
            #             collected_array.loc["0.0", str(dulation)] += 1

            # if i[0] == 0.5:
            #     for dulation in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]:
            #         if i[1] == dulation:
            #             collected_array.loc["0.5", str(dulation)] += 1

            offset_valiation = [0.0, 1/3, 0.5, 2/3,
                                1.0, 4/3, 1.5, 2.0, 2.5, 3.0, 3.5]
            dulation_valiation = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

            for offset in offset_valiation:
                if i[0] == offset:
                    for dulation in dulation_valiation:
                        if i[1] == dulation:
                            collected_array.loc[str(
                                offset), str(dulation)] += 1

        return collected_array