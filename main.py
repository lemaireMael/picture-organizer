from classes.PicOrdener import PicOrdener
import sys

if __name__ == '__main__':

    start_dir = sys.argv[1]
    copy_dir = sys.argv[2]

    photos = PicOrdener(start_dir, copy_dir)
    photos.start_classification()



