import matplotlib.pyplot as plt

from random_walk import RandomWalk

decisions = input("How many choices would you like the walk to make?\n")
sizes= input("What size would you like your data points to be?\n")

while True:
    rw = RandomWalk(decisions)
    rw.fill_walk()
    
    plt.figure(figsize=(10,6))

    point_numbers = list(range(int(rw.num_points)))
    
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolor = 'none', s=int(sizes))
    plt.scatter(0,0, c='red')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red')
    
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    
    
    
    plt.show()
    
    keep_running = input("Make another walk with "+decisions+" decisions and "+sizes+" size points?(y/n): ")
    if keep_running.lower() == 'n':
        break
