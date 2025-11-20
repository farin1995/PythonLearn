# Creating tuples
my_tuple = (1, 2, 3, "hello", True)  # A tuple with mixed data types
single_element_tuple = ("single_item",) # Note the comma for a single-element tuple
empty_tuple = ()
another_tuple = tuple([4, 5, 6]) # Converting a list to a tuple

print("Original tuple:", my_tuple)
print("Single element tuple:", single_element_tuple)
print("Empty tuple:", empty_tuple)
print("Tuple from list:", another_tuple)

# Accessing elements
print("\nAccessing elements:")
print("First element:", my_tuple[0])
print("Fourth element:", my_tuple[3])
print("Last element (negative indexing):", my_tuple[-1])

# Slicing tuples
print("\nSlicing tuples:")
print("Slice from index 1 to 3 (exclusive):", my_tuple[1:4])
print("Slice from beginning to index 2 (exclusive):", my_tuple[:3])
print("Slice from index 2 to end:", my_tuple[2:])

# Immutability demonstration (this will raise an error)
# try:
#     my_tuple[0] = 10
# except TypeError as e:
#     print(f"\nError demonstrating immutability: {e}")

# Tuple concatenation
combined_tuple = my_tuple + another_tuple
print("\nCombined tuple:", combined_tuple)

# Tuple repetition
repeated_tuple = (1, 2) * 3
print("Repeated tuple:", repeated_tuple)

# Looping through a tuple
print("\nLooping through a tuple:")
for item in my_tuple:
    print(item)

# Checking if an element exists
print("\nChecking for elements:")
print("Is 'hello' in my_tuple?", "hello" in my_tuple)
print("Is 10 in my_tuple?", 10 in my_tuple)

# Finding the index of an element
print("\nFinding element index:")
print("Index of 'hello':", my_tuple.index("hello"))

# Counting occurrences of an element
duplicate_tuple = (1, 2, 2, 3, 1)
print("Count of 1 in duplicate_tuple:", duplicate_tuple.count(1))
