import matplotlib.pyplot as plt

def subplots_autogrid(n, fig=None, **kwargs):    
    """
    create a square-like grid of subplots of
    n axes. Does some work to identify a good
    row/col combo for n. Sends **kwargs either to
    fig.subplots or plt.subplots. Yields each
    axis, stopping at n. 
    """
    rows = int(math.sqrt(n))
    cols = rows
    if n % rows > 0: 
        depart_max = max(min(int(rows * .4), 10), 1)
        best_alternative = sorted([(alt, n % alt) for alt in (range(rows+1, rows+depart_max+1) + range(rows-1, rows-depart_max-1))], 
                                  key=lambda x: x[1], reverse=True)[0]
        rows = best_alternative[0]
        cols = n / rows + 1
    if fig:
        axes = fig.subplots(rows, cols, **kwargs)
    else: 
        fig, axes = plt.subplots(rows, cols, **kwargs)
    count = 0
    for c in xrange(cols):
        for r in xrange(rows):
            if count < n:
                yield axes[r][c]
            count += 1
