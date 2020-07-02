import os
import cv2
import math

from PIL import Image, ImageFont, ImageDraw, ImageStat

from datetime import datetime


def annotate_image(infile_path, infile_name, outfile_dir, outfile_name):

    outfile = outfile_dir + "/" + outfile_name

    # Check if already existing
    if os.path.isfile(outfile):
        return outfile

    timestr = infile_name[:-4]
    timestamp = datetime.strptime(timestr, '%Y_%m_%d_%H_%M_%S')

    img = Image.open(infile_path)
    stat = ImageStat.Stat(img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeMono.ttf", 72)

    r, g, b = stat.mean
    brightness = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

    if brightness < 5.0:
        return None

    x, y = (50, 50)
    padding = 5
    text = timestamp.strftime('%c')

    w, h = font.getsize(text)
    draw.rectangle((x - padding, y - padding, x + w + padding, y + h + padding), fill="black")
    draw.text((x, y), text, (255, 255, 255), font=font)

    img.save(outfile)

    return outfile


if __name__ == '__main__':

    input_dir = "/path/to/uploaded/image/folder"
    output_dir = "/path/to/folder/for/annotated/images"
    output_video = "/path/to/save/output/video.mp4"

    img_list = []

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                infile_path = input_dir + "/" + file
                outfile_name = file[:-4] + "_annotated.jpg"
                output = annotate_image(infile_path, file, output_dir, outfile_name)
                if output:
                    img_list.append(output)

    img = cv2.imread(img_list[0])
    height, width, layers = img.shape
    im_size = (width, height)

    video_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'avc1'), 24, im_size)

    for frame in sorted(img_list):
        img = cv2.imread(frame)
        video_writer.write(img)

    video_writer.release()
