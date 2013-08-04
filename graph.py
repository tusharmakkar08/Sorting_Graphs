import matplotlib.pyplot as plt
import csv
import logging

logging.basicConfig(filename='examplegraph.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.debug('This message should go to the log file')

sortdict={"1": "Insertion Sort","2": "Bubble Sort","3": "Merge Sort",\
  	"4": "Quick Sort","5": "Heap Sort","6": "Selection Sort","7": "Tim Sort"\
		,"8": "Gnome Sort","9": "Cocktail Sort","10": "Strand Sort"}

def makegraph(key):
	logging.debug('Entered Makegraph with %s and %s'%(key,sortdict[key]))
	no_of_terms=[]
	time_taken=[]
	soreader=csv.reader(open("sortdata.csv","rb"))
	logging.debug('Opened Sortdata File')
	for row in soreader:
		logging.debug('Rows are %s'%(row))
		if row[0]!="id":
			if row[0]==key:
				no_of_terms.append(row[1])
				time_taken.append(row[2])
	fig=plt.figure()
	logging.debug('Making graph with %s and %s'%(no_of_terms,time_taken))
	ax=fig.add_subplot(111)
	p=ax.plot(no_of_terms,time_taken,'r')
	ax.set_xlabel('No of Terms')
	ax.set_ylabel('Time Taken in microseconds')
	ax.set_title('Number of Terms versus Time in %s'%(sortdict[key]))
	fig.show()
	logging.debug('Plotted Graph')

def compareGraph():
	while 1:
		print "Enter the id's and enter 0 for exit"
		key1=raw_input("")
		if key1=="0":
			break
		key2=raw_input("")
		makeComparegraph(key1,key2)

def makeComparegraph(key1,key2):
	#logging.debug('Entered Makegraph with %s and %s'%(key,sortdict[key]))
	no_of_terms=[]
	time_taken1=[]
	time_taken2=[]
	soreader=csv.reader(open("sortdata.csv","rb"))
	logging.debug('Opened Sortdata File')
	for row in soreader:
		logging.debug('Rows are %s'%(row))
		if row[0]!="id":
			if row[0]==key1:
				no_of_terms.append(row[1])
				time_taken1.append(row[2])
			if row[0]==key2:
				time_taken2.append(row[2])
	fig=plt.figure()
	logging.debug('Making graph with %s and %s and %s'%(no_of_terms,time_taken1,time_taken2))
	ax=fig.add_subplot(111)
	p=ax.plot(no_of_terms,time_taken1,'b')
	p=ax.plot(no_of_terms,time_taken2,'g')
	ax.set_xlabel('No of Terms')
	ax.set_ylabel('Time Taken in microseconds')
	ax.set_title('Number of Terms versus Time in %s (blue) and %s (green)'%(sortdict[str(key1)],sortdict[str(key2)]))
	fig.show()
	logging.debug('Plotted Graph')
