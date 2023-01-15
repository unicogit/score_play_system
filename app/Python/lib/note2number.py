# pip3 install librosa

import librosa


def getNumber(tar) :
	notes = librosa.hz_to_note(librosa.cqt_frequencies(n_bins=88, fmin=librosa.note_to_hz('C1')))
	for i in range(len(notes)) :
		if notes[i] == tar :
			return i
	return 0

def drawNumber(img, datas) :
	for h in range(len(datas)) :
		for n in range(len(datas[h])) :
			note = datas[h][n]
			no = getNumber(note)
			img[h][no] = 255
