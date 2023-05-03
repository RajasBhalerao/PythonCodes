#Chapter 7: File Processing

"""Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average
of those values and produce an output as shown below. Do not use the sum() function or a variable named
sum in your solution.You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name."""
import sys
fname = input(r"C:\Users\Rajas\OneDrive\Desktop\mbox-short.txt")
fh = open(fname)

addNums = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.strip()
    ipos = line.find(':')
    fline = line[20:]
    try:
        fnum = float(fline)
    except:
        fnum = -1
        sys.exit("Error")

    total = total + 1
    addNums = addNums + fnum
print("Average spam confidence:",addNums/total )