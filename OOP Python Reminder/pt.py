
class Queue():

    def __init__(self,listInput) -> None:
        self.__data = listInput

    def isEmpty(self):

       if(len(self.__data)==0):
        return True
       else:
        return False

    def clear(self):
        self.__data.clear()

    
    def enqueue(self, data):

        self.__data.append(data)

    def dequeue(self):

        if(self.isEmpty()):
            return None

        else:
            temp = self.__data[0]

            for i in range(1,len(self.__data)):

                self.__data[i-1] = self.__data[i]

            self.__data.remove(self.__data[(len(self.__data))-1])
    
            return temp


    def front(self):

        if(self.isEmpty()):

            return None

        else:

            return self.__data[0]

    
    def __len__(self):

        return len(self.__data)

    def __iter__(self):

        if(self.isEmpty()):

            print(None)


        else:
            for i in self.__data:
                print(i)

    def __str__(self):
        return str(self.__data)

class FibonacciExt(Queue):

    def __init__(self,k,q) -> None:
        self.k =  k
        self.q = q
        self.__que = Queue([])
        self.___last_N = None






q  = Queue([1,1])

# q.enqueue(1)
# q.enqueue(1)
# temp = q.dequeue()+q.front()
# q.enqueue(temp)
# q.__iter__()
# print(q.front())


f1 = 0
f0 = 1

#recurssive
def fi(h):

    if(h==1 or h==2):
        return 1
    else:
        return fi(h-1) + fi(h-2)


# print(fi(30))

def fibb(n,k):
    q  = Queue([1,1])
    q1  = Queue([1,1])
    if(n>k):

        for i in range(2,n):

            temp = q.dequeue()+q.front()
            q.enqueue(temp) 
    
        q.__iter__()
    
        for i in range(2,k):

            temp2 = q1.dequeue()+q1.front()
            q1.enqueue(temp2) 
        q1.__iter__()
        q.dequeue()
        q1.dequeue()
        print(q.front() % q1.front())
    else:
        print(q.front())    
 

fibb(78,69)




# daynamic 

def dafi(h):
    pass




# queue
