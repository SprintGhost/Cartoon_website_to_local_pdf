from fpdf import FPDF
from PIL import Image
import os

COMBINED_NAME = 'combined.jpg'

def makePdf(pdfFileName, listPages):
    cover = Image.open(listPages[0])
    width, height = cover.size
    pdf = FPDF(unit = "pt", format = [width, height])
    for page in listPages:
        pdf.add_page()
        pdf.image(page, 0, 0)

    pdf.output(pdfFileName, "F")

def image_combine(image_list):
    images = [Image.open(x) for x in image_list]

    widths, heights = zip(*(i.size for i in images))

    heights = [height + 500 for height in heights]

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height),color="white")

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save(COMBINED_NAME)
    makePdf("combine.pdf", [COMBINED_NAME])  

# makePdf("result.pdf", ["./test_picture/" + imgFileName for imgFileName in os.listdir('./test_picture') \
#                        if imgFileName.endswith("png")])

image_combine(["./test_picture/" + imgFileName for imgFileName in os.listdir('./test_picture') \
                       if imgFileName.endswith("png")])


