import os.path

#########################################################
# フォルダ作成
# def mkdir (folder) :
# folder : 作成するフォルダ名

#########################################################
# 各小節の座標を取得する
# def readbarpoint(folder, debug=False) :
# folder : 処理対象フォルダ名
# debug  : データ読み込み確認
# 
# 戻り値
# ２次元リスト [0 ~ [小節数,left,top,right,bottom], [小節数,left,top,right,bottom] … ]
_barpoint = 'point.txt'

#########################################################
# 各小節の開始時刻ファイルの読み込み
# def readtimestamp(folder, debug=False) :
# folder : 処理対象フォルダ名
# debug  : データ読み込み確認
# 
# 戻り値
# ２次元リスト [0 ~ [小節数, タイムスタンプ], [小節数, タイムスタンプ] … ]
_timestamp = 'index.txt'


#########################################################
# フォルダ作成
# def mkdir (folder) :
# folder : 作成するフォルダ名

def mkdir (folder) :
	if not os.path.exists(folder):
		os.mkdir(folder)


#########################################################
# 各小節の座標を取得する
# def readbarpoint(folder, debug=False) :
# folder : 処理対象フォルダ名
# debug  : データ読み込み確認
# 
# 戻り値
# ２次元リスト [0 ~ [小節数,left,top,right,bottom], [小節数,left,top,right,bottom] … ]

def readbarpoint(folder, debug=False) :
	datas = []
	path = folder + '/' + _barpoint
	with open(path) as f:
		str = f.read()
		buf = str.split('\n')
		for str in buf :
			if ',' in str:
				data = str.split(',')
				n = int(data[0])
				l = int(data[1])
				t = int(data[2])
				r = int(data[3])
				b = int(data[4])
				datas.append([n, l, t, r, b])

	if debug :
		for chk in datas :
			print(chk)

	return datas


#########################################################
# 各小節の開始時刻ファイルの読み込み
# def readtimestamp(folder, debug=False) :
# folder : 処理対象フォルダ名
# debug  : データ読み込み確認
# 
# 戻り値
# ２次元リスト [0 ~ [小節数, タイムスタンプ], [小節数, タイムスタンプ] … ]

def readtimestamp(folder, debug=False) :
	datas = []
	path = folder + '/' + _timestamp
	with open(path) as f:
		str = f.read()
		buf = str.split('\n')
		for str in buf :
			if ',' in str:
				scidx, stidx = str.split(',')
				cidx = int(scidx)
				tidx = float(stidx)
				tidx *= 1000
				tidx = int(tidx)
				datas.append([cidx, tidx])

	if debug :
		for chk in datas :
			print(chk)

	return datas
