import librosa
import librosa.display
import argparse
import urllib.request
import pathlib
import cv2
import numpy as np
import sys
#import func
import copy
import re
import matplotlib.pyplot as plt
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
def main():
    filename = "../music/20.wav"
    y, sr = librosa.load(filename)
    y, index = librosa.effects.trim(y)

    window = 'hann'
    win_length = 1024
    hop_length = win_length // 256
    
    bins_per_octave = 12
    n_octaves = 7
    n_chroma = 12
    n_bins =bins_per_octave * n_octaves
    #chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=hop_length, fmin=librosa.note_to_hz('C1'), n_chroma=n_chroma, n_octaves=n_octaves)
    cqt_amplitude = np.abs(librosa.cqt(y=y,sr=sr, hop_length=hop_length, fmin=librosa.note_to_hz('C1'), n_bins=n_bins,bins_per_octave=bins_per_octave, window=window))
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr
=sr)
    syosetsu_num = tempo/4
    syosetsu_time = np.round(60/syosetsu_num,2)
    
    h_range = [1, 2] 
    weights = [1.0, 0.5]

    o_env = librosa.onset.onset_strength(y, sr=sr)**3
    times = librosa.times_like(o_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
    
    max_indices = np.argmax(cqt_amplitude, axis=0)
    notes = librosa.hz_to_note(librosa.cqt_frequencies(n_bins=n_bins, fmin=librosa.note_to_hz('C1'), bins_per_octave=bins_per_octave))
    notes2=np.array(notes)
    time = librosa.core.frames_to_time(np.arange(max_indices.shape[0]), sr=sr, hop_length=hop_length)
    daten_array = []
    time_array = []

    cnt = len(time)
    cqt_amplitude_t = cqt_amplitude.transpose()
    for daten in zip(times[onset_frames]):
        for t, max_index in zip(time, max_indices):
            result = re.findall('[+-]?[0-9]+\.?[0-9]*', str(daten))
            daten_time = float(result[0])
            if(np.array_equal(t, daten[0])):
                print(f'{t:.3f},{notes[max_index]}', end='')
                print()


if __name__ == '__main__':
    main()
