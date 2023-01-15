import argparse
import cv2
import numpy as np
import sys

_folder = ''
_D = False

_nimg = ''
_nheight = 0
_nwidth  = 0

_mimg = ''
_mheight = 0
_mwidth  = 0

_bookline = []
# _bookline: 1次元データ[0~] 各音符行の小節を管理
_bookdata = []
# bookdata: 2次元データ[1~] [各小節の開始行数][各小節の終了行数][行数][打点数]

_music_bar = []


def getoverlapline() :
	lineidx = 0
	countmax = 0

	for mh in range(_mheight) :
		# mh: 音声認識ベースでの検索行
		if _D :
			print(f'基準 音楽行 [{mh}] ', end='')

		count = 0
		for nh in range(_nheight) :
			if mh + nh >= _mheight :
				if _D :
					print(f'音声データ終了 音声:{mh} 楽譜:{nh} ', end='')
				break
					
			if nh + mh >= _nheight :
				if _D :
					print(f'楽譜データ終了 音声:{mh} 楽譜:{nh} ', end='')
				break

			for m in range(88) :
				if _mimg[mh+nh][m][0] == _nimg[nh+mh][m][0] == 255 :
					count += 1

		if _D :
			print(f'オーバーラップ率:{count} ')

		if countmax < count :
			countmax = count
			lineidx = mh	

	return lineidx


# 楽譜をベースに検索
def search_book() :
	buf_no = 0
	buf_h = 0
	line_num = 0
	note_num = 0
	for h in range(_nheight) :
		str = ''
		for w in range(88, _nwidth, 1) :
			if _nimg[h][w][0] == 255 :
				str += '1'
			else :
				str += '0'
		no = int(str, 2)

		for w in range(88) :
			if _nimg[h][w][0] == 255 :
				note_num += 1

		_bookline.append(no)
		if buf_no != no or h == _nheight - 1:
			buf_no = no
			_bookdata.append([buf_h, h-1,line_num,note_num])
			buf_h = h
			line_num = 0
			note_num = 0
		line_num += 1


# 音をベースに検索

def search_music(diff) :
	nh = diff
	tar = 0
	mh = 0
	flag = False
	while mh < _mheight :
		if _D :
			print(f'基準 音楽行 [{mh}] {flag}')
		
		if nh >= _nheight :
			break

		if tar != _bookline[nh]:
			tar = _bookline[nh]

			tmp_mh = 0
			tmp_c = 0
			while mh < _mheight :
				if _D :
					print(f'検索対象 小節:{tar} 小節行:{nh} 音楽行:{mh} ', end='')
				
				if tmp_mh == 0 :
					tmp_mh = mh

				buf_mh = mh
				buf_nh = nh
				count = 0
				for ni in range(_bookdata[tar][0], _bookdata[tar][1]+1, 1) :
					if mh < _mheight :
						for w in range(88) :
							if _mimg[mh][w][0] == _nimg[ni][w][0] == 255 :
								count += 1
					mh += 1
					nh += 1
				if _D :
					print(f'一致数:{count} ', end='')
				
				if count == _bookdata[tar][3] :
					if flag == False :
						back = 0
						count = 0
						if buf_mh - 1 >= 0 :
							for w in range(88) :
								if _mimg[buf_mh][w][0] == 255 :
									back += 1
							for w in range(88) :
								if _mimg[buf_mh-1][w][0] == _mimg[buf_mh][w][0] == 255 :
									count += 1
							if back == count :
								buf_mh -= 1
								if _D :
									print('前行同じ', end='')

					_music_bar.append([tar, buf_mh])
					flag = True
					if _D :
						print(f'完全一致')
					break

				else :
					if tmp_c >= count :
						_music_bar.append([tar, tmp_mh])
						if _D :
							print(f'部分一致:{tmp_c} 初期[{tmp_mh}] ({_bookdata[tar][2]})')
							# mh = tmp_mh + _bookdata[tar][2]
							mh = tmp_mh + tmp_c
							tmp_mh = 0
							break
					else :
						flag = False

				tmp_c = count

				mh = buf_mh + 1
				nh = buf_nh
				if _D :
					print(f'flag:{flag}')

		if tar == _bookline[len(_bookline)-1] :
			break

def main() :
	diff = getoverlapline()
	if _D :
		print(f'最大値 diff:{diff}')
	
	search_book()
	if _D :
		print('_bookline')
		for i in range(len(_bookline)) :
			print(f'{[i]} {_bookline[i]}')
		print('_bookdata')
		for i in range(len(_bookdata)) :
			print(f'{[i]} {_bookdata[i]}')
	
	search_music(diff)
	if _D :
		print('_music_bar:')
		for data in _music_bar :
			print(data)

	mdatas = []
	mfp = open(_folder+'/music.txt', 'r')
	while True:
		data = mfp.readline()
		if data == '' :
			break
		time_idx, code = data.split(',')
		mdatas.append(time_idx)
	mfp.close()


	ifp = open(_folder+'/index.txt', 'w')
	for bar_idx, mline in _music_bar :
		if _D :
			print(f'{bar_idx} {mline}')
		time_idx = mdatas[mline]
		str = '{},{}\n'.format(bar_idx, time_idx)
		ifp.write(str)
	ifp.close()




if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', type=str, default='out', help='対象フォルダ')
	args = parser.parse_args()

	_folder = args.f
	_D = True

	_nimg = cv2.imread(_folder+'/notes.png')
	(_nheight, _nwidth, dummp) = _nimg.shape

	_mimg = cv2.imread(_folder+'/music.png')
	(_mheight, _mwidth, dummp) = _mimg.shape

	main()
