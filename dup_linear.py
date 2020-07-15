import bpy

def duplicate_linear(distance):
    bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":distance, "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

def calc_new_distance(base, difference):
    x = base[0] + difference[0]
    y = base[1] + difference[1]
    z = base[2] + difference[2]
    return (x, y, z)

dup_info = {
    "count": 20, #number of copies to make
    "base": (0, -1.4, 0), #distance between original object and the first copy
    "difference": (0, 0.1, 0) #difference in distance between nth and (n+1)th object.
}

# In given example distance between each object on Y axis will be: 1.4, 1.3, 1.2, ... -0,5

distance = dup_info["base"]
for i in range(dup_info["count"]):
    duplicate_linear(distance)
    distance = calc_new_distance(distance, dup_info["difference"])
    
