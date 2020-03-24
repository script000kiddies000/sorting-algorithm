import bubble, selection, time

data = [10, 2, 6, 7, 1, 3, 15] 

def cekWaktu(start, end):
  return "Selesai dalam %f detik\n" % (end - start)

while True:
  jwb = input("1. buble sort \n2. selection sort \npilih yang mana ??  ")

  if jwb == '1' :
    start = time.time()
    bubble.bubbleSort(data)
    end = time.time()
    print(cekWaktu(start, end))

  elif jwb == '2' :
    start = time.time()
    selection.selection(data)
    end = time.time()
    print(cekWaktu(start, end))   

  else:
    exit()

  

