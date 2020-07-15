import bpy

dup_info = {
    "count": 20, #number of copies to make
    "base": (0, -1.4, 0), #distance between original object and the first copy
    "formula": (0, 0.1, 0) #difference in distance between nth and (n+1)th object.
}

# In given example distance between each object on Y axis will be: 1.4, 1.3, 1.2, ... -0,6

for i in range(dup_info["count"]):
    print("key")
