import csv

def deleteSortData(n):
	cr = csv.reader(open("sortdata.csv","rb"))
	sortData = []
	for row in cr:
		if row[0] != n or row[0] == 'Id':
			sortData.append(row)
	with open("sortdata.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(sortData)
		
def compareFor(n):
	timeList = {}
	cr = csv.reader(open("sortdata.csv","rb"))
	name = csv.reader(open("sortindex.csv","rb"))
	for row in cr:
		if row[1] == n:
			timeList[row[0]] = row[2]
	l=map(float,timeList.values())
	print "Min time is",min(l)
	#print timeList,l
	for key in timeList:
		#print timeList[key][:13],str(max(l))
		if timeList[key][:13] == str(min(l))[:13]:
		#	print "LOL"
			minKey = key
		if timeList[key][:12] == str(max(l))[:12]:
		#	print "big LOL"
			maxKey = key
	for row in name:
		if row[0] == minKey:
			print "The sorting algorithm with least running time is",row[1]
		if row[0] == maxKey:
			print "The sorting algorithm with maximum running time is",row[1]

def findSortType():
    sortDict = {'1':'O(n)','2':'O(1)','3':'O(n^2)','4':'O(n log(n))'}
    notFoundFlag = 0
    print "\nSelect the kind of complexity to check:"
    print "1: Worst case time"
    print "2: Worst case space"
    print "3: Best case time"
    print "4: Average case time"
    choice = raw_input("")
    cr = csv.reader(open("sortindex.csv","rb"))
    print "Select the complexity:"
    print "1: O(n)"
    print "2: O(1)"
    print "3: O(n^2)"
    print "4: O(n log(n))"
    complexityChoice = raw_input("")
    for row in cr:
        if choice == '1':
            if row[4] == sortDict[complexityChoice]:
                notFoundFlag = 1
                print row[1]
        elif choice == '2':
            if row[5] == sortDict[complexityChoice]:
                notFoundFlag = 1
                print row[1]
        if choice == '3':
            if row[2] == sortDict[complexityChoice]:
                notFoundFlag = 1
                print row[1]
        if choice == '4':
            if row[3] == sortDict[complexityChoice]:
                notFoundFlag = 1
                print row[1]
    if notFoundFlag == 0:
        print "Sort algorithm with given complexity not found"

print "---------Welcome to Database Module for sorting------------"
print "Press 1 for Deleting a Particular column"
print "Press 2 for comparing the time "
print "Press 3 for Checking out algorithms for a particular functionality"
inp=input()
if inp==1:
	print "Whose data you want to delete ?"
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
	inp1=input()
	deleteSortData(str(inp1))
if inp==2:
	print "For which time do you want to compare ?"
	inp2=input()
	compareFor(str(inp2))
if inp==3:
	findSortType()
