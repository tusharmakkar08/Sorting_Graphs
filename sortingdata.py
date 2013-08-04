import logging
import graph
import csv
import random
import time

elapsed_time=0

def insertion(ar):
    "Insertion sort"
    for i in range(len(ar)):
        j=i-1
        ch=i
        while j>=0:
            if (ar[ch]<ar[j]):
                ar[ch],ar[j]=ar[j],ar[ch]
                ch=j
            j-=1

def selection(ar):
    "Selection Sort"
    for i in range(len(ar)):
        pos=i
        for j in range(i,len(ar)):
            if(ar[pos]>ar[j]):
                pos=j
        ar[i],ar[pos]=ar[pos],ar[i]
        #print ar

def bubble(ar):
    "Bubble sort"
    for i in range(len(ar)):
        sorted=True
        for j in range(len(ar)-i-1):
            if(ar[j]>ar[j+1]):
                ar[j],ar[j+1]=ar[j+1],ar[j]
                sorted=False
        if sorted:
            break
        #print ar

def quickSort(ar): 
#This function returns the sorted list but does not change the original array like others . Uses extra array and not in place .
    "Quicksort implementation"
    if len(ar)<=1:              
        return ar
    lf,rt=[],[]
    p=ar[0]
    for j in ar:
        if j>=p:
            rt.append(j)
        else:
            lf.append(j)
    l=quickSort(lf)
    r=quickSort(rt[1:])
    c=l+[rt[0]]+r
    #for u in c:
    #    print u,
    #print
    return c
quickSort([1,32,12,12])

def cocktailsort(ar):
    "Cocktail sort implementation"
    swapped=True
    while(swapped):
        swapped=False
        for i in range(len(ar)-1):
            if ar[i]>ar[i+1]:
                ar[i],ar[i+1]=ar[i+1],ar[i]
                swapped=True
        if swapped==False:
            break
        swapped=False
       # print ar
        i=len(ar)-2
        while i>=0:
            if ar[i]>ar[i+1]:
                ar[i],ar[i+1]=ar[i+1],ar[i]
                swapped=True
            i-=1
        #print ar

def gnomesort(ar):
    "Gnomesort implementation"
    pos=1
    last=0
    while pos<len(ar):
        if ar[pos]>=ar[pos-1]:
            if last:
                pos=last
                last=0
            pos+=1
        else:
            ar[pos],ar[pos-1]=ar[pos-1],ar[pos]
            if pos>1:
                if not last:
                    last=pos
                pos-=1
            else:
                pos+=1
        #print ar

def heapsort(ar):
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
        start-=1
def siftdown(ar,start,end):
    "finds approprite position in heap"
    root=start
    while root*2+1<=end:
        child=root*2+1
        swap=root
        if ar[swap]<ar[child]:
            swap=child
        if child+1<=end and ar[swap]<ar[child+1]:
            swap=child+1
        if not (swap==root):
            ar[root],ar[swap]=ar[swap],ar[root]
            root=swap
        else:
            return


def mergesort(ar):
    "Merge sort implementation"
    if len(ar)<=1:
        return ar
    middle=len(ar)/2
    left =ar[:middle]
    right=ar[middle:]
    left=mergesort(left)
    right=mergesort(right)
    res=merge(left,right)
    #print res
    return res
    
def merge(left,right):
    "Merging left and right array in order"
    res=[]
    while len(left)+len(right):
        if len(left)*len(right):
            if left[0]<=right[0]:
                res.append(left[0])
                left=left[1:]
            else:
                res.append(right[0])
                right=right[1:]
        elif len(left):
            res.append(left[0])
            left=left[1:]
        elif len(right):
            res.append(right[0])
            right=right[1:]
    return res


def strandsort(ar):
    "Strandsort implementation"
    items = len(ar)
    sortedBins = []
    while( len(ar) > 0 ):
        highest = float("-inf")
        newBin = []
        i = 0
        while( i < len(ar) ):
            if( ar[i] >= highest ):
                highest = ar.pop(i)
                newBin.append( highest )
            else:
                i=i+1
        sortedBins.append(newBin)
     
    sorted = []
    while( len(sorted) < items ):
        lowBin = 0
        for j in range( 0, len(sortedBins) ):
            if( sortedBins[j][0] < sortedBins[lowBin][0] ):
                lowBin = j
        sorted.append( sortedBins[lowBin].pop(0) )
        if( len(sortedBins[lowBin]) == 0 ):
            del sortedBins[lowBin]
    #print sorted
    #return sorted   

def sorting(key):
  logging.debug('Entered sorting function with %s key'%(key))
	print "Enter the increment"
	inc=input()
	print "Enter Starting Value of N"
	st=input()
	print "Enter Ending Value of N"
	end=input()
	m=[]
	for i in xrange(st,end,inc):
		if key==1:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			insertion(lis)
			elapsed_time=time.time()-start_time
			m.append(["1",i,elapsed_time*(10**6)])
		if key==2:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			bubble(lis)
			elapsed_time=time.time()-start_time
			m.append(["2",i,elapsed_time*(10**6)])
		if key==3:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			mergesort(lis)
			elapsed_time=time.time()-start_time
			m.append(["3",i,elapsed_time*(10**6)])
		if key==4:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			quickSort(lis)
			elapsed_time=time.time()-start_time
			m.append(["4",i,elapsed_time*(10**6)])
		if key==5:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			heapsort(lis)
			elapsed_time=time.time()-start_time
			m.append(["5",i,elapsed_time*(10**6)])
		if key==6:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			selection(lis)
			elapsed_time=time.time()-start_time
			m.append(["6",i,elapsed_time*(10**6)])
		if key==7:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			lis.sort()
			elapsed_time=time.time()-start_time
			m.append(["7",i,elapsed_time*(10**6)])
		if key==8:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			gnomesort(lis)
			elapsed_time=time.time()-start_time
			m.append(["8",i,elapsed_time*(10**6)])
		if key==9:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			cocktailsort(lis)
			elapsed_time=time.time()-start_time
			m.append(["9",i,elapsed_time*(10**6)])
		if key==10:
			lis=random.sample(xrange(1000000), i)
			start_time=time.time()
			strandsort(lis)
			elapsed_time=time.time()-start_time
			m.append(["10",i,elapsed_time*(10**6)])
		try:
			with open("sortdata.csv"):
				logging.debug("File found")
				pass
		except IOError:
			logging.debug("Making New File")
			swriter=csv.writer(open("sortdata.csv","w"))
			swriter.writerow(["id","Number of Terms","Time(in microseconds)"])
	with open("sortdata.csv", "a") as f:
		writer = csv.writer(f)
		writer.writerows(m)
	graph.makegraph(str(key))
	logging.debug('Returning to Main function')


logging.debug('Entered Main function')

while(1):

	print "---------Welcome to The Sorting Experiment Labs-------"
	print "Which algorithm do you want to experiment ? "
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

	inp=input()
	if inp==11:
		break
	logging.debug('Calling Sorting function with %s'%(inp))
	sorting(inp)

graph.compareGraph()
logging.debug('---------------Program Ends--------------')

