# pip3 install ffmpeg-python
# brew install ffmpeg

import argparse
# import ffmpeg 
import subprocess
import lib.fileio as fileio
 

def main (infile, folder) :
	outfile = folder+'/music.wav'
	com = 'ffmpeg -i ' + infile + ' ' + outfile
	subprocess.call(com, shell=True)

	outfile = folder+'/movie.mp4'
	com = 'ffmpeg -i ' + infile + ' ' + outfile
	subprocess.call(com, shell=True)

	# stream = ffmpeg.input(infile) 
	# stream = ffmpeg.output(stream, outfile) 
	# ffmpeg.run(stream)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', type=str, required=True, help='変換対象動画ファイル')
	parser.add_argument('-f', type=str, default='out', help='出力フォルダ')
	args = parser.parse_args()

	infile = args.i
	folder = args.f

	fileio.mkdir(folder)
	main(infile, folder)
