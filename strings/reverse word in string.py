word = input("Enter string: ")
print(word[::-1])


'''
       Use [::-1]:

This is the more common and concise way to reverse a list.
It clearly indicates that you want to reverse the entire list without specifying a starting point.

       Use [-1::-1]:

This is a more explicit way of stating that you are starting from the last element.
It might be useful if you want to emphasize that the reversal starts from the last item.


but both give same output'''
