import numpy as np

from algo import bubblesort, insertionsort, premerge, prequick , heapsort
from visualizer import visualize


print("Sorting Algorithm Visualizer")
print("1 Bubble Sort")
print("2 Insertion Sort")
print("3 Merge Sort")
print("4 quick sort")
print("5 heap sort")

choice = input("Choose algorithm: ")

arr = list(np.random.randint(1,100,30))

if choice == "1":

    gen = bubblesort(arr.copy())
    visualize(arr, gen, "Bubble Sort")

elif choice == "2":

    gen = insertionsort(arr.copy())
    visualize(arr, gen, "Insertion Sort")

elif choice == "3":

    gen = premerge(arr.copy())
    visualize(arr, gen, "Merge Sort")


elif choice == "4":
    gen= prequick(arr.copy())
    visualize(arr,gen,"quick sort")

elif choice == "5":
    gen=heapsort(arr.copy())
    visualize(arr,gen,"heapsort")

else:

    print("Invalid option")