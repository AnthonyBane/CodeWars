def sort_array(source_array):
    
    odds_sorted = iter(sorted([num for num in source_array if num % 2 != 0]))    
    
    return [num if num % 2 == 0 else next(odds_sorted) for num in source_array]