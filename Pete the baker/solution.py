def cakes(recipe, available):
    return min(available.get(key, 0) // recipe[key] for key in recipe)
