from pathlib import Path
import os
from database.create_db import Database
from database.get_stats import DBStats

import logging
from devlogger import devlogger


def main():
    # Create a logger
    logger = devlogger.Logger(logging.getLogger(__name__))

    # Specify dataset directory
    image_dir = os.path.join(str(Path.home()), "dataset/idd/IDD_Detection/JPEGImages")
    label_dir = os.path.join(str(Path.home()), "dataset/idd/IDD_Detection/Annotations")
    logger.log_i("Image Directory : {}".format(image_dir))
    logger.log_i("Annotation Directory : {}".format(label_dir))

    _db = Database(image_dir, label_dir)
    _stats = DBStats(_db.db)

    logger.log_i("Database created with {} images".format(len(_db.db)))


if __name__ == '__main__':
    main()
