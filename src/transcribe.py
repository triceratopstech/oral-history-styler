import csv
import sys

def transcribe(rawCSV):
    transcript = "transcript: "
    csvreader = csv.reader(rawCSV)
    for row in csvreader:
        transcript=transcript + ' ' + row[2] + ','
    return transcript

def openUTF8(filename):
    with open(filename, encoding='utf8') as my_file:
        return(transcribe(my_file))


#this is still executable on its own with a csv file as an argument
if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf8') as my_file:
        print(transcribe(my_file))


