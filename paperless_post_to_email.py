import csv
import argparse
import sys

def main(filename):
    emails = []
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # ['Name', 'Email', 'Status', 'Total', 'Comment', 'Private Message', 'Response', 'Mailing Line 1', 'Mailing Line 2', 'City', 'State', 'Zip Code', 'Country']
            #print row['Email']
            emails.append(row['Email'])
    print ', '.join(emails)

if __name__ == '__main__':
    args = sys.argv[1:]
    filename = args[0]
    print "Reading file: ", filename
    main(filename)
