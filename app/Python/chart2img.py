# pip3 install opencv-python

import argparse
import cv2
import copy
import numpy as np
import sys
import lib.fileio as fileio
import lib.func as func

_imgfname = ''
_folder = ''


_datas = [
		 ['', '', (0,255,0)],										# color! B:G:R
		 ['', '', (255,0,0)],
		 ['Gclef.png', 0.7, (192,64,0)],
		 ['Fclef.png', 0.7, (0,128,0)],
		 ['A.png', 0.6, (0,0,255)],
		 ['B.png', 0.6, (0,0,255)],
		 ['flat.png', 0.7, (64,64,0)],
		 ['sharp.png', 0.7, (128,192,0)],
		 ['natural.png', 0.7, (64,128,128)]
		]

_notes = [
		 [		'A6', 'G6', 'F6', 'E6', 'D6', 'C6',
		  'B5', 'A5', 'G5', 'F5', 'E5', 'D5', 'C5',
		  'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4',
		  'B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3',],
		 [									  'C5',
		  'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4',
		  'B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3',
		  'B2', 'A2', 'G2', 'F2', 'E2', 'D2', 'C2',
		  'B1', 'A1', 'G1', 'F1', 'E1',			   ]
		]

_convF2S = {'C':'B','D':'C♯','E':'D♯','F':'E','G':'F♯','A':'G♯','B':'A♯'}
_convS2S = {'C':'C♯','D':'D♯','E':'F','F':'F♯','G':'G♯','A':'A♯','B':'C'}

def main() : 
	ref = copy.deepcopy(_notes)
	# ref: 音階情報

	fp = open(_folder+'/res.txt', 'w')
	# fp: 結果出力用ファイルポインタ

	fpp = open(_folder+'/point.txt', 'w')
	# fp: 結果出力用ファイルポインタ

	im = cv2.imread(_imgfname)
	# im: 楽譜画像情報
	(height, width, dummp) = im.shape
	cv2.imwrite(_folder+'/chart.png', im)

	tmp = 'file:{}\nwidth:{}\nheight:{}\n'.format(_imgfname, height, width)
	fp.write(tmp)
	if _D :
		print('対象ファイル')
		print(tmp, end='')

	print('五線譜抽出 ...')
	res = func.getLine(im, _datas[0][2])								# 横線抽出
	# res: 白キャンパスに五線譜を緑色で書き込んだ画像

	pt = func.getStavePoint(res, _datas[0][2])							# 五線譜の座標を取得
	# pt: 2次元配列
	# 1次元目: 配列[0] 一番上ラインのy座標..[4] 一番下ラインのy座標
	if _D :
		print(pt)

	if len(pt) == 0 :
		print('五線譜認識失敗')
		sys.exit()

	print('小節抽出 ...')
	func.getLines(im, res, pt, _datas)									# 小節線抽出
	# resに小節線を青色で追記（五線譜上の縦線を抽出）

	diff5 = func.getLineDiff(pt[0])										# 線幅を取得
	# diff5: 五線譜の縦幅

	print('楽譜認識 ...')
	ratio = func.getImgRaito(diff5, _datas[2][0])						# テンプレートの倍率取得
	# ratio: テンプレートに対する対象画像の拡大率
	func.objmatch(ratio, _datas, im, res)								# オブジェクト検索

	idxno = 1
	# idxno: 小節番号格納用
	outstr = '\n'
	# outstr: 抽出音階格納用

	print('認識結果')
	# ペア or シングル 判別　###############################################
	mode = 'single'

	left = func.getLineLeft(res, pt[0], _datas[0][2])					# 五線譜左端
	right = func.getLineRight(res, pt[0], _datas[0][2])					# 五線譜右端
	nflag1, left = func.getClef(_datas, res, left, right, pt[0][2])		# 音記号取得
	# nflag1:0 ト音記号 nflg1:1 ヘ音記号

	if len(pt) > 1 :
		left = func.getLineLeft(res, pt[1], _datas[0][2])				# 五線譜左端
		right = func.getLineRight(res, pt[1], _datas[0][2])				# 五線譜右端
		nflag2, left = func.getClef(_datas, res, left, right, pt[1][2])	# 音記号取得
		# nflag2:0 ト音記号 nflg1:1 ヘ音記号

		if nflag1 == 0 and nflag2 == 1 :
			mode = 'double'

	info = []

	# シングルモード　#####################################################
	if mode == 'single' :
		for p in range(len(pt)) :
			left = func.getLineLeft(res, pt[p], _datas[0][2])
			right = func.getLineRight(res, pt[p], _datas[0][2])
			boxleft = left
			# boxleft: 小節の左座標

			nflag, left = func.getClef(_datas, res, left, right, pt[p][2])
			# nflag:0 ト音記号 nflg:1 ヘ音記号
			if _D :
				print(f'note:{nflag}')

			centers = func.getStaveLine(pt[p])
			# centers: 音階の検索対象センター座標

			boxtop = centers[0]
			# boxtop: 小節の上座標
			boxbottom = centers[len(centers)-1]
			# boxbottom: 小節の下座標

			# 調号抽出refに反映させる
			left = func.getMark(_datas, res, left, right, centers, 
								_notes, nflag, ref, _convF2S, _convS2S)
			# left: 調号記号検索終了時の座標
			if _D :
				print(ref)
			tar = copy.deepcopy(ref)
			# tar: 小節内音階情報

			while left < right :
				# 音符抽出
				music, left = func.getNotes(_datas, res, left, right, centers,
												_notes, nflag, ref, _convF2S, _convS2S, tar)
				# music: 抽出音階リスト
				mlen = len(music)
				if mlen > 0 :
					hoge = []
					hoge.append(idxno)
					hoge.append(music)
					info.append(hoge)
					outstr += music[0]
					for i in range(1, mlen, 1) :
						outstr += ',' + music[i]
					outstr += '\n'

				# 小節区切り検索
				bar, left = func.getBarLines(_datas, res, left, right, centers)
				# bar: 小節線を検出時 True
				if bar == True :
					cv2.rectangle(res, (boxleft, boxtop), (left, boxbottom), _datas[1][2], 3)
					
					idxnostr = '\n{},{},{},{},{}'.format(idxno,boxleft,boxtop,left,boxbottom)
					print(idxnostr + outstr, end='')
					fp.write(idxnostr + outstr)
					fpp.write(idxnostr)

					boxleft = left
					idxno += 1
					outstr = '\n'
					tar = copy.deepcopy(ref)
				else:
					if left == right :
						cv2.rectangle(res, (boxleft, boxtop), (left, boxbottom), _datas[1][2], 3)
						
						idxnostr = '\n{},{},{},{},{}'.format(idxno,boxleft,boxtop,left,boxbottom)
						print(idxnostr, end='')
						fp.write(idxnostr)
						fpp.write(idxnostr)

	else :
		for p in range(0, len(pt), 2) :
			left = func.getLineLeft(res, pt[p], _datas[0][2])
			right = func.getLineRight(res, pt[p], _datas[0][2])
			boxleft = left
			# boxleft: 小節の左座標

			centers = []
			centers1 = func.getStaveLine(pt[p])
			centers.append(centers1)
			centers2 = func.getStaveLine(pt[p+1])
			centers.append(centers2)
			# centers: 音階の検索対象センター座標

			boxtop = centers1[0]
			# boxtop: 小節の上座標
			boxbottom = centers2[len(centers2)-1]
			# boxbottom: 小節の下座標

			# 調号抽出refに反映させる
			left1 = func.getMark(_datas, res, left, right, centers1, 
								_notes, 0, ref, _convF2S, _convS2S)
			left2 = func.getMark(_datas, res, left, right, centers2, 
								_notes, 1, ref, _convF2S, _convS2S)
			tar = copy.deepcopy(ref)
			# tar: 小節内音階情報

			left = left1 if left1 < left2 else left2

			while left < right :
				# 音符抽出
				music, left = func.getNotesDouble(_datas, res, left, right, centers,
												_notes, ref, _convF2S, _convS2S, tar)
				# music: 抽出音階リスト
				mlen = len(music)
				if mlen > 0 :
					hoge = []
					hoge.append(idxno)
					hoge.append(music)
					info.append(hoge)
					outstr += music[0]
					for i in range(1, mlen, 1) :
						outstr += ',' + music[i]
					outstr += '\n'
					cv2.rectangle(res, (left, boxtop), (left+1, boxbottom), (0,192,192), 1)

				# 小節区切り検索
				bar, left = func.getBarLinesDouble(_datas, res, left, right, centers)
				# bar: 小節線を検出時 True
				if bar == True :
					cv2.rectangle(res, (boxleft, boxtop), (left, boxbottom), _datas[1][2], 3)
					
					idxnostr = '\n{},{},{},{},{}'.format(idxno,boxleft,boxtop,left,boxbottom)
					print(idxnostr + outstr, end='')
					fp.write(idxnostr + outstr)
					fpp.write(idxnostr)
					
					boxleft = left
					idxno += 1
					outstr = '\n'
					tar = copy.deepcopy(ref)

				else:
					if left == right :
						cv2.rectangle(res, (boxleft, boxtop), (left, boxbottom), _datas[1][2], 3)
						
						idxnostr = '\n{},{},{},{},{}'.format(idxno,boxleft,boxtop,left,boxbottom)
						print(idxnostr, end='')
						fp.write(idxnostr)
						fpp.write(idxnostr)

	cv2.imwrite(_folder+'/res.png', res)

	fp.close()
	fpp.close()

	# 結果画像作成
	func.mkresimg(_folder+'/notes.png', info)


	fpn = open(_folder+'/notes.txt', 'w')

	for idx, notes in info :
		outstr = str(idx) + ',' + str(notes) + '\n'
		fpn.write(outstr)

	fpn.close()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', type=str, required=True, help='楽譜ファイル')
	parser.add_argument('-f', type=str, default='out', help='対象フォルダ')
	args = parser.parse_args()

	_imgfname = args.i
	_folder = args.f

	fileio.mkdir(_folder)

	_D = True
	# _D = False

	main()
