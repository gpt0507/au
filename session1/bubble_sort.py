# def bubble_sort(arr):
#   for  i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#       if arr[j]>arr[j+1]:
#         arr[j],arr[j+1]=arr[j+1],arr[j]
#   print(arr)



# bubble_sort([10,5,7,2,33,18])



def bubble_sort(arr):
  for  i in range(len(arr)):
    for j in range(len(arr)-i-1):
      
      if (arr[j]-arr[j+1])>0:
        arr[j],arr[j+1]=arr[j+1],arr[j]
      else:
        continue

  print(arr)



# bubble_sort([10,5,7,2,33,18])
bubble_sort([2,5,7,10,18,33])