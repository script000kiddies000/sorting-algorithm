def swap(a,b):
  swap = a
  a = b
  b = swap
  return a,b

def selection(A):
  print("SELECTION SORT \n")
  print("Array awal : %s" %A)

  for i in range(len(A)): 
      print("[%i] - %s" % (i,A))

      min_idx = i 
      for j in range(i+1, len(A)): 
          if A[min_idx] > A[j]: 
              min_idx = j 
  
      A[i], A[min_idx] = swap( A[i], A[min_idx])

  print("Array Akhir : %s\n" %A)
