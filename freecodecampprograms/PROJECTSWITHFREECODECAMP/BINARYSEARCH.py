#a binary search algorithm is one that searches an item through a list of sorted items by splitting the list by half and checking on both ends
def binary_search(list,element):
  start=0
  middle=0
  end=len(list)
  steps=0
  while (start<=end):
    print("Steps ",steps,":",str(list[start:end+1]))
    steps+=1
    middle=(start+end)//2
    if element==list[middle]:
      return middle
    if element<list[middle]:
      end=middle-1
    else:
      start=middle+1
  return -1
my_list =[1,2,3,4,5,6,7,8,9,10,11,12]
element=int(input("Enter a number between 1 -12 to be searched through a list: "))
binary_search(my_list,element)
    