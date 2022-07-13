import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


#Physical parameters
g = 9.8
l = 1
k = 3
m = 0.5
w = np.sqrt(k/m)
dt = 0.001

#initial conditions
t_final = 20*(np.pi/w)
theta_0 = np.pi/4     #(initial angle)
theta_dot_0 = 0       #(initial angular velocity)   
x_0 = 0.5             #(initial extension of spring)
x_dot_0 = 0           #(initial radial velocity of bob)



print(f"Motion of a spring pendulum for total time {t_final} seconds")
print(f"Mass of the bob = {m} kg")
print(f"Natural lenght of spring = {l} m")
print(f"Spring constant = {k} N/m")
print(f'Initial angle of bob = {theta_0} radians')
print(f'Initial angular velocity bob = {theta_dot} rad/s')
print(f'Initial extension of spring = {x_0} m')
print(f'Initial radial velocity of bob = {x_dot} m/s')



# Equations of motion
def get_theta_ddot(x, theta, theta_dot, x_dot):
    return (-2/(x+l))*(theta_dot*x_dot)-(g/(x+l))*np.sin(theta)


def get_x_ddot(x, theta_dot, theta):
    return (x+l)*(theta_dot**2)+g*np.cos(theta)-(x*w**2)


#initialising variables
x = x_0
theta = theta_0
theta_dot = theta_dot_0
x_dot = x_dot_0
t = 0 

#Lists for storage
x_list = [x_0]
theta_list = [theta_0] 
x1_list = [(x_0+l)*np.sin(theta_0)]
y1_list = [-(x_0+l)*np.cos(theta_0)]

while t<=t_final:
    x_ddot = get_x_ddot(x, theta_dot, theta)
    theta_ddot = get_theta_ddot(x, theta, theta_dot, x_dot)
    
    x += x_dot*dt
    x_list.append(x)
    x_dot += x_ddot*dt
    
    theta += theta_dot*dt
    theta_list.append(theta)
    theta_dot += theta_ddot*dt
    
    x1_list.append((x+l)*np.sin(theta))
    y1_list.append(-(x+l)*np.cos(theta))
                   
    t += dt    


#Ploting/Animating the results

#fig = plt.figure()
#ax = plt.subplot(1, 1, 1)
#data_skip = 5
#def init_func():
#    ax.clear()
#def anim(i):
#    ax.plot(x1_list[i:i+data_skip], y1_list[i:i+data_skip], color='b')
#    plt.xlim(-2, 2)
#    plt.ylim(-5, 2)
#anim1 = FuncAnimation(fig, anim, frames=np.arange(0, len(x1_list), data_skip), init_func=init_func, interval = 5)
#plt.show()
#anim1.save('spring_pendulum.mp4', dpi = 150, fps=60, writer='Pillow')


plt.plot(x1_list, y1_list, label='trajectory')
plt.plot([0], [0], 'k.', label="point of suspension")
plt.plot([x1_list[0]], [y1_list[0]], 'r.', label="initial point")
plt.xlim([-2, 2])
plt.ylim([-5, 2])
plt.grid()
plt.legend()
plt.show()
    
