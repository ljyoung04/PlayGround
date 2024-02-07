class Sort :
    
    @staticmethod
    def bubbleSort(lst):
        for i in range(len(lst)-1):
            for j in range(len(lst)-1-i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    @staticmethod
    def insertionSort(lst):
        for i in range(1,len(lst)):
            key = lst[i]
            j = i - 1 
            while j >= 0 and key < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
        return lst
    
    @staticmethod
    def mergeSort():
        pass

    @staticmethod
    def quickSort():
        pass