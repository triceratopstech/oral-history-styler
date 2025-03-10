import csv
import sys
import docx
import re
from datetime import time

def transcribe(rawCSV):

    #configure this to adjust timestamps.
    #Smithsonian oral history spec is 5 minutes
    timestampInterval = 5 #in minutes


    csvreader = csv.reader(rawCSV)
    transcript = str() #start a string to append to
    next(csvreader) #assume first line is just headers and ignore
    nextTimestampMinute = timestampInterval
    speaker_name = re.compile("[A-Z, ]+:")


    for row in csvreader:
        nextEntry = str()
        try:
            #is it time to set a timestamp?
            currentTimestamp = time.fromisoformat(row[0])

            if(currentTimestamp.minute >= nextTimestampMinute): 
                nextEntry = nextEntry + "\n\n["+currentTimestamp.isoformat("seconds")+"]"
                nextTimestampMinute = (nextTimestampMinute+timestampInterval)%60
                if(not speaker_name.match(row[2])):
                    nextEntry = nextEntry + "\n\n"
            for line in row[2].splitlines():
                if(speaker_name.match(line)):
                    nextEntry = nextEntry + "\n\n" + line + ' '
                else:
                    nextEntry = nextEntry + line + ' '

            transcript = transcript+nextEntry
    
        except Exception as e:
            print("skipping row with malformed text: " + ','.join(row) + '\n', e)

    return transcript

def openUTF8(filename):
    with open(filename, encoding='utf8') as my_file:
        return(transcribe(my_file))

def makedocx(content):
    doc = docx.Document()
    doc.add_paragraph(content)
    return doc

#this is still executable on its own with a csv file as an argument
if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf8') as my_file:
        print(transcribe(my_file))


