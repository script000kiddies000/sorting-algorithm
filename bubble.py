import time

data = [10, 2, 6, 7, 1, 3, 15] 

def swap(a,b):
  swap = a
  a = b
  b = swap
  return a,b

def bubbleSort(data):
    n = len(data)
    for i in range(n):
      for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
          data[j+1], data[j] = swap(data[j+1], data[j])
        print("[%i-%i] - %s" % (i, j, data))


print("BUBBLE SORT \n")
print("Array awal : %s" % data)
start = time.time()
bubbleSort(data)
end = time.time()
print("Array Akhir : %s\n" %data)
print("Selesai dalam %f detik" % (end - start))
