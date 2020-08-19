import argparse
import os
import sys
import easyocr
import PIL
from PIL import ImageDraw


_this_folder_ = os.path.dirname(os.path.abspath(__file__))
_this_basename_ = os.path.splitext(os.path.basename(__file__))[0]

# Draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def main(args):

    # Create a reader to do OCR.
    reader = easyocr.Reader(lang_list=args.lang, gpu=args.gpu)

    img = PIL.Image.open(args.file)

    # Doing OCR. Get bounding boxes.
    bounds = reader.readtext(args.file, detail=args.detail)

    print("[Text recog.] results :")
    for line in bounds:
        print(line)

    res_img = draw_boxes(img, bounds)
    res_img.show()

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