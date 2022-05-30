import sys
import music21
from FeatureExtract import RhythmTransFeature
from FeatureExtract import PitchTransFeature
from FeatureExtract import Util


def main() -> None:
    if not sys.argv[1:]:
        raise ValueError("No input file specified")

    input_file_path = sys.argv[1]
    stream_object = Util.midi_to_stream(input_file_path)

    return stream_object


def extract_rhythm_transitoin_feature(stream_object: music21.stream):
    # Extract Melody Part
    melody_part = Util.extract_melody_part(stream_object, 0)

    # Extract melody rhytm transition matrix
    temp = PitchTransFeature.extract(melody_part)
    print(temp)
    # melody_rhythm_transition_feature = rte.RhythmTransExtract.convert_dulation_to_string(
    #     temp)

    # for i in temp:
    #     # print(f"offset: {i[0]}, dulation: {i[1]}")
    #     # print(
    #     #     rte.RhythmTransExtract.convert_note_dulation_to_string(i[0]), i[1])
    #     print(i)

    # return melody_rhythm_transition_feature


# def extract_melody_pitch_transition_feature(stream_object: stream):
#     # Extract melody part
#     melody_part = util.Util.extract_melody_part(stream_object, 1)

#     # Extract melody pitch transition matrix
#     melody_pitch_transition_feature = pte.PitchTransExtract.extract(melody_part)

#     print(melody_pitch_transition_feature)


if __name__ == "__main__":
    stream_object = main()
    extract_rhythm_transitoin_feature(stream_object)
