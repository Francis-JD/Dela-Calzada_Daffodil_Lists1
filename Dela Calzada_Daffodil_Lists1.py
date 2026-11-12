items = []
for i in range(5):
    item = input("Enter item: ")
    items.append(item)

print("Original List: ", end=" ")
for item in items:
    print(item, end=", ")
print()

index = int(input("Input Index to Update: "))
new_value = input("Input New Value: ")
start = int(input("Enter Slice Range 1: "))
end = int(input("Enter Slice Range 2: "))
search = input("Enter Search Item: ")

print("Index to Update:", index)
print("New Value:", new_value)

sliced_list = items[start:end]
print("Sliced List: (" + str(start) + ":" + str(end) + ")", end=" ")
for item in sliced_list:
    print(item, end=", ")
print()

found = False
for x in sliced_list:
    if x == search:
        found = True

if found == True:
    print("Search Result (from sliced array): ", search, "is found in the sliced list")
else:
    print("Search Result (from sliced array): ", search, "is not found in the sliced list")

items[index] = new_value
print("Updated List: ", end=" ")
for item in items:
    print(item, end=", ")
print()