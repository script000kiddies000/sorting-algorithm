import time

data = [10, 2, 6, 7, 1, 3, 15] 

def swap(a,b):
  swap = a
  a = b
  b = swap
  return a,b

def selection(A):
  for i in range(len(A)): 
      print("[%i] - %s" % (i,A))

      min_idx = i 
      for j in range(i+1, len(A)): 
          if A[min_idx] > A[j]: 
              min_idx = j 
  
      A[i], A[min_idx] = swap( A[i], A[min_idx])

print("SELECTION SORT \n")
print("Array awal : %s" %data)
start = time.time()
selection(data)
end = time.time()
print("Array Akhir : %s\n" %data)
print("Selesai dalam %f detik" % (end - start))
