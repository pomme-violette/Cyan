import sys
import pandas
import numpy
import music21
from FeatureExtract import RhythmTransFeature
from FeatureExtract import PitchTransFeature
from FeatureExtract import Util


def main() -> music21.stream:
    if not sys.argv[1:]:
        raise ValueError("No input file specified")

    input_file_path = sys.argv[1]
    stream_object = Util.midi_to_stream(input_file_path)

    return stream_object


def get_pitch_trans_feature(stream_object: music21.stream) -> pandas.DataFrame:
    # Extract Melody Part
    melody_part = Util.extract_melody_part(stream_object, 0)

    melody_pitch_list = PitchTransFeature.extract(
        melody_part, octave_difference=True)
    melody_pitch_trans_df = PitchTransFeature.collection(
        melody_pitch_list, collection_type="absolute")

    return melody_pitch_trans_df


def get_rhythm_trans_feature(stream_object: music21.stream) -> pandas.DataFrame:
    # Extract Melody Part
    melody_part = Util.extract_melody_part(stream_object, 0)
    melody_note_dulation_list = RhythmTransFeature.extract(melody_part)

    return melody_note_dulation_list


def compose(pitch_transfeature: pandas.DataFrame, key: str, generate_melody_num: int) -> list[str]:
    """
    Args:
        pitch_transfeature (pandas.DataFrame):
        key (str):
        generate_melody_num (int):

    Returns:
        list[str]:

    Example:
        >>> compose(pitch_transfeature, "C", 4)
    """
    for i in range(len(pitch_transfeature)):
        pitch_transfeature.iloc[i, :] /= sum(pitch_transfeature.iloc[i, :])

    note_list = ["C", "C#", "D", "D#", "E",
                 "F", "F#", "G", "G#", "A", "A#", "B"]

    note_result = [key]
    for _ in range(generate_melody_num):
        now_note = note_result[-1]
        line = pitch_transfeature.loc[[now_note], :]
        next_num = numpy.random.choice(
            list(range(-12, 13)), size=1, p=line.values[0])[0]
        next_note = note_list[(note_list.index(now_note) + next_num) % 12]
        note_result.append(next_note)

    return note_result


if __name__ == "__main__":
    stream = main()
    rhythm_trans_feature_matrix = get_rhythm_trans_feature(stream)
    print(rhythm_trans_feature_matrix)
