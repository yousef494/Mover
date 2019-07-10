#!/usr/bin/env python3
import os
from os import path
import shutil
import csv
import argparse


class FileMover():

    SETTINGS = {}
    LOOKUP_TABLE = {}

    def __init__(self, csv_file, src, dst_folder, classes, opr):
        self.SETTINGS = {
            'csv_file': csv_file,
            'src': src,
            'dst': dst_folder,
            'opr': opr
        }
        for _class in classes:
            self.SETTINGS.update( { _class.strip() :  dst_folder + _class.strip() } )
        self.read_csv()

    def run(self):
        #iterate over all images (files) in the src dir
        src = self.SETTINGS['src']
        files = [i for i in os.listdir(src) if i.lower().endswith("jpg") and path.isfile(path.join(src, i))]
        for f in files:
            dst = self.lookUp(f)

            if not path.exists(dst):
                os.mkdir(dst)

            if self.SETTINGS['opr'] == 'copy':
                shutil.copy(path.join(src, f), dst)
            elif self.SETTINGS['opr'] == 'move':
                shutil.move(path.join(src, f), dst)
            else:
                print("Unrecognized operaion ({}). Either 'copy' or 'move'".format(self.SETTINGS['opr']))
                break

    def lookUp(self, key):        
        try:
            try:
                _class = self.LOOKUP_TABLE[key]
            except:
                return self.SETTINGS['dst'] + 'UNLABELED_FILE'
            dst = self.SETTINGS[_class]
            return dst
        except:
            return self.SETTINGS['dst'] + 'UNDEFINED_CLASS'
    
    def read_csv(self):
        filePath = self.SETTINGS['csv_file']
        with open(filePath, 'rt') as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in data:
                # name (key): class (value)
                self.LOOKUP_TABLE.update( { row[0] : row[1].strip() })


if __name__ == "__main__":
    #You can hard-code the defaults, so you don't have to pass them as parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--labels", help="CSV file which contains file-label pairs",
    default='/dir/to/labels.csv')

    parser.add_argument("-src", "--source", help="Source folder of the files",
    default='/dir/to/src/')
    
    parser.add_argument("-dst", "--destination", help="Destination folder which will have the sub-folders. Program will create sub-folders if does not exist.",
    default='/dir/to/dst/')

    parser.add_argument("-cls", "--classes", help="Possible classes (labels) e.g. 0,1",
    default='0,1')
    
    parser.add_argument("-opr", "--operation", help="Should the files copied or moved (copy/move)",
    default='copy')
    
    args = parser.parse_args()
    fileMover = FileMover(args.labels, args.source, args.destination, args.classes.split(','), args.operation)
    fileMover.run()