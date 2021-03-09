# Created by: Antoine Gustave

mynumbers = [1,5,-4,8,-11]

def num_pos():
    results = 0
    
    for number in mynumbers:
        if number > 0:
            results += 1
    
    print(f'Total positive numbers: {results}')

num_pos()