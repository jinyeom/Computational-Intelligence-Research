# util.py

# sort agents by their fitness via quicksort
def quicksort(agents):
    if len(agents) > 1:
        pivot = agents[0]
        
        larger = [a for a in agents if a.fitness > pivot.fitness]
        equal = [a for a in agents if a.fitness == pivot.fitness]
        smaller = [a for a in agents if a.fitness < pivot.fitness]

        return quicksort(larger) + equal + quicksort(smaller)

    return agents
