import csv
import logging

logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.debug('This message should go to the log file')

sortdict={"1": "Insertion Sort","2": "Bubble Sort","3": "Merge Sort",\
  	"4": "Quick Sort","5": "Heap Sort","6": "Selection Sort","7": "Tim Sort"\
		,"8": "Gnome Sort","9": "Cocktail Sort","10": "Strand Sort"}

def choice(inp,stri):
	logging.debug("Entered Choice")
	k=0
	sreader=csv.reader(open("sortindex.csv","rb"))
	for row in sreader:
		if k==inp:
			logging.debug("Entering Comp with %s and %s"%(row,stri))):
    "Heapsort implementation"
    heapify(ar)
    end=len(ar)-1
    while end>0:
        ar[end],ar[0]=ar[0],ar[end]
        end-=1
        siftdown(ar,0,end)
        #print ar
def heapify(ar):
    "Changes array to heap"
    start=(len(ar)-1)/2
    while start>=0:
        siftdown(ar,start,len(ar)-1)
			comp(row,stri)
			logging.debug("Returned from Comp")
			break
		k+=1
	logging.debug("Returning from Choice")

def comp(row,stri):
	logging.debug("Entered comp that is algorithm analysis")
	print "Which type of Complexity do you want to know ? "
	print "1 : Best Case Time Complexity"
	print "2 : Average Case Time Complexity"
	print "3 : Worst Case Time Complexity"
	print "4 : Worst Case Space Complexity"
	inp3=input()
	if inp3==1:
		print "Best Case Time Complexity of",stri,"is",row[2]
	if inp3==2:
		print "Average Case Time Complexity of",stri,"is",row[3]
	if inp3==3:
		print "Worst Case Time Complexity of",stri,"is",row[4]
	if inp3==4:
		print "Worst Case Space Complexity of",stri,"is",row[5]
	logging.debug("Returning from comp")
	
try:
	with open("sortindex.csv"):
		logging.debug("File is already present")
		pass
		
except IOError:
	logging.debug("Making New File")
	swriter=csv.writer(open("sortindex.csv","wb"))
	swriter.writerow(["id","Algorithm Name","Best Case Running time",\
	"Average Case Running Time","Worst Case Running Time",\
	"Worst Case Space Complexity"])
	swriter.writerow(["1","Insertion Sort","O(n)","O(n^2)","O(n^2)","O(1)"])
	swriter.writerow(["2","Bubble Sort","O(n)","O(n^2)","O(n^2)","O(1)"])
	swriter.writerow(["3","Merge Sort","O(n log(n))","O(n log(n))","O(n log(n))","O(n)"])
	swriter.writerow(["4","Quick Sort","O(n log(n))","O(n log(n))","O(n^2)","O(log(n))"])
	swriter.writerow(["5","Heap Sort","O(n log(n))","O(n log(n))","O(n log(n))","O(1)"])
	swriter.writerow(["6","Selection Sort","O(n^2)","O(n^2)","O(n^2)","O(1)"])
	swriter.writerow(["7","Tim Sort","O(n)","O(n log(n))","O(n log(n))","O(n)"])
	swriter.writerow(["8","Gnome Sort","O(n)","O(n^2)","O(n^2)","O(1)"])
	swriter.writerow(["9","Cocktail Sort","O(n)","O(n^2)","O(n^2)","O(1)"])
	swriter.writerow(["10","Strand Sort","O(n)","O(n^2)","O(n^2)","O(n)"])
	logging.debug("----------------File made fully----------------")
	pass

logging.debug("Reading File")
sreader=csv.reader(open("sortindex.csv","rb"))
print "Welcome to the Sorting Algorithms Analysis Page"
print "Enter Input : "
print "1: Print the content of the file"
print "2: Know Thy Complexities"
inp1=input()

if inp1==1:
	print "\n\nPrinting The Contents Of File"
	for row in sreader:
		print row
	logging.debug("---------File Read fully--------")
	
if inp1==2:
	while(1):
		logging.debug("Entered algorithm analysis")
		print "\n\n-----------------------------------"
		print "Which Algorithm Interests you ?"
		print "1: Insertion Sort"
		print "2: Bubble Sort"
		print "3: Merge Sort"
		print "4: Quick Sort"
		print "5: Heap Sort"
		print "6: Selection Sort"
		print "7: Tim Sort"
		print "8: Gnome Sort"
		print "9: Cocktail Sort"
		print "10: Strand Sort"
		print "11: Exit"
		inp2=input()
		if inp2==11:
			break
		logging.debug("Entering Choice function with %s and %s "%(inp2,sortdict[str(inp2)]))
		choice(inp2,sortdict[str(inp2)])
		logging.debug("Returned from Choice function")
		
			
logging.debug("-----------------------------------END OF PROGRAM-------\
---------------------------------\n\n")
