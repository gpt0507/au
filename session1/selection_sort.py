# # # way1
# def selection_sort(arr):
#   for i in range(len(arr)-1):
#     min=arr[i]
#     for j in range(i+1,len(arr)):
#         if arr[j]<min:
#           min=arr[j]
#           loc=j
#     temp=arr[i]      
#     arr[i]=min
#     arr[loc]=temp
#   return arr


# print(selection_sort([7,3,18,17]))


# # way2
def selection_sort(arr):
  for i in range(len(arr)-1):
    min=arr[i]
    for j in range(i+1,len(arr)):
        if arr[j]<min:
          min=arr[j]
          loc=j
    arr[i],arr[loc]=arr[loc],arr[i]
  return arr

print(selection_sort([7,3,18,17]))

# # # Way3
# def selection_sort(arr):
#   for i in range(len(arr)-1):
#     min=i
#     for j in range(i+1,len(arr)):
#         if arr[min]>arr[j]:
#           min=j
#     arr[min],arr[i]=arr[i],arr[min]
#   return arr


# # print(selection_sort([7,3,18,17]))