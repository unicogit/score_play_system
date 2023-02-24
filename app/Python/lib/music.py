import matplotlib.pyplot as plt
import numpy as np

D = False

#########################################
# 波形データ
# fname : 保存するファイル名
# datas : 描画データ

def mkfig(fname, datas) :
	ext = "png"
	fname += "." + ext
	plt.figure(figsize=(30, 5))
	plt.plot(datas)
	plt.savefig(fname, format=ext, dpi=300)


#########################################
# 平均データ作成
# wav  : データ
# sf   : データサンプリング周波数
# rate : 平均化割合
# 
# 戻り値 : 平均化済 numpy.ndarray データ

def wav2mean(wav, sf, rate = 0.01) :
	br = int(sf * rate)

	mean = np.zeros(len(wav))
	diff = np.zeros(len(wav))

	buf = abs(wav[0])
	tmp = 0

	b = 0
	tr = 0
	for i in range(1, len(wav)) :
		buf += abs(wav[i])
		b += 1
		if b == br :
			b = 0
			ave = buf/br

			for j in range(br) :
				mean[tr*br + j] = ave

			if tr > 0 :
				for j in range(br) :
					diff[(tr-1)*br + j] = abs(ave - tmp)

			buf = 0
			tmp = ave
			tr += 1

	return br, mean, diff


#########################################
# 打点ポイント解析
# diff   : 差分データ
# inter  : 差分データインターバル
# pullup : 立ち上がりDB閾値
# skip   : 無効インターバル
#
# 戻り値 : 打点地点 numpy.ndarray データ

def diff2db(diff, inter, pullup=0.05, skip=5) :

	res = np.zeros(diff.size)

	s = 0
	for i in range(0, diff.size, inter) :
		# 無効インターバル区間内
		if s > 0 :
			s -= 1
			continue

		x = diff[i]

		# 立ち上がりが閾値以上
		if x >= pullup :
			if D == True :
				print(f'i:{i:4d} data:{x}')
			# for j in range(5) :
			# 	res[i+j] = 1
			res[i] = 1
			s = skip
			continue

	return res
