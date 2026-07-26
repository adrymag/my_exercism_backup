def transform(legacy_data):
    new_data = {}
    
    for point_group_points in list(legacy_data): # legacy_data.keys
        for letter in legacy_data[point_group_points]:
            new_data[letter.lower()] = point_group_points
    
    return new_data