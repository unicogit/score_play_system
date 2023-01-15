# # conda create -n music python=3.7
# # pip3 install librosa
# # pip3 install matplotlib

import argparse
import cv2
import librosa
import librosa.display
import numpy as np
import soundfile
import sys
import time
import lib.fileio as fileio
import lib.music as musicfunc
import lib.note2number as note2number

D = True
# # D = False

threshold = 1
syousetu = 0
syousetu_time = 0
flag = 0
break_flag = 0

note1 = 0
note2 = 0

parser = argparse.ArgumentParser()
parser.add_argument('-int', type=float, default='0.01', help='解析間隔 0.01')
parser.add_argument('-th', type=float, default='0.05', help='打点閾値 0.05')
parser.add_argument('-keep', type=float, default='0.1', help='打点保持 0.1')
parser.add_argument('-f', type=str, default='out', help='結果出力フォルダ')
parser.add_argument('-m', type=str, help='音楽データ')
args = parser.parse_args()

# 対象フォルダ
folder = args.f

print('データ読込 ...')
y, sf = librosa.load(folder+'/music.wav', sr=None, mono=False)
wav = y
if y.ndim > 1 :
	wav = y[0][:]

if D :
	soundfile.write(folder+'/mono.wav', wav, sf)

n_bins = 88

# 音楽コード配列生成
notes = librosa.hz_to_note(librosa.cqt_frequencies(n_bins=n_bins, fmin=librosa.note_to_hz('C1')))

# 定Q変換
rate = 0.01
hop_length = int(sf * rate)
cqt = np.abs(librosa.cqt(wav, sr=sf, hop_length=hop_length, fmin=librosa.note_to_hz('C1'), n_bins=n_bins))
n, datas = cqt.shape

print(n)
print(datas)
s2 = []
s3 = []
# 配列の要素の最大値取得
max_indices = np.argmax(cqt, axis=0)
# 楽譜データ読み込み
# f = open(folder+"notes.txt","r")
with open(folder+"/notes.txt","r",encoding="utf-8") as f:
	s = f.readlines()
	for v in range(len(s)):
		table = s[v].maketrans({
		'[': '', #左が置換したい文字、右が新しい文字。
		']': '', #左が置換したい文字、右が新しい文字。
		"\'": '', #左が置換したい文字、右が新しい文字。
		"\n": '',
		" ":'',
		})
		s2.append(s[v].translate(table))
for h in range(len(s)):
	s3.append(s2[h].split(","))
res = np.zeros((n_bins, datas, 3))
for k in range(len(s3)): #比較元取得 
	print(s3[k])
	cnt = 0
	flag = 0
		# for l in range(len(s3[k])):
		# 	flag = 0
		# 	print(s3[k][l])
	for i in range(5, datas, 1):
		note1 = 0
		note2 = 0
		flag = 0
		for j in range(n):
			# print(s3[k][2])
			if(len(s3[k])>2):
				if(i*rate > syousetu_time):
					# print(syousetu_time)
					if (notes[j]==s3[k][2]):
						if(cqt[j][i] >= threshold):
							flag = 1
							note1 = i*rate
						elif(flag == 1 and cqt[j][i] <= threshold):
							flag = 0
							# print("flagoff")
							cnt = cnt + 1
							break
					if (notes[j]==s3[k][1]):
						# print(notes[j])
						if(cqt[j][i] >= threshold):
							flag = 1
							note2 = i*rate
							# print("flagon")
						elif(flag == 1 and cqt[j][i] <= threshold):
							flag = 0
							# print("flagoff")
							cnt = cnt + 1
							break
						# print(f'{notes[j]},{i*rate:.3f},{cqt[j][i]}',end ="")
						# print()
						# if(cnt == 1 and flag == 1 and i*rate > syousetu_time):
						# 	syousetu_time1 = i*rate
						# 	print(syousetu_time)
						# 	break_flag = 1
						# 	break
						# if(cnt == 2 and flag == 1 and i*rate > syousetu_time):
						# 	syousetu_time2 = i*rate
						# 	print(syousetu_time2)
						# 	break_flag = 1
						# 	break
			else:
				for i in range(5, datas, 1):
					for j in range(n):
						if (notes[j]==s3[k][1]):
							if(cqt[j][i] >= threshold):
								flag = 1
								note1 = i*rate
							elif(cqt[j][i] <= threshold):
								flag = 0
							# print(f'{notes[j]},{i*rate:.3f},{cqt[j][i]}',end ="")
							# print()
							# if(s3[k][0]!=syousetu and i*rate > syousetu_time and flag == 1):
							# 	syousetu = s3[k][0]
							# 	# syousetu_time = i*rate
							# 	print(f'{notes[j]},{i*rate:.3f},{cqt[j][i]}',end ="")
							# 	print()
							# 	print(f'{syousetu}小節目:{syousetu_time:.2f}')
							# 	print()
							# 	break
		if(note1>note2):
			syousetu_time = note1
			if(flag == 1 and s3[k][0]!=syousetu):
			# print(f'{s3[k][0]},{syousetu}')
				syousetu = s3[k][0]
				if(note1>note2):
					syousetu_time = note1
				else:
					syousetu_time = note2
				print(f'{notes[j]},{i*rate:.3f},{cqt[j][i]}',end ="")
				print()
				print(f'{syousetu}小節目:{syousetu_time:.2f}')
				print()
		else:
			syousetu_time = note2
			if(flag == 1 and s3[k][0]!=syousetu):
			# print(f'{s3[k][0]},{syousetu}')
				syousetu = s3[k][0]
				if(note1>note2):
					syousetu_time = note1
				else:
					syousetu_time = note2
				print(f'{notes[j]},{i*rate:.3f},{cqt[j][i]}',end ="")
				print()
				print(f'{syousetu}小節目:{syousetu_time:.2f}')
				print()
			


cv2.imwrite("debug.png", res)