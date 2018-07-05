import argparse
import datetime
from qread.scan import scan

def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-he", "--height", type=int, default=500,
    	help="frame height in pixels")
    ap.add_argument("-o", "--output", type=str, default="{}.csv".format(datetime.date.today()),
    	help="path to output CSV file containing barcodes")
    ap.add_argument("-t", "--timeout", type=int, default=3,
    	help="timeout after detection in seconds")
    ap.add_argument("-v", "--video", type=bool, default=False,
    	help="boolean whether video will be shown or not")
    ap.add_argument("-w", "--width", type=int, default=500,
        help="frame width in pixels")
    args = vars(ap.parse_args())
    scan(args)

if __name__ == '__main__':
    main()
