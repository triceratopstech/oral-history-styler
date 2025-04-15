import csv
import sys
import docx
from docx.enum.text import WD_COLOR_INDEX
import re
from datetime import timedelta

def transcribe(rawCSV):

    #configure this to adjust timestamps.
    #Smithsonian oral history spec is 5 minutes
    timestampIntervalMinutes = 5 #in minutes


    csvreader = csv.reader(rawCSV)
    transcript = str() #start a string to append to
    next(csvreader) #assume first line is just headers and ignore
    timestampInterval = timedelta(minutes=timestampIntervalMinutes)
    nextTimestampMinute = timestampInterval
    speaker_name = re.compile("[A-Z, ]+:")


    for row in csvreader:
        nextEntry = str()
        try:
            #is it time to set a timestamp?
            timeString = row[0][0:8]
            timeString = timeString.replace(";",":")
            currentTimestamp = convert_to_timedelta(timeString)

            if(currentTimestamp >= nextTimestampMinute): 
                nextEntry = nextEntry + "\n\n["+str(currentTimestamp)+"]"
                nextTimestampMinute = nextTimestampMinute+timestampInterval
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
    doc = add_begining(doc)
    doc.add_paragraph(content)
    doc = add_ending(doc)
    return doc

def add_ending(doc):
    ending_content = "[END OF INTERVIEW.]"
    doc.add_paragraph(ending_content)
    return doc

def add_begining(doc):
    headings = "Transcript\n\nPreface\n\n"
    heading_run = doc.add_paragraph().add_run(headings)
    heading_run.bold = True

    highlights = ["Interview Name", "Interview Date", "Interview Location", "Interviewee Name and Interviewer Name"]

    intro_paragraph = doc.add_paragraph()
    intro_paragraph.add_run("The following oral history transcript is the result of a recorded interview with ")

    highlight1 = intro_paragraph.add_run("Interview Name")
    highlight1.font.highlight_color = WD_COLOR_INDEX.YELLOW  #Word Doc color index, enum from MSFT.  Yellow is currently 7

    return doc



def convert_to_timedelta(total_time):
    hours = 0
    minutes = 0
    seconds = 0

    hours, minutes, seconds = map(float, total_time.split(':'))
    timedelta(hours=hours, minutes=minutes, seconds=seconds)

    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

#this is still executable on its own with a csv file as an argument
if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf8') as my_file:
        print(transcribe(my_file))


