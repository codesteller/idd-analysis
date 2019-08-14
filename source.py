import cv2
import json
import numpy as np
import xml.dom.minidom as xml_parse
import xml.etree.ElementTree as ET
import os


image_dir = "dataset/IDD_Detection/JPEGImages"
label_dir = "dataset/IDD_Detection/Annotations"


class Database:
    def __init__(self, img_dir, lbl_dir):
        self.img_dir = img_dir
        self.lbl_dir = lbl_dir
        self.imgtypes = ["png", "jpeg", "jpg"]
        self.lbltypes = ["xml"]

        # Call methods
        self.make_dataset()

    @staticmethod
    def _get_images(file_dir, file_types):
        file_list = list()
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                for filetype in file_types:
                    if file.endswith(filetype):
                        file_list.append(os.path.join(root, file))

        return file_list

    def make_dataset(self):
        imgpaths = self._get_images(self.img_dir, self.imgtypes)
        lblpaths = self._get_images(self.lbl_dir, self.lbltypes)
        db_dict = dict()

        for lbl_path in lblpaths:
            tree = ET.parse(lbl_path)
            root = tree.getroot()
            basename = os.path.basename(lbl_path)

            xml_obj = xml_parse.parse(lbl_path)


_db = Database(image_dir, label_dir)

print(len(_db.imgpaths))
print(len(_db.lblpaths))

print("done")
