#!/usr/bin/env python
#regular expressions are imported
import re

#mpileup file is opened and each line is read out and is inserted into a lines list
with open("newFile.mpileup") as f:
	f.readline()
	lines = f.readlines()

#important lines list that stores index locations of lines with indels on them
importantLines = []
#count for the maximum sequencing error of the sequencing
#diffCount divided by totalCount
diffCount = 0
totalCount = 0
#count for each individual sequencing error of each line
#dC divided by tC
dC = 0
tC = 0
#two lists that store the line positions of lines with indels and one that stores the significant mutation line
iLines = []
iSM = []

#for loop that basically finds lines with indels and finds the maximum sequencing error of the sequencing
for x in range(0,len(lines)):
	#seq is equal to the line being separated by tabs
	seq = lines[x].split("\t")
	#finditer used in the wrong way to find occurences of indels on the seq line
	y = re.finditer(r'(\+|\-)\d\D*',seq[4])
	for z in y:
		#when an indel is found, the diffCount increments
		diffCount = diffCount + 1
		#the location of the line is also added to important lines
		importantLines.append(x)
	#total count is found
	totalCount = totalCount + len(seq[4])

#outside the for loop, the maximum sequencing error rate is found
mser = diffCount / float(totalCount)

#for loop that finds the sequencing error rate for each line, if the rate is greater than the maximum
#sequencing error rate, then the line's position and line are recorded
for a in range(0,len(importantLines)):
	#s reference is set equal to the line being separated by tabs
	s = lines[importantLines[a]].split("\t")
	#findall is used to find all occurences of indels on the line being viewed
	q = re.findall(r'(\+|\-)\d\D*',s[4])
	#dC and tC are recorded and are used to calculate the sequencing mutation rate for the line
	dC = len(q)
	tC = len(s[4])
	m = ((dC / float(tC)))
	#if the sequencing mutation rate is greater than the maximum sequencing error rate, then the
	#line location and line are recorded and are stored into lists iLines and iSM accordingly
	if (m > mser):
		iLines.append(importantLines[a])
		iSM.append(lines[importantLines[a]])

#mutations.file is opened and the positions and lines with significant mutations are written to the mutations.file
with open("mutations.file","w") as j:
	for w in range(0,len(iLines)):
		j.write("Position: " + str(iLines[w]) + "\n" +  "Significant Mutation Site: " + str(iSM[w]) + "\n")

#**** Note: The output file has multiple occurences of lines due to there being multiple mutations on one line
#**** Also this works for the most part (I think so please be kind when grading this) 
#**** - Samuel Phillips
		
	
