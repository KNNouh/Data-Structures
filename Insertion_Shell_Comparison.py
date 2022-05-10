import time
import matplotlib.pyplot as plt

#Here we implement the functions repeated in Shell and Insertion sort to inheret from
class MainFunctions:
    #To compare between to elements @item1, @item2
    def less(self, item1, item2):
        try:
            #We use a structure of our own with a certian function (compareTo)
            return item1.compareTo(item2) < 0
        except:
            return item1 < item2


    def exchange(self, listOfItems, i, mini):
        #To swap to elements in the list we want to sort @listOfItems located in indexes @i, @mini
        swap = listOfItems[i]
        listOfItems[i] = listOfItems[mini]
        listOfItems[mini] = swap

    def is_sorted(self, listOfItems):
        #To check it the list @listOfItems is sorted or not
        length = len(listOfItems)
        for i in range(1, length):
            if self.less(listOfItems[i], listOfItems[i - 1]):
                return False
        return True

class InsertionSort(MainFunctions):
    #Sort Function @listOfItems the list of items to be sorted
    def sort(self, listOfItems):
        length = len(listOfItems)
        for i in range(length):
            for j in range(i, 0, -1):
                if super().less(listOfItems[j], listOfItems[j-1]):
                    super().exchange(listOfItems, j, j-1)
                else:
                    break

class ShellSort(MainFunctions):
    #Sort Function @listOfItems the list of items to be sorted
    def sort(self, listOfItems):
        length = len(listOfItems)
        h = 1
        while h < length//3: h = 3 * h + 1
        while h >= 1:
            for i in range(h, length):
                for j in range(i, 0, -h):
                    if j >= h and super().less(listOfItems[j], listOfItems[j-h]):
                        super().exchange(listOfItems, j, j-h)
                    else:
                        break
            h //= 3

# A structure we use as an example
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

#To initialize data we want to sort
def initialize_data(n):
    data = [DataFrame("Karim", "01173091969", 4),
            DataFrame("Nabil", "01273091968", 1),
            DataFrame("Atiaa", "01178031367", 3),
            DataFrame("Karim", "01273091969", 2)]*n
    return data

#Number of data items we will use each time
x1 = [100, 500, 1000, 5000, 10000]
insertion_y = []
shell_y = []

for _ in x1:
    #As the frame we use contain 4 elements each time multiplied by _
    __ = 4*_
    print(f"For {__} Items: ")

    data = initialize_data(_)
   
    #Calculate time taken
    start_time = time.time()
    #Starting the Shell Sort
    ShellSort().sort(data)
    shell_time_taken = (time.time() - start_time)
    
    #Append time taken to shell_y list
    shell_y.append(shell_time_taken*1000)
    print(f"Shell Sort took --- {shell_time_taken:0.5f} seconds ---" )

    #####
    data = initialize_data(_)
  
    #Calculate time taken
    start_time = time.time()
    #Starting the Insertion Sort
    InsertionSort().sort(data)
    insertion_time_taken = (time.time() - start_time)
    
    #Append time taken to insertion_y list
    insertion_y.append(insertion_time_taken*1000)
    print(f"Insetion Sort took --- {insertion_time_taken:0.5} milliseconds ---" )
    percentage = 1
    if shell_time_taken != 0:
        percentage = insertion_time_taken//shell_time_taken
    print(f'Shell is {percentage:0.3f} times faster.\n')

x = [4*i for i in x1]

plt.xlabel('Number Of Items')
plt.ylabel('Execution Time (Milliseconds)')
plt.title('Shell Sort')
plt.plot(x, insertion_y, label = 'Inserstion Sort')
plt.plot(x, shell_y, label = 'Shell Sort')
plt.show()
