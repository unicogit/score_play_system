# pip3 install opencv-python

import cv2
import numpy as np
import copy
import lib.note2number as note2number

D = False
# D = True

dataOffSet = 2

#########################################################
# 横線抽出
#

def getLine (im, color) :
	width  = im.shape[1]
	height = im.shape[0]
	blank = np.zeros((height, width, 3))
	
	for j in range (height) :
		start = 0
		for i in range (width) :
			blank[j, i] = [255, 255, 255]
			r = im[j, i, 2]

			if r < 150 :
				if start == 0 :
					start = i

			else :
				if start > 0 :
					if (i-start) > (width / 2) :
						for k in range(start, i, 1) :
							blank[j, k] = color
					start = 0
	return blank


#########################################################
# １次元配列 -> ２次元配列 変換
#

def convert_1d_to_2d(l, cols):
	return [l[i:i + cols] for i in range(0, len(l), cols)]


#########################################################
# 五線譜の座標を取得
#

def getStavePoint(im, color) :
	width  = im.shape[1]
	height = im.shape[0]

	empty = []
	buf = 0
	for j in range (height) :
		b, g, r = im[j, int(width/2)]

		if r == color[2] and g == color[1] and b == color[0]:
			if buf == 0 :
				buf = j
		else :
			if buf > 0 :
				y = int((j-1 + buf) / 2)
				empty.append(y)
				buf = 0

	return convert_1d_to_2d(empty, 5)


#########################################################
# 小節線抽出

def getLines(im, res, pt, datas) :
	for p in range(0, len(pt), 1) :
		left  = getLineLeft(res, pt[p], datas[0][2])
		right = getLineRight(res, pt[p], datas[0][2])

		for w in range(left, right, 1) :
			flag = True
			for h in range(pt[p][0], pt[p][4], 1) :
				r = im[h, w, 2]
				if r > 150 :
					flag = False
			
			if flag == True:
				for x in range(pt[p][0], pt[p][4], 1) :
					res[x, w] = datas[1][2]


#########################################################
# 五線譜の幅を取得
#

def getLineDiff(datas) :
	diff = datas[4] - datas[0]
	return diff


#########################################################
# テンプレートの倍率取得
#

def getImgRaito(height, fname) :
	im = cv2.imread('./img/'+fname)
	h = im.shape[0]
	raito = height / h
	return raito


#########################################################
# マッチ
#

def match(img, template, threshold) :
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	# 処理対象画像に対して、テンプレート画像との類似度を算出する
	res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

	# 類似度の高い部分を検出する
	loc = np.where(res >= threshold)

	return loc


#########################################################
# オブジェクト検索
#

def objmatch(ratio, datas, im, res) :
	for i in range(dataOffSet, len(datas), 1) :
		fname = datas[i][0]
		th    = datas[i][1]
		color = datas[i][2]

		buf = cv2.imread('./img/' + fname)
		width  = buf.shape[1]
		height = buf.shape[0]
		w = int(width*ratio)
		h = int(height*ratio)
		tar = cv2.resize(buf, (w, h))
		loc = match(im, tar, th)
		for xy in zip(*loc[::-1]):
			d = int(h*0.4)
			cv2.rectangle(res, (xy[0], xy[1]+d), (xy[0]+w, xy[1]+h-d), color, -1)


#########################################################
# 五線譜左端
#

def getLineLeft(res, pt, color) :
	width = res.shape[1]
	for w in range(width-1) :
		for l in range(5) :
			h = pt[l]
			b, g, r = res[h, w]
			if r == color[2] and g == color[1] and b == color[0]:
				return w
	return w


#########################################################
# 五線譜右端
#

def getLineRight(res, pt, color) :
	width = res.shape[1]
	for w in range(width-1, 0, -1) :
		for l in range(5) :
			h = pt[l]
			b, g, r = res[h, w]
			if r == color[2] and g == color[1] and b == color[0]:
				return w
	return w


#########################################################
# 音記号取得
#
def getClef(datas, res, left, right, center) :
	for c in range(2) :
		flag = False
		color = datas[c+dataOffSet][2]
		for w in range(left, right, 1) :
			b, g, r = res[center, w]
			if r == color[2] and g == color[1] and b == color[0]:
				flag = True
			else :
				if flag == True :
					return c, w


#########################################################
# 楽譜 検索座標取得
#
def getStaveLine(pt) :
	l1 = pt[0]
	l2 = pt[1]
	l3 = pt[2]
	l4 = pt[3]
	l5 = pt[4]
	df = int((l2 - l1)/2)
	d = l5 - l1
	lines = [l1-df-d, l1-d, l2-df-d, l2-d, l3-df-d, l3-d, l4-df-d, l4-d, l5-df-d,
			          l1,   l2-df,   l2,   l3-df,   l3,   l4-df,   l4,   l5-df,
			          l1+d, l2-df+d, l2+d, l3-df+d, l3+d, l4-df+d, l4+d, l5-df+d, l5+d, l5+d+df]
	return lines


#########################################################
# 色情報
#
def getMarkColor(datas, fname) :
	for i in range(len(datas)) :
		if datas[i][0] == fname :
			return datas[i][2]


#########################################################
# 調号抽出
#
def getMark(datas, res, left, right, centers, notes, note, ref, convF2S, convS2S) :
	Acolor = getMarkColor(datas, 'A.png')
	Bcolor = getMarkColor(datas, 'B.png')
	Fcolor = getMarkColor(datas, 'flat.png')
	Scolor = getMarkColor(datas, 'sharp.png')
	Ncolor = getMarkColor(datas, 'natural.png')
	
	for w in range(left, right, 1) :
		for i in range(len(centers)) :
			h = centers[i]
			rb, rg, rr = res[h, w]
			code = notes[note][i]

			if rr == Acolor[2] and rg == Acolor[1] and rb == Acolor[0] :
				if D :
					print('音符 検出')
				return w
			
			if rr == Bcolor[2] and rg == Bcolor[1] and rb == Bcolor[0] :
				if D :
					print('音符 検出')
				return w
			
			if rr == Ncolor[2] and rg == Ncolor[1] and rb == Ncolor[0] :
				if D :
					print('ナチュラル 検出')
				return w

			if rr == Fcolor[2] and rg == Fcolor[1] and rb == Fcolor[0] :
				if D :
					print(f'{code} フラット 検出')
				for k in range(len(notes[note])) :
					buf = notes[note][k]
					if code[0] == buf[0] :
						ref[note][k] = convF2S[code[0]] + buf[1]
			
			elif rr == Scolor[2] and rg == Scolor[1] and rb == Scolor[0] :
				if D :
					print(f'{code} シャープ 検出')
				for k in range(len(notes[note])) :
					buf = notes[note][k]
					if code[0] == buf[0] :
						ref[note][k] = convS2S[code[0]] + buf[1]

	return right


def Line2NA(datas, res, width, centers) :
	top = centers[0]
	bottom = centers[len(centers)-1]
	for i in range(top, bottom, 1) :
		rb, rg, rr = res[i, width]
		if rr == datas[1][2][2] and rg == datas[1][2][1] and rb == datas[1][2][0] :
			res[i, width] = (255, 255, 255)


#########################################################
# 音取得
#
def getNotes(datas, res, left, right, centers, notes, note, ref, convF2S, convS2S, dsp) :
	Acolor = getMarkColor(datas, 'A.png')
	Bcolor = getMarkColor(datas, 'B.png')
	Fcolor = getMarkColor(datas, 'flat.png')
	Scolor = getMarkColor(datas, 'sharp.png')
	Ncolor = getMarkColor(datas, 'natural.png')

	eflag = False
	result = []
	for w in range(left, right, 1) :
		cflag = False
		for i in range(len(centers)) :
			h = centers[i]
			rb, rg, rr = res[h, w]
			
			code = dsp[note][i]
			if rr == Acolor[2] and rg == Acolor[1] and rb == Acolor[0] :
				cflag = True
				eflag = True
				if code in result :
					pass
				else :
					result.append(code)
			
			elif rr == Bcolor[2] and rg == Bcolor[1] and rb == Bcolor[0] :
				cflag = True
				eflag = True
				if code in result :
					pass
				else :
					result.append(code)
			
			elif rr == Ncolor[2] and rg == Ncolor[1] and rb == Ncolor[0] :
				if D :
					print('ナチュラル 検出')
				dsp[note][i] = notes[note][i]

			elif rr == Fcolor[2] and rg == Fcolor[1] and rb == Fcolor[0] :
				if D :
					print(f'{code} フラット 検出')

				if dsp[note][i][1] == '♯' :
					if D :
						print(f'適応済み')
				else :
					dsp[note][i] = convF2S[code[0]] + dsp[note][i][1]

			elif rr == Scolor[2] and rg == Scolor[1] and rb == Scolor[0] :
				if D :
					print(f'{code} シャープ 検出')

				if dsp[note][i][1] == '♯' :
					if D :
						print(f'適応済み')
				else :
					dsp[note][i] = convS2S[code[0]] + dsp[note][i][1]

			elif rr == datas[1][2][2] and rg == datas[1][2][1] and rb == datas[1][2][0] :
				cflag = True

		if eflag == True :
			if cflag == True :
				Line2NA(datas, res, w+1, centers)

			else :
				return result, w

	return result, right


#########################################################
# 音取得
#
def getNotesDouble(datas, res, left, right, centers, notes, ref, convF2S, convS2S, dsp) :
	Acolor = getMarkColor(datas, 'A.png')
	Bcolor = getMarkColor(datas, 'B.png')
	Fcolor = getMarkColor(datas, 'flat.png')
	Scolor = getMarkColor(datas, 'sharp.png')
	Ncolor = getMarkColor(datas, 'natural.png')

	eflag = False
	result = []
	for w in range(left, right, 1) :
		cflag = False
		for note in range(2) :
			st = 0 if note == 0 else 2
			for i in range(st, len(centers[0]), 1) :
				h = centers[note][i]
				rb, rg, rr = res[h, w]
				
				code = dsp[note][i]
				if rr == Acolor[2] and rg == Acolor[1] and rb == Acolor[0] :
					cflag = True
					eflag = True
					if code in result :
						pass
					else :
						result.append(code)
				
				elif rr == Bcolor[2] and rg == Bcolor[1] and rb == Bcolor[0] :
					cflag = True
					eflag = True
					if code in result :
						pass
					else :
						result.append(code)
				
				elif rr == Ncolor[2] and rg == Ncolor[1] and rb == Ncolor[0] :
					if D :
						print('ナチュラル 検出')
					dsp[note][i] = notes[note][i]

				elif rr == Fcolor[2] and rg == Fcolor[1] and rb == Fcolor[0] :
					if D :
						print(f'{code} フラット 検出')

					if dsp[note][i][1] == '♯' :
						if D :
							print(f'適応済み')
					else :
						dsp[note][i] = convF2S[code[0]] + dsp[note][i][1]

				elif rr == Scolor[2] and rg == Scolor[1] and rb == Scolor[0] :
					if D :
						print(f'{code} シャープ 検出')

					if dsp[note][i][1] == '♯' :
						if D :
							print(f'適応済み')
					else :
						dsp[note][i] = convS2S[code[0]] + dsp[note][i][1]

				elif rr == datas[1][2][2] and rg == datas[1][2][1] and rb == datas[1][2][0] :
					cflag = True

		if eflag == True :
			if cflag == True :
				Line2NA(datas, res, w+1, centers[0])
				Line2NA(datas, res, w+1, centers[1])

			else :
				if D :
					print(f'endpoint:{w} {result}')
				return result, w

	return result, right


#########################################################
# 区切り線取得
#

def getBarLines(datas, res, left, right, centers) :
	flag = False
	for w in range(left, right, 1) :
		h = centers[int(len(centers)/2)]
		rb, rg, rr = res[h, w]
		if rr == datas[1][2][2] and rg == datas[1][2][1] and rb == datas[1][2][0] :
			flag = True
		else :
			if flag == True :
				return True, w

		for i in range(len(centers)) :
			h = centers[i]
			rb, rg, rr = res[h, w]

			
			for j in range(dataOffSet, len(datas), 1) :
				db, dg, dr = datas[j][2]
				if rr == dr and rg == dg and rb == db :
					Line2NA(datas, res, w, centers)
					return False, w
	
	return flag, right


#########################################################
# 区切り線取得
#

def getBarLinesDouble(datas, res, left, right, centers) :
	flag = False
	for w in range(left, right, 1) :
		for note in range(2) :
			h = centers[note][int(len(centers[0])/2)]
			rb, rg, rr = res[h, w]
			if rr == datas[1][2][2] and rg == datas[1][2][1] and rb == datas[1][2][0] :
				flag = True
			else :
				if flag == True :
					return True, w

			for i in range(len(centers[0])) :
				h = centers[note][i]
				rb, rg, rr = res[h, w]

				
				for j in range(dataOffSet, len(datas), 1) :
					db, dg, dr = datas[j][2]
					if rr == dr and rg == dg and rb == db :
						Line2NA(datas, res, w, centers[0])
						Line2NA(datas, res, w, centers[1])
						return False, w
	
	return flag, right


#########################################################
# 結果画像作成
#

def mkresimg(fname, info) :
	width = 88 + 8
	height = len(info)

	res = np.zeros((height, width, 1))
	datas = [notes for idx, notes in info]

	note2number.drawNumber(res, datas)

	for h in range(height) :
		str = format(info[h][0], 'b')
		for i in range(len(str)) :
			w = width -1 - i
			if str[len(str)-1-i] == '1' :
				res[h][w] = 255

	cv2.imwrite(fname, res)
