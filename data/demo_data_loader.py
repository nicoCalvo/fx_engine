import numpy as np
import bcolz
import csv

DEMO_PAIRS = ['eur_dol', 'dol_yua', 'ars_mex', 'bol_yen',
              'uru_ars', 'cub_dol', 'dol_uru', 'yen_eur']

LOOPS = 1 # Loops is the number of times to re read the csv and duplicate amount of data

LEN = int(len(list(open('hist.csv'))) * LOOPS)
FILE_NAME = 'hist.csv'


class DemoLoader(object):

    def load_data(self, count, pairs):
        row_index = LOOPS - count
        with open(FILE_NAME) as _file:
            reader = csv.reader(_file, delimiter=',')
            for i, row in enumerate(reader):
                _index = i - row_index
                self.write_data(pairs, row, _index)
        if count > 0:
            count -= 1
            self.load_data(count, pairs)

    def write_data(self, pairs, row, index):
        count = 0
        size = 4
        end = 6
        start = 2
        for pair in pairs:
            pair[index] = row[start:end]
            start = end + 1
            end = start + size

    def ingest(self):
        eur_dol = np.empty([LEN, 4])
        dol_yua = np.empty([LEN, 4])
        ars_mex = np.empty([LEN, 4])
        bol_yen = np.empty([LEN, 4])
        uru_ars = np.empty([LEN, 4])
        cub_dol = np.empty([LEN, 4])
        dol_uru = np.empty([LEN, 4])
        yen_eur = np.empty([LEN, 4])
        self.load_data(LOOPS, (eur_dol, dol_yua, ars_mex,
                               bol_yen, uru_ars, cub_dol, dol_uru, yen_eur))
        return bcolz.ctable(columns=[eur_dol, dol_yua, ars_mex, bol_yen, uru_ars,
                                   cub_dol, dol_uru, yen_eur], names=DEMO_PAIRS, mode='w', expectedlen=LEN)
