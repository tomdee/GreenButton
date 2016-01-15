import datetime

import sys
from dateutil.parser import parse
import csv
epoch = datetime.datetime(1970,1,1)

reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
for row in reader:
    # Skip headers
    if len(row) > 1 and 'usage' in row[0]:
        if 'gas' in row[0]:
            # Gas is daily
            b = parse(row[1])
            timestamp = int((b - epoch).total_seconds() * 1000000000)
            print "energy,energy_type=gas,value_type=usage value=%s %s" % (row[2], timestamp)
            if row[4][1:] != "":
                print "energy,energy_type=gas,value_type=cost value=%s %s" % (row[4][1:], timestamp)
        else:
            # Electricity is hourly
            b = parse("%s %s" % (row[1], row[2]))
            timestamp = int((b - epoch).total_seconds() * 1000000000)
            print "energy,energy_type=electric,value_type=usage value=%s %s" % (row[4], timestamp)
            if row[6][1:] != "":
                print "energy,energy_type=electric,value_type=cost value=%s %s" % (row[6][1:], timestamp)

        # print ', '.join(row)