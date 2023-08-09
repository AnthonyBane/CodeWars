def tower_builder(n_floors):
    
    if n_floors == 1:
        return ['*', ]
    
    floors = []
    max_items = 2 * n_floors -1
    
    for floor in range(1, n_floors + 1):
        stars = 2 * floor  -1
        spaces = (max_items - stars) // 2
        
        floors.append((" " * spaces) + ("*" * stars) + (" " * spaces))
    
    return floors