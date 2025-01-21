import csv
import sys

def transcribe(rawCSV):
    transcript = "transcript: "
    csvreader = csv.reader(rawCSV)
    for row in csvreader:
        transcript=transcript + ' ' + row[2] + ','
    return transcript


with open(sys.argv[1]) as my_file:
    print(transcribe(my_file))


