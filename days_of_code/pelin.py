# AUTOGENERATED! DO NOT EDIT! File to edit: 05_Playing_with_Perlin.ipynb (unless otherwise specified).

__all__ = ['random_grad', 'interpolate', 'dotGridGradient', 'perlin', 'perlin_grid']

# Cell
def random_grad(ix, iy):
    #Random float. No precomputed gradients mean this works for any number of grid coordinates
    random = 2920 * np.sin(ix * 21942 + iy * 171324 + 8912) * np.cos(ix * 23157 * iy * 217832 + 9758)
    return np.array([np.cos(random),np.sin(random)])

# Cell
def interpolate(a0, a1, w):
    """ Interpolate between the two points, with weight 0<w<1 """
#     return (a1 - a0) * w + a0 # Can make this smoother later
    return (a1 - a0) * ((w * (w * 6.0 - 15.0) + 10.0) * w * w * w) + a0

def dotGridGradient(ix, iy, x, y):
    gradient = random_grad(ix, iy);

    # Compute the distance vector
    dx = x - ix
    dy = y - iy

    # Return the dot-product
    return (dx*gradient[0] + dy*gradient[1]);

# Compute Perlin noise at coordinates x, y
def perlin(x,y):
    # Determine grid cell coordinates
    x0 = np.array(x).astype(int)
    x1 = x0 + 1
    y0 = np.array(y).astype(int)
    y1 = y0 + 1

    # Determine interpolation weights
    sx = x - x0 # Could also use higher order polynomial/s-curve here
    sy = y - y0

    # Interpolate between grid point gradients
    n0 = dotGridGradient(x0, y0, x, y)
    n1 = dotGridGradient(x1, y0, x, y)
    ix0 = interpolate(n0, n1, sx)

    n0 = dotGridGradient(x0, y1, x, y)
    n1 = dotGridGradient(x1, y1, x, y)
    ix1 = interpolate(n0, n1, sx)

    value = interpolate(ix0, ix1, sy)
    return value

# Cell
def perlin_grid(w, h, x_bounds=(0, 1), y_bounds=(0, 1)):
    nx, ny = w, h
    x = np.linspace(*x_bounds, nx)
    y = np.linspace(*y_bounds, ny)
    xv, yv = np.meshgrid(x, y)
    return perlin(xv, yv)