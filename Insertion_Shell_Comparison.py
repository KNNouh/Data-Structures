import time
import matplotlib.pyplot as plt

class MainFunctions:
    def less(self, item1, item2):
        try:
            return item1.compareTo(item2) < 0
        except:
            return item1 < item2


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

class InsertionSort(MainFunctions):
    #Sort Function @prams the list of items to be sorted
    def sort(self, listOfItems):
        length = len(listOfItems)
        for i in range(length):
            for j in range(i, 0, -1):
                if super().less(listOfItems[j], listOfItems[j-1]):
                    super().exchange(listOfItems, j, j-1)
                else:
                    break

class ShellSort(MainFunctions):
    #Sort Function @prams the list of items to be sorted
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

def initialize_data(n):
    data = [DataFrame("Karim", "01173091969", 4),
            DataFrame("Nabil", "01273091968", 1),
            DataFrame("Atiaa", "01178031367", 3),
            DataFrame("Karim", "01273091969", 2)]*n
    return data

x1 = [100, 500, 1000, 5000, 10000]
insertion_y = []
shell_y = []

for _ in x1:
    __ = 4*_
    print(f"For {__} Items: ")

    data = initialize_data(_)
    shell = ShellSort()
    start_time = time.time()

    shell.sort(data)

    shell_time_taken = (time.time() - start_time)
    shell_y.append(shell_time_taken*1000)
    print(f"Shell Sort took --- {shell_time_taken:0.5f} seconds ---" )

    #####
    data = initialize_data(_)
    insertion = InsertionSort()
    start_time = time.time()

    insertion.sort(data)

    insertion_time_taken = (time.time() - start_time)
    insertion_y.append(insertion_time_taken*1000)
    print(f"Insetion Sort took --- {insertion_time_taken:0.5} milliseconds ---" )
    percentage = 1/insertion_time_taken
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
