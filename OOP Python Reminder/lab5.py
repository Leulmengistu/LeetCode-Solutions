class Queue(object):
    def __init__(self, collections = None):
        #rear: end of the list
        #front: begining of the list
        self._data = list()
        if collections is not None:
            for x in collections:
                self._data.append(x)

    def isEmpty(self): return len(self._data)==0
    
    def clear(self): self._data.clear()
    
    def enqueue(self, obj):
        self._data.append(obj)
        
    def dequeue(self): #remove and return front item
        try:
            return self._data.pop(0)
        except Exception as e:
            print("Caught exception ", str(e))
            raise Exception('dequeue an empty queue')

    def front(self): #return front item

        try:
            return self._data[0]
        except Exception as e:
            print("Caught exception ", str(e))
            raise Exception('front() is called for an empty queue')

    def __str__(self): return str(self._data)
        
    def __len__(self) : return len(self._data)
        
    def __iter__(self):
        for x in self._data:
            yield x

    def __eq__(self, other):
        if len(self._data) !=  len(other._data):
            return False
        for i in range(len(self._data)):
            if self._data[i] != other._data[i]:
                return False
        return True

    def __getitem__(self, index):
        return self._data[index]


class FibonacciExt(Queue):

    def __init__(self,k,q,collections=None):

        super().__init__(collections)

        self.k=k

        self.q=q

        self.__que = None

        self.__last_N = None

    def valueAt(self,n):
        
        assert n >=0, f"Value of n must be greater than or equal to  0"

        tempList = list()

        for i in range(self.k):

            tempList.append(1)

        self.__que =Queue(tempList)
       
        if(self.k == 0): return None

        if(self.k < n and self.k > 0 and self.q > 0):

            for j in range (self.k,n+1):

                tempSum = self.__que.dequeue()

                for i in range(self.k-1):
             
                    tempdata = self.__que.dequeue()

                    tempSum = tempSum + tempdata

                    self.__que.enqueue(tempdata)

                self.__que.enqueue(tempSum)

            if(tempSum >= self.q):

                return tempSum % self.q

            else:

                return tempSum

        else:

            return self.__que.front()

    def __str__(self,n):

        return  str(self.valueAt(n))


def splitLine(Line:str):

    spaceCounter1 = 0

    spaceCounter2 = 0


    spaceCounter3 = 0

    n,k,q = "","",""

    for char in Line:

        if(char == " " and n == ""):

            continue

        if(char != " " and spaceCounter1 == spaceCounter2):

            n = n + char

        if(char == " " and n != "" and k == ""):

            spaceCounter2 += 1

            spaceCounter3 += 1

            continue

        if (char != " " and spaceCounter1 < spaceCounter2 and spaceCounter2 == spaceCounter3):

            k = k + char

        if(char == " " and k != ""):

            spaceCounter3 += 1

            continue

        if(char != " " and k != ""and spaceCounter2 < spaceCounter3):
            
            q = q + char

    return int(n), int(k), int(q)


def main():

    with open("lab5_input.txt","r") as fileInput:

        with open("lab5_output.txt", "a") as fileOutput:

            counter = 0

            for item in fileInput:

                counter += 1

                Line = item.strip("\n")

                n,k,q = splitLine(Line)

                fib = FibonacciExt(k,q)

                if(fib.valueAt(n)!= None):

                    fileOutput.write(f"Case {counter}: {str(fib.valueAt(n))}\n")

                else:

                    counter -= 1


if __name__ == "__main__":

    main()

