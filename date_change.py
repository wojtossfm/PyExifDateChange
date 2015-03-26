# -*- coding: cp1250 -*-
import os
import datetime
import argparse

import pyexiv2


'''
Dependencies:
* http://tilloy.net/dev/pyexiv2/
'''


def modify_dates(source, change, test=False, verbose=False):
    for (root, dirs, files) in os.walk(source):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                metadata = pyexiv2.ImageMetadata(filepath)
                metadata.read()
            except:
                continue
            metadata['Exif.Image.DateTime'].value += change
            metadata['Exif.Photo.DateTimeOriginal'].value += change
            metadata['Exif.Photo.DateTimeDigitized'].value += change
            # print metadata['Exif.Photo.DateTimeOriginal'].value
            if test or verbose:
                print file, metadata['Exif.Photo.DateTimeOriginal'].value
            if not test:
                metadata.write()


def get_parser():
    parser = argparse.ArgumentParser(prog="date_change", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("target", help="directory containing images to modify")
    parser.add_argument("days", help="number of days", type=int, default=0)
    parser.add_argument("hours", help="number of hours", type=int, default=0)
    parser.add_argument("minutes", help="number of minutes", type=int, default=0)
    parser.add_argument("seconds", help="number of seconds", type=int, default=0)
    parser.add_argument("--subtract", action="store_true")
    parser.add_argument("--simulate", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    if args.subtract:
        change = datetime.timedelta(-args.days, hours=-args.hours, minutes=-args.minutes, seconds=-args.seconds)
    else:
        change = datetime.timedelta(args.days, hours=args.hours, minutes=args.minutes, seconds=args.seconds)
    if not os.path.isdir(args.target):
        raise IOError("Couldn't find target directory")
    modify_dates(args.target, change, args.simulate, args.verbose)
