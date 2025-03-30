# Sets in Python are unordered collections. 
# So print the elements in a sorted order by converting the Set to a sorted list using the " sorted() " function.

a = set(input("Enter elements for the first set (space-separated):").split())
b = set(input("Enter elements for the second set (space-separated):").split())

print(f"Set 1: {sorted(a)}")
print(f"Set 2: {sorted(b)}")
print(f"Union Set: {sorted(a.union(b))}")
print(f"Intersection set: {sorted(a.intersection(b))}")
print(f"Difference Set (Set 1 - Set 2): {sorted(a.difference(b))}")
print(f"Symmetric difference set: {sorted(a.symmetric_difference(b))}")


'''
The symmetric difference of two sets is defined as the set of elements that are in either of the sets but not in their intersection.
In other words, it includes elements that are unique to each set.
example:

a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference(b)  # This would yield {1, 2, 4, 5} '''
