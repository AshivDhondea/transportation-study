"""
Plotting the acceleration vs time profile for a Battery Electric Vehicle
Chapter 2.

Ref:
1. Hayes & Goodarzi, Electric Powertrain
"""

from transportation.vehicle_dynamics import dynamics
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

    w_array = speed_array * gear_ratio / r # rotor speed
    masked_speed = np.ma.masked_less(speed_array, rated_speed)  # speed is less than rated speed
    torque_array[masked_speed.mask] = rated_torque  # apply mask to torque array. eqn 2.28
    # angular speed is more than rated speed
    torque_array[~masked_speed.mask] = rated_power / speed_array[~masked_speed.mask]  # eqn 2.30

    for n in range(0, np.shape(time_array)[0]-1):
        # eqn 2.34
        speed_array[n+1] = speed_array[n] + delta_t*(gear_ratio * gear_efficiency * torque_array[n] - r*dynamics.road_load_force(speed_array[n], coastdown_params))/(r*mass + moment_of_inertia/r)

    power_array =  torque_array * w_array
