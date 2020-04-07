import os
import sys
import csv
from core.domain.NetflixTitle import NetflixTitle


class LoadTitles(object):

    def load_from_csv_file(self, file_path, csv_separator):
        title_list = []

        with open(file_path, 'r', encoding="utf8") as file:
            # skip header
            next(file)

            reader = csv.reader(file)
            for row in reader:
                title = NetflixTitle(row[0], row[1], row[2], row[3], row[4],
                                     row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                title_list.append(title)

        return title_list
