from os.path import join
from os import walk
import os
import shutil
from exif import Image
from classes.ImageObj import ImageObj
from tqdm import tqdm
import re
import csv


MONTHS = {
        "01": "01_Janvier",
        "02": "02_Fevrier",
        "03": "03_Mars",
        "04": "04_Avril",
        "05": "05_Mai",
        "06": "06_Juin",
        "07": "07_Juillet",
        "08": "08_Aout",
        "09": "09_Septembre",
        "10": "10_Octobre",
        "11": "11_Novembre",
        "12": "12_Décembre"
    }


def check_dir(path_name):
    """
    Checks if designed dir exists
    :param path_name: dir path to check
    :return: None
    """
    if not os.path.exists(path_name):
        os.makedirs(path_name, exist_ok=True)

def get_month(number):
    """
    Returns the month from the corresponding key
    :param number: month number key
    :return:
    """
    if number in MONTHS:
        return MONTHS[number]
    else:
        return "unclassified"


class PicOrdener:
    """
    All the logic for retrieving images, get metadatas and copying images in target directory, organized by year and
    month
    :param start_dir: directory from which the program will search pictures
    :param target_dir: dir where pictures will be copy
    :param extension[]: file extension we want to keep

    :method search_for_images: uses python walk() to list all files
    :method get_image_name: parse the given path of image to only keep name
    :method search_for_metadata: given the image path, uses exif modules to get the datetime
    :method copy_image: goes through all images, parse year and month to create path to finally copy image
    """

    # File extension accepted
    extension = ["jpg", ]

    # Arrays for images paths found
    images_list = []
    all_path = []

    def __init__(self, start_dir, target_dir):
        self.start_dir = start_dir
        self.target_dir = target_dir

    def search_for_images(self):
        """
        Search for all images in dirs and subdirs
        :return: None
        """
        print("Searching for images ...")

        for (dirpath, dirnames, filenames) in (walk(self.start_dir)):
            # Get the full path of the image for later copy
            # Iterates through filenames  parse the name to check the file extension
            files_path = [join(dirpath, img) for img in filenames if os.path.split(img)[-1].split(".")[-1].lower() in self.extension]

            self.all_path.extend(files_path)

    def get_image_name(self):
        """
        Split the path to only recover file name (useful for file copying)
        :return: None
        """
        for index, images in enumerate(self.all_path):
            # Parse path to "/" to only get the image name
            # Instantiate a ImageObj to store data
            self.images_list.append(ImageObj(self.all_path[index], self.all_path[index].split("/")[-1]))

    def search_for_metadata(self):
        """
        Search for the photo datetime it was taken
        :return: None
        """

        # Uses tqdm for fancy terminal output
        for img in tqdm(self.images_list, desc="Retrieving datetime"):

            with open(img.path, 'rb') as img_file:
                img_meta = Image(img_file)

                # Given all exif keys, we need the "datetime" one
                # Add the metadata to the corresponding ImageObj instance
                try :
                    img.meta = img_meta.get("datetime")
                except:
                    pass

    def save_to_csv(self):
        """
        Write all metadta to csv in order to gain time if prpgram crash durinf copying
        :return: None
        """
        print("Saving to CSV")

        with open("metadate.csv", 'w') as f:
            writer = csv.writer(f)

            for images in self.images_list:
                writer.writerow(images.get_img())

    def copy_images(self):
        """
        Parse the metadata to get year and month, create the corresponding dir if necessary and finnaly copy the image
        :return:
        """
        for images in tqdm(self.images_list, desc="Copying images"):

            try:
                # Parsing metadata (format : YYYY:MM:DD)
                year, month = images.meta.split(":")[0], images.meta.split(":")[1]
                verbose_month = get_month(month)

                if re.match("^\d{4}$", year):

                    # Concatenate the path
                    dated_path = os.path.join(year, verbose_month)
                    full_path = os.path.join(self.target_dir, dated_path)

                    check_dir(full_path)

                    # Copy image
                    shutil.copyfile(images.path, os.path.join(full_path, images.name))

                else:
                    raise AttributeError

            # If we can't find metadata, then we create an unclassified folder to store them
            except (AttributeError, IndexError):
                check_dir("copy/unclassified")

                shutil.copyfile(images.path, os.path.join("copy/unclassified", images.name))

            except:
                pass

        print("All done !")

    def start_classification(self):
        self.search_for_images()
        self.get_image_name()
        self.search_for_metadata()
        self.copy_images()
