shoppinglist = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

itemtofind= "spam"
foundat = None

# for index in range(6):
# for index in range(len(shoppinglist)):
#     if shoppinglist[index] == itemtofind:
#         foundat = index
#         break

if itemtofind in shoppinglist:
    foundat = shoppinglist.index(itemtofind)
if foundat is not None:
    print("Item found in aisle {}".format(foundat))  
else:
    print("{} not found".format(itemtofind))     