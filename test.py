from music21 import *
import pandas

pitch_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
collected_array = pandas.DataFrame(index=pitch_list,
                                   columns=[i for i in range(-12, 12 + 1)])
collected_array.fillna(0, inplace=True)

melody_array = ['F#', 'E', 'D', 'C#', 'B', 'A', 'B', 'C#', 'A', 'A', 'F#', 'F#', 'D', 'D', 'D', 'E', 'D', 'F#', 'A',
                'G', 'F#', 'D', 'F#', 'E', 'D', 'B', 'D', 'F#', 'G', 'B', 'A', 'G', 'D', 'F#', 'E', 'G', 'D', 'D', 'C#',
                'E', 'B', 'B', 'A', 'F#', 'B', 'B', 'C#', 'G', 'D', 'C#', 'D', 'A', 'A', 'C#', 'D', 'F#', 'A', 'B', 'G',
                'F#', 'E', 'G', 'F#', 'E', 'D', 'C#', 'B', 'A', 'D', 'D', 'C#', 'D', 'C#', 'D', 'A', 'A', 'C#', 'D',
                'F#', 'A', 'B', 'G', 'F#', 'E', 'G', 'F#', 'E', 'D', 'C#', 'B', 'A', 'D', 'D', 'C#', 'D', 'C#', 'D',
                'A', 'C#', 'A', 'E', 'F#', 'D', 'D', 'C#', 'B', 'C#', 'F#', 'A', 'B', 'G', 'F#', 'E', 'G', 'F#', 'E',
                'D', 'C#', 'B', 'A', 'G', 'F#', 'E', 'G', 'F#', 'E', 'D', 'E', 'F#', 'G', 'A', 'E', 'A', 'G', 'F#', 'B',
                'A', 'G', 'A', 'G', 'F#', 'E', 'D', 'B', 'B', 'C#', 'D', 'F#', 'E', 'D', 'F#', 'G', 'D', 'C#', 'B',
                'C#', 'D', 'C#', 'A', 'F#', 'G', 'A', 'F#', 'G', 'A', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G', 'F#', 'D',
                'E', 'F#', 'F#', 'G', 'A', 'B', 'A', 'G', 'A', 'F#', 'G', 'A', 'G', 'B', 'A', 'G', 'F#', 'E', 'F#', 'E',
                'D', 'E', 'F#', 'G', 'A', 'B', 'G', 'B', 'A', 'B', 'C#', 'D', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G', 'A',
                'A', 'F#', 'G', 'A', 'F#', 'G', 'A', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G', 'F#', 'D', 'E', 'F#', 'F#',
                'G', 'A', 'B', 'A', 'G', 'A', 'F#', 'G', 'A', 'G', 'B', 'A', 'G', 'F#', 'E', 'F#', 'E', 'D', 'E', 'F#',
                'G', 'A', 'B', 'G', 'B', 'A', 'B', 'C#', 'D', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'F#', 'D', 'E',
                'F#', 'E', 'D', 'E', 'C#', 'D', 'E', 'F#', 'E', 'D', 'C#', 'D', 'B', 'C#', 'D', 'D', 'E', 'F#', 'G',
                'F#', 'E', 'F#', 'D', 'C#', 'D', 'B', 'D', 'C#', 'B', 'A', 'G', 'A', 'G', 'F#', 'G', 'A', 'B', 'C#',
                'D', 'B', 'D', 'C#', 'D', 'C#', 'B', 'C#', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G', 'F#', 'D', 'E', 'F#',
                'E', 'D', 'E', 'C#', 'D', 'E', 'F#', 'E', 'D', 'C#', 'D', 'B', 'C#', 'D', 'D', 'E', 'F#', 'G', 'F#',
                'E', 'F#', 'D', 'C#', 'D', 'B', 'D', 'C#', 'B', 'A', 'G', 'A', 'G', 'F#', 'G', 'A', 'B', 'C#', 'D', 'B',
                'D', 'C#', 'D', 'C#', 'B', 'C#', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'D', 'F#', 'A', 'A', 'B',
                'A', 'G', 'F#', 'F#', 'F#', 'G', 'F#', 'E', 'D', 'C', 'B', 'C', 'D', 'A', 'A', 'D', 'C', 'B', 'C', 'D',
                'C#', 'A', 'A', 'A', 'B', 'A', 'G', 'F#', 'F#', 'F#', 'G', 'F#', 'E', 'D', 'C', 'B', 'C', 'D', 'A', 'A',
                'D', 'C', 'B', 'C', 'D', 'C#', 'F#', 'F#', 'G', 'F#', 'E', 'E', 'F#', 'E', 'D', 'F#', 'D', 'B', 'A',
                'A', 'G', 'A', 'B', 'B', 'C#', 'B', 'A', 'A', 'G', 'A', 'B', 'B', 'A', 'B', 'C#', 'C#', 'B', 'C#', 'D',
                'D', 'E', 'D', 'C#', 'C#', 'D', 'C#', 'B', 'B', 'A', 'B', 'C#', 'C#', 'F#', 'E', 'D', 'D', 'E', 'G',
                'F#', 'F#', 'A', 'F#', 'F#', 'G', 'F#', 'G', 'E', 'A', 'E', 'C#', 'D', 'D', 'E', 'F#', 'D', 'C#', 'C#',
                'D', 'E', 'C#', 'B', 'B', 'C#', 'D', 'B', 'A', 'A', 'G', 'F#', 'E', 'B', 'G', 'F#', 'E', 'G', 'A', 'D',
                'E', 'F#', 'A', 'G', 'B', 'A', 'G', 'B', 'C#', 'A', 'G', 'F#', 'E', 'D', 'D', 'C#', 'D', 'A', 'A', 'A',
                'B', 'C#', 'A', 'B', 'D', 'E', 'D', 'D', 'C#', 'F#', 'E', 'D', 'C#', 'G', 'B', 'A', 'B', 'C#', 'A',
                'F#', 'E', 'D', 'F#', 'B', 'D', 'C#', 'B', 'C#', 'A', 'C#', 'A', 'F#', 'F#', 'G', 'F#', 'E', 'D', 'D',
                'D', 'E', 'D', 'C#', 'G', 'D', 'A', 'G', 'A', 'C#', 'D', 'F#', 'F#', 'G', 'F#', 'E', 'D', 'D', 'D', 'E',
                'D', 'C#', 'B', 'C', 'B', 'C', 'D', 'A', 'F#', 'D', 'C', 'B', 'C', 'A', 'C#', 'F#', 'A', 'A', 'B', 'A',
                'G', 'F#', 'F#', 'F#', 'G', 'F#', 'E', 'D', 'C', 'B', 'C', 'D', 'A', 'A', 'D', 'C', 'B', 'C', 'D', 'C#',
                'A', 'A', 'A', 'B', 'A', 'G', 'C#', 'B', 'A', 'A', 'G', 'A', 'A', 'G', 'E', 'A', 'A', 'E', 'F#', 'D',
                'E', 'D', 'G', 'F#', 'D', 'D', 'E', 'C#', 'G', 'A', 'A', 'G', 'F#', 'F#', 'E', 'D', 'F#', 'D', 'B', 'E',
                'E', 'A', 'A', 'D', 'D']


def calc_pitch_diff(pitch_1, pitch_2) -> int:
    return pitch.Pitch(pitch_1).pitchClass - pitch.Pitch(pitch_2).pitchClass


for melody in range(len(melody_array) - 1):
    for pitch_list_item in pitch_list:
        if melody_array[melody] == pitch_list_item:
            for pitch_list_item in pitch_list:
                if melody_array[melody + 1] == pitch_list_item:
                    pitch_diff = calc_pitch_diff(melody_array[melody], melody_array[melody + 1])
                    collected_array.loc[melody_array[melody], pitch_diff] += 1
