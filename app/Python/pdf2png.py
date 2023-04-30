# pip3 install pdf2image
# pip3 install python-poppler
# brew install poppler (for mac)

from pathlib import Path
from pdf2image import convert_from_path
import sys

args = sys.argv
fname = args[1]
dpi = int(args[2])

def pdf_image(pdf_file, img_path, dpi=200):

    #pdf_file、img_pathをPathにする
    pdf_path = Path(pdf_file)
    image_dir = Path(img_path)

    # PDFをImage に変換(pdf2imageの関数)
    pages = convert_from_path(pdf_path, dpi)

    # 画像ファイルを１ページずつ保存
    for i, page in enumerate(pages):
        file_name = "{}_{:02d}.{}".format(pdf_path.stem,i+1,fmt)
        image_path = image_dir / file_name
        page.save(image_path, fmt)

if __name__ == "__main__":
    # PDFファイルのパス
    pdf_path = Path(fname)
    img_path = Path("./out")

    pdf_image(pdf_path, img_path, 'png', dpi)


