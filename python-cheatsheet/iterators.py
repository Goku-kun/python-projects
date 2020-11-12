# Iterators in python (specifically range function)

# Iterators are a type of objects specifically used to iterate.
# There is a list iterator as well as a range iterator.

a_list = iter([1, 2, 3, 4])
print(a_list)

print(iter(range(10)))


# Great benefit of using iterators in range() is that a List is never explicitly created for this type of object

# for ex:

N = 10**12

for i in range(N):
    if i>=10: break
    print(i, end=' ')

# It would be a waste of memory if the range(10**12) amount of memory was occupied when only the memory needed was for the first ten values.

# The examples of other iterators could be enumerate, zip, filter, and map.