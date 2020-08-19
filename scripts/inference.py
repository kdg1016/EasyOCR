import easyocr
from PIL import ImageDraw


# Draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def main():

    # Create a reader to do OCR.
    reader = easyocr.Reader(['th', 'en'])

    # Doing OCR. Get bounding boxes.
    bounds = reader.readtext("../examples/thai.jpg")

    print(bounds)

    pass


if __name__ == "__main__":
    main()