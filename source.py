import cv2
import json
import numpy as np
from database.create_db import Database


image_dir = "dataset/IDD_Detection/JPEGImages"
label_dir = "dataset/IDD_Detection/Annotations"

_db = Database(image_dir, label_dir)

print("Database created with {} images".format(len(_db.db)))

