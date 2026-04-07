#import argparse
from transportation.vehicle_dynamics import dynamics


if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-c", "--calculate", type=str, required=True, help="Calculate ")

    #args = parser.parse_args()
    #calc_action = args.calculate

    c_d = 0.25
    cross_area = 2.
    v = 33.33
    rho_air = 1.2
    wind_speed = 0.
    f_d, p_d = dynamics.aerodynamic_drag(rho_air, c_d, cross_area, v, wind_speed)
    print(f_d)
    print(p_d)

    drag_range = dynamics.drag_range(20*3.6*10**6, v, p_d)
    print(drag_range)

    rolling_force, rolling_power = dynamics.rolling_resistance(0.0085, 2000, 2.77)
    print(rolling_force)



