from devlogger import devlogger
import logging


class DBStats:
    """
    @brief:
    """
    def __init__(self, dbdict):
        self.logger = devlogger.Logger(logging.getLogger(__name__))
        self.db = dbdict
        self.class_list = list()

        # Method Calls
        self.stats = self.get_stats()

    def get_stats(self):
        print(len(self.db))
        stats_dict = dict()

        for idx in self.db:
            temp_dict = dict()
            ianno = self.db[idx]["annotation"]
            _class_list_per_image = list()
            for x in ianno:
                if x[1].lower() not in self.class_list:
                    self.class_list.append(x[1].lower())
                if x[1].lower() not in _class_list_per_image:
                    _class_list_per_image.append(x[1].lower())
            temp_dict["class_list"] = _class_list_per_image
            stats_dict[idx] = temp_dict

        return stats_dict
