"""
Plotting the torque and speed characteristics vs vehicle speed
Recreated figure 2.7.

Ref:
1. Hayes & Goodarzi, Electric Powertrain
"""
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    rated_power = 80000 # rated rotor power in W
    rated_torque = 254 # rated rotor torque in Nm
    r = 0.315 # wheel radius
    gear_ratio = 8.19 #
    max_speed = 150 # maximum vehicle speed in km/h
    rated_wr = rated_power / rated_torque # rated angular speed
    max_wr = gear_ratio * max_speed /(3.6 * r) # rotor speed at maximum speed
    num_steps = 1000
    wr_array = np.linspace(1, max_wr, num_steps)
    speed_array = (3.6 * r) *wr_array / gear_ratio # [km/h]

    torque_array = np.zeros_like(wr_array)
    vehicle_speed_array = np.zeros_like(wr_array)

    # wr_array < rated_wr
    masked_wr = np.ma.masked_less(wr_array, rated_wr) # angular speed is less than rated speed
    torque_array[masked_wr.mask] = rated_torque # apply mask to torque array. eqn 2.28
    power_array = rated_torque * wr_array
    vehicle_speed_array[masked_wr.mask] = wr_array[masked_wr.mask] / gear_ratio * r
    # angular speed is more than rated speed
    torque_array[~masked_wr.mask] = rated_power / wr_array[~masked_wr.mask] # eqn 2.30
    power_array[~masked_wr.mask] = rated_power # eqn 2.30

    fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
    ax1.plot(speed_array, torque_array)
    ax2.plot(speed_array, power_array/1000)
    ax1.set_xlabel('Speed [km/h]')
    ax1.set_ylabel('Torque [Nm]')
    ax2.set_xlabel('Speed [km/h]')
    ax2.set_ylabel('Power [kW]')
    ax1.grid(True)
    ax2.grid(True)
    ax1.set_title('Nissan Leaf Nominal Torque Characteristics')
    ax2.set_title('Nissan Leaf Nominal Power Characteristics')
    plt.savefig('Nissan Leat Nominal Power and Torque Characteristics.pdf', bbox_inches='tight')
    plt.savefig('Nissan Leaf Nominal Power and Torque Characteristics.png', bbox_inches='tight')
    plt.show()
    plt.close()


