import argparse
import os
import sys
import easyocr
import PIL
import cv2
import numpy as np
from PIL import ImageDraw
from easyocr import general_utils as g_utils
from easyocr import craft_file_utils as f_utils


_this_folder_ = os.path.dirname(os.path.abspath(__file__))
_this_basename_ = os.path.splitext(os.path.basename(__file__))[0]


def main(args):

    # Create a reader to do OCR.
    reader = easyocr.Reader(lang_list=args.lang, gpu=args.gpu)

    # Read image
    img = g_utils.imread(args.file)

    # Doing OCR. Get bounding boxes.
    results = reader.readtext(args.file, detail=args.detail)

    print("[Text recog.] results :")
    for line in results:
        print(line)

    f_utils.saveResult('result.png', img, reader.bboxes, dirname='./Output/', texts=reader.texts)
    pass

def parse_arguments(argv):
    parser = argparse.ArgumentParser(description="Process EasyOCR.")
    parser.add_argument(
        "-l",
        "--lang",
        nargs='+',
        required=True,
        type=str,
        help="for languages",
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        type=str,
        help="input file",
    )
    parser.add_argument(
        "--detail",
        type=int,
        choices=[0, 1],
        default=1,
        help="simple output (default: 1)",
    )
    parser.add_argument(
        "--gpu",
        type=bool,
        choices=[True, False],
        default=True,
        help="Using GPU (default: True)",
    )

    args = parser.parse_args(argv)

    return args


SELF_TEST_ = True
IMG_PATH = "./examples/chinese.jpg"


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.extend(["--lang", 'ch_sim','en'])
        sys.argv.extend(["--file", IMG_PATH])
        sys.argv.extend(["--detail", '1'])
        sys.argv.extend(["--gpu", 'True'])
    else:
        sys.argv.extend(["--help"])

    main(parse_arguments(sys.argv[1:]))