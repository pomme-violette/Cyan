import sys
from FeatureExtract import PitchTransExtract as pt
from FeatureExtract import RhythmTransExtract as rt
from FeatureExtract import util


def main() -> None:
    if not sys.argv[1:]:
        raise ValueError("No input file specified")

    # pitch_trans_extract = pt.PitchTransExtract(sys.argv[1])
    # pitch_trans_feature = pitch_trans_extract.extract()
    # pitch_trans_extract.generate_melody_feature_heatmap(pitch_trans_feature)

    rhythm_trans_extract = rt.RhythmTransExtract(sys.argv[1])
    rhythm_trans_feature = rhythm_trans_extract.extract()

    utility = util.Util()
    utility.generate_feature_heatmap(rhythm_trans_feature)
    return None


if __name__ == "__main__":
    main()
