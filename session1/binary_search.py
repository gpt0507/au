def Binary_Search(arr,item):
  low=0
  high=len(arr)-1

  while low<=high:
    mid_value=(low+high)//2
    if arr[mid_value]==item:
      return mid_value
    elif arr[mid_value]<item:
      low=mid_value+1
    elif arr[mid_value]>item:
      high=mid_value-1
  return "item not in list"


print(Binary_Search([0,3,5,7,9,11],3))




























