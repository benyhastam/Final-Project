f= open ("output.txt",'w')

import numpy as np

#فرمول داخل تابع میدان را بدست میارد 

def calculate_electric_field(grid):
    k = 8.9875517873681764e9  
    field_x, field_y = 0, 0  
    o_position = np.where(grid == 'o') 
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] != 'o':
                charge = float(grid[i][j])
                distance_x = j - o_position[1]
                distance_y = i - o_position[0]
                distance = np.sqrt(distance_x**2 + distance_y**2)
                field_x += k * charge * distance_x / distance**3
                field_y += k * charge * distance_y / distance**3
    return [field_x, field_y]

def electric_field_line(C1, length=50, distance=1):
    k = 8.9875517873681764e9  
    dq = C1 * length  
    field_x = k * dq / distance**2  
    return [field_x, 0]  


grid = np.array([['2', '0', '0', '0', '0', '0'],
                 ['0', '0', 'o', '0', '0', '2'],
                 ['0', '0', '0', '0', '0', '0'],
                 ['3', '0', '1', '0', '0', '5'],
                 ['0', '0', '0', '0', '0', '0']])
print("meidan dar O:", calculate_electric_field(grid))

C1 = 1e-6  
print("meidan az fasele dk metry az vasat", electric_field_line(C1))


print("meidan az fasele dk metry az vasat", electric_field_line(C1),file=f)
print( "meidan dar O:", calculate_electric_field(grid),file=f)
f.write( "meidan az fasele dk metry az vasat", electric_field_line(C1))
f.write( "meidan dar O:", calculate_electric_field(grid))
f.close()