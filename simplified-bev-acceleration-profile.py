"""
Plotting the acceleration vs time profile for a Battery Electric Vehicle
Chapter 2.

Ref:
1. Hayes & Goodarzi, Electric Powertrain
"""

from transportation.vehicle_dynamics import dynamics
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    rated_power = 80000  # rated rotor power in W
    rated_torque = 254  # rated rotor torque in Nm
    r = 0.315  # wheel radius
    gear_ratio = 8.19  #
    mass = 1645 # mass in kg
    coastdown_params = (133.3, 0.7094, 0.491) # coastdown parameters A, B, C
    gear_efficiency = 0.97 # assumed gear efficiency
    moment_of_inertia = 3 # assumed axle-reference Moment of Inertia
    rated_wr = rated_power / rated_torque  # rated angular speed
    rated_speed = rated_wr * r / gear_ratio # vehicle speed in m/s

    time_array = np.linspace(0, 12, endpoint=True, num=100)
    delta_t = time_array[1] - time_array[0]
    speed_array = np.zeros_like(time_array)
    torque_array = np.zeros_like(time_array)
    w_array = np.zeros_like(time_array)
    power_array = np.zeros_like(time_array)

    for n in range(0, np.shape(time_array)[0]-1):
        w_array[n] = speed_array[n] * gear_ratio / r  # rotor speed
        if speed_array[n] < rated_speed:
            torque_array[n] = rated_torque
        else:
            torque_array[n] = rated_power / w_array[n]

        # eqn 2.34
        speed_array[n+1] = speed_array[n] + delta_t*(gear_ratio * gear_efficiency * torque_array[n] - r*dynamics.road_load_force(speed_array[n], coastdown_params))/(r*mass + moment_of_inertia/r)

        power_array[n] =  torque_array[n] * w_array[n]

    fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
    ax1.plot(time_array[:-1], 3.6*speed_array[:-1])
    ax2.plot(time_array[:-1], power_array[:-1] / 1000)
    #ax1.set_ylim(0, 100)
    ax2.set_ylim(0, 100)
    ax1.set_ylabel('Speed [km/h]')
    ax1.set_xlabel('Time [s]')
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Power [kW]')
    ax1.grid(True)
    ax2.grid(True)
    ax1.set_title('Nissan Leaf Acceleration Profile - speed vs time')
    ax2.set_title('Nissan Leaf Acceleration Profile - power vs time')
    plt.savefig('Nissan Leaf Acceleration Profile.pdf', bbox_inches='tight')
    plt.savefig('Nisan Leaf Acceleration Profile.png', bbox_inches='tight')
    plt.show()
    plt.close()
