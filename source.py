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
            annotation_tree = ET.parse(lbl_path)
            annotation_obj = annotation_tree.getroot()
            labels_dict = self._get_annotation(annotation_obj)

            print("Here")


    @staticmethod
    def _get_annotation(annotation_obj):
        anno_obj = dict()
        object_list = list()
        counter = 0

        for iobj in annotation_obj:
            temp = list()
            if iobj.tag.lower() == "filename":
                anno_obj["filename"] = [iobj.text]
            if iobj.tag.lower() == "size":
                anno_obj["size"] = [iobj[0].text, iobj[1].text]
            if iobj.tag.lower() == "object":
                temp.append(counter)  # Box ID
                temp.append(iobj[0].text)  # Box Class
                temp.append(int(iobj[1][0].text))  # Box x0
                temp.append(int(iobj[1][1].text))  # Box y0
                temp.append(int(iobj[1][2].text))  # Box x1
                temp.append(int(iobj[1][3].text))  # Box y1
                counter += 1
                object_list.append(temp)
        print(counter)
        anno_obj["object_list"] = object_list
        for iobj in anno_obj["object_list"]:
            print(iobj)

        return anno_obj


_db = Database(image_dir, label_dir)

print(len(_db.imgpaths))
print(len(_db.lblpaths))

print("done")
