import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, sigma, r, b):
    dx = sigma * (y - x)
    dy = r*x - y - x*z
    dz = x*y - b*z
    return dx, dy, dz
# determine step size
dt = 0.01
steps = 10000
xs = np.empty(steps + 1)
ys = np.empty(steps + 1)
zs = np.empty(steps + 1)
ts = np.linspace(0, 100, steps + 1)

def plotLorenz(r):
    # initial conditions
    sigma = 10
    b = 8/3

    xs[0], ys[0], zs[0] = 10.5, 3.0, 7.0 # PNG, JPG, GIF
    for i in range(steps):
        dx, dy, dz = lorenz(xs[i], ys[i], zs[i], sigma, r, b)
        xs[i+1] = xs[i] + dx*dt
        ys[i+1] = ys[i] + dy*dt
        zs[i+1] = zs[i] + dz*dt

    fig = plt.figure()
    ax = fig.gca(projection='3d')  # Make plot 3D

    ax.plot(xs, ys, zs, lw=0.5)  # Plot x, y, and z with line width 0.5
    ax.set_xlabel("x-axis")  # Sets x label
    ax.set_ylabel("y-axis")  # Sets y label
    ax.set_zlabel("z-axis")  # Sets z label
    ax.set_title("Lorenz | r = " + str(r))  # Set title based on r
    plt.show()  # Show Lorenz plot

    ts = np.linspace(0, 100.01, 10001)  # Set array for time based on dt step size
    plt.title("x(t) [JPG] | r = " + str(r))  # Set title for x(t) plot based on r
    plt.xlabel("t - Time")  # Sets x label - time
    plt.ylabel("x - JPG")  # Sets y label - x
    plt.plot(ts, xs)  # Plots x(t)
    plt.show()  # Show plot
    
    plt.title("y(t) [PNG] | r = " + str(r))  # Set title for y(t) plot based on r
    plt.xlabel("t - Time")  # Sets x label - time
    plt.ylabel("y - PNG")  # Sets y label - y
    plt.plot(ts, ys)  # Plots y(t)
    plt.show()  # Show plot
    
    plt.title("z(t) [GIF] | r = " + str(r))  # Set title for z(t) plot based on r
    plt.xlabel("t")  # Sets x label - y
    plt.ylabel("z - GIF")  # Sets y label - z
    plt.plot(ts, zs)  # Plot z(t)
    plt.show()  # Show plot

plotLorenz(4)
plotLorenz(12)
plotLorenz(36)
