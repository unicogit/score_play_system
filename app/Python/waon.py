import librosa
import librosa.display
import argparse
import urllib.request
import pathlib
import numpy as np
import matplotlib.pyplot as plt


def main():
    y,sr = librosa.load('../music/20.wav')
    y, index = librosa.effects.trim(y)
    
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)


    hop_length = 512
    n_chroma = 12
    n_octaves = 7
    bins_per_octave = n_chroma*n_octaves
    chroma_cq = np.abs(librosa.cqt(y=y, sr=sr, hop_length=hop_length, fmin=librosa.note_to_hz('C1'), n_bins=84, bins_per_octave=7,window='hann'))
    notes =np.array(librosa.hz_to_note(librosa.cqt_frequencies(n_bins=bins_per_octave, fmin=librosa.note_to_hz('C1'), bins_per_octave=n_chroma)))
    time = librosa.core.frames_to_time(np.arange(chroma_cq.shape[1]), sr=sr, hop_length=hop_length)
    array = []
    end_frames = onset_frames[1:]
    end_frames = np.append(end_frames, chroma_cq.shape[1])
    for onset_frame, end_frame in zip(onset_frames, end_frames):
        chroma_cq_mean = np.mean(chroma_cq[:, onset_frame:end_frame], axis=1)
        chord_indices = np.argsort(chroma_cq_mean)[-1:-4:-1]
        current_notes = set(notes[chord_indices])
        onset_time = librosa.core.frames_to_time(onset_frame, sr=sr, hop_length=hop_length)
        end_time = librosa.core.frames_to_time(end_frame, sr=sr, hop_length=hop_length)
        for i in range(3):
            array.append(notes[chord_indices[i]])
        current_notes = set(notes[chord_indices])
        print(f'{onset_time:.3f},{array[0]},{array[1]},{array[2]}', end='')
        print()

if __name__ == '__main__':
    main()
