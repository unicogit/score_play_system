import argparse
import cv2
import numpy as np
import lib.note2number as note2number

D = True
# D = False


def main() :
	fp = open(_folder+'/23_wav.txt', 'r')
	# fp: 結果出力用ファイルポインタ

	notes = []

	while True :
		str = fp.readline()
		if str == '' :
			break
		str = str.rstrip('\n')
		buf = str.split(',')
		tmp = []
		for i in range(1, len(buf), 1) :
			tmp.append(buf[i])
		notes.append(tmp)
	fp.close()

	width = 88
	height = len(notes)
	if _D :
		print(f'w:{width} h:{height}')
	res = np.zeros((height, width, 1))
	note2number.drawNumber(res, notes)
	cv2.imwrite(_folder+'/music.png', res)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', type=str, default='out', help='対象フォルダ')
	args = parser.parse_args()

	_folder = args.f

	_D = True
	# _D = False

	main()

