import argparse
from scan import scan

def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="{}.csv".format(datetime.time.today()),
    	help="path to output CSV file containing barcodes")
    ap.add_argument("-t", "--timeout", type=int, default=3,
    	help="timeout after detection in seconds")
    ap.add_argument("-v", "--video", type=bool, default=False,
    	help="boolean whether video will be shown or not")
    args = vars(ap.parse_args())
    print(args)

    
if __name__ == '__main__':
    main()
