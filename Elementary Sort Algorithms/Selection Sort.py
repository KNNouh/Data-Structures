#Self programmed version of Selection Sort
class SelectionSort:
    #Sort Function @prams the list of items to be sorted
    def sort(self, listOfItems):
        length = len(listOfItems)
        for i in range(length):
            #@mini the index of the least item in the list starting
            #from the current @ith element
            mini = i
            for j in range(i, length):
                #Compare between the two elements using the rules
                #we put
                if self.less(listOfItems[j], listOfItems[mini]):
                    mini = j
            #Swap the two elements of the element and itself if it is
            #the smallest
            self.exchange(listOfItems, i, mini)

    def less(self, item1, item2):
        return item1.compareTo(item2) < 0

    def exchange(self, listOfItems, i, mini):
        swap = listOfItems[i]
        listOfItems[i] = listOfItems[mini]
        listOfItems[mini] = swap

    def is_sorted(self, listOfItems):
        length = len(listOfItems)
        for i in range(1, length):
            if self.less(listOfItems[i], listOfItems[i - 1]):
                return False
        return True

#A class to use as an example
class DataFrame:
    def __init__(self, name, phone, id):
        self.name = name
        self.phone = phone
        self.id = id

    def compareTo(self, that):
        #Compare on names first
        if self.name < that.name: return -1
        if self.name > that.name: return 1
        #If equal, compare on phones second
        if self.phone < that.phone: return -1
        if self.phone > that.phone: return 1
        #If equal, compare on id last
        if self.id < that.id: return -1
        if self.id > that.id: return 1
        #if equal return 0
        return 0

#An example to be sorted using the rules we put
data = [DataFrame("Karim", "01100000000", 4),
        DataFrame("Nabil", "01273000000", 1),
        DataFrame("Atiaa", "01178000000", 3),
        DataFrame("Karim", "01273000000", 2)]

Selection = SelectionSort()
print(Selection.is_sorted(data))

Selection.sort(data)

for _ in data:
    print(_.name, _.phone, _.id)

print(Selection.is_sorted(data))
