import csv
import sys
import docx

def transcribe(rawCSV):
    csvreader = csv.reader(rawCSV)
    transcript = str() #start a string to append to
    for row in csvreader:
        try:
            transcript=transcript + ' ' + row[2]
        except IndexError:
            print("row has no valid text")
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


