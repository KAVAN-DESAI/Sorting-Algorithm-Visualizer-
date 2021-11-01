import pygame
import random
pygame.font.init()


screen = pygame.display.set_mode((900, 650))
  
pygame.display.set_caption("SORTING VISUALISER")

run = True

width = 900
length = 600
sz = 50000
array = [0]*(sz+1)
arr_clr = [(0, 204, 102)]*(sz+1)
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0),
       (0, 0, 153), (255, 102, 0),(230,230,250)]


fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 30)
fnt2 = pygame.font.SysFont("comicsans", 20)


base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(600, 10, 140, 32)
  

color_active = pygame.Color('lightskyblue3')
  

color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = False


def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
    
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
      
    if largest != i:
        arr_clr[i] = clr[2]
        arr_clr[largest] = clr[2]
        refill(4)
        arr_clr[i] = clr[0]
        arr_clr[largest] = clr[0]
        arr[i], arr[largest] = arr[largest], arr[i]
        
        heapify(arr, n, largest)

        
        
# Sorting Algo:Heap sort
def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2 - 1, -1, -1):
        arr_clr[i] = clr[1]
        refill(4)
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr_clr[i] = clr[2]
        arr_clr[0] = clr[2]
        refill(4)
        arr_clr[i] = clr[3]
        arr_clr[0] = clr[0]
        refill(4)
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    for i in range(n):
        arr_clr[i]=clr[3]
        
        
        
        

def quickSortPartition(start, end, array):
      
    
    pivot_index = start 
    pivot = array[pivot_index]
    arr_clr[pivot_index] = clr[4]
      
    
    while start < end:
        while start < len(array) and array[start] <= pivot:
            arr_clr[start] = clr[1]
            refill(3)
            arr_clr[start] = clr[0]
            start += 1
              
        
        while array[end] > pivot:
            arr_clr[end] = clr[2]
            refill(3)
            arr_clr[end] = clr[0]
            end -= 1
          
        
        if(start < end):
            arr_clr[start] = clr[1]
            arr_clr[end] = clr[2]
            refill(3)
            array[start], array[end] = array[end], array[start]
            arr_clr[start] = clr[2]
            arr_clr[end] = clr[1]
            refill(3)
            arr_clr[start] = clr[0]
            arr_clr[end] = clr[0]
    
    arr_clr[end] = clr[2]
    refill(3)
    array[end], array[pivot_index] = array[pivot_index], array[end]
    arr_clr[end] = clr[2]
    arr_clr[pivot_index] = clr[4]
    refill(3)
    arr_clr[end] = clr[0]
    arr_clr[pivot_index] = clr[0]
     
    
    return end

  
# Sorting Algo:Quick sort
def quickSort(start, end, array):
    if (start < end):
        p = quickSortPartition(start, end, array)
        quickSort(start, p - 1, array)
        quickSort(p + 1, end, array)
    for i in range(end+1):
        arr_clr[i]=clr[3]
        
# Sorting Algo:Bubble sort
def bubblesort(array):
    pygame.event.pump()
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
          if array[j] > array[j+1]:
                arr_clr[j] = clr[1]
                arr_clr[j+1] = clr[2]
                refill(2)
                arr_clr[j] = clr[0]
                arr_clr[j+1] = clr[0]
                array[j], array[j+1] = array[j+1], array[j]
    for i in range(n):
        arr_clr[i]=clr[3]
        
# Generate new Array
def generate_arr():
    for i in range(1, sz+1):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 90)


# Refill
def refill(x):
    screen.fill((255, 255, 255))
    draw(x)
    pygame.display.update()
    pygame.time.delay(50)
    
# Sorting Algo:Merge sort
def mergesort(array, l, r):
    mid = (l + r)//2
    if l < r:
      mergesort(array, l, mid)
      mergesort(array, mid + 1, r)
      merge(array, l, mid,mid + 1, r)

def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        arr_clr[i] = clr[1]
        arr_clr[j] = clr[1]
        refill(1)
        arr_clr[i] = clr[0]
        arr_clr[j] = clr[0]
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        arr_clr[i] = clr[1]
        refill(1)
        arr_clr[i] = clr[0]
        temp.append(array[i])
        i += 1
    while j <= y2:
        arr_clr[j] = clr[1]
        refill(1)
        arr_clr[j] = clr[0]
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        arr_clr[i] = clr[2]
        refill(1)
        if y2-x1 == len(array)-2:
            arr_clr[i] = clr[3]
        else:
            arr_clr[i] = clr[0]
