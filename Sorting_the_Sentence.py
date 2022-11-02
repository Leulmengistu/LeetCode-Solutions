class Solution:
    def sortSentence(self, s: str) -> str:
        mylist = s.split()
        size = len(mylist)
# sorting the words using insertion sort by using the last number on each word as sorting mechanism.

        for i in range(1,size):
            hole = i
            value = mylist[hole]
            while(hole > 0 and mylist[hole-1][-1] > value[-1]):
                mylist[hole]= mylist[hole-1]
                hole = hole - 1
                
            mylist[hole]= value
        
        stringOutput = ""
        
        for item in mylist:
            
            item = item.rstrip(item[-1])
            if(stringOutput != ""):
                stringOutput = stringOutput + " " + item
            else:
                stringOutput = stringOutput + item
            
        return stringOutput
            