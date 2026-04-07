from typing import Union
import numpy as np
import scipy.constants as const

def aerodynamic_drag(air_density: Union[np.ndarray, float], drag_coeff: Union[np.ndarray, float], area: Union[np.ndarray, float], speed: Union[np.ndarray, float], wind_speed: Union[np.ndarray, float]) -> tuple[Union[np.ndarray, float], Union[np.ndarray, float]]:
    """
    Calculate the vehicle's aerodynamic drag force and power.

    :param air_density: air density in [kg/m^3]
    :param drag_coeff: drag coefficient [unitless]
    :param area: vehicle's cross-sectional area in [m^2]
    :param speed: vehicle's speed in [m/s]
    :param wind_speed: wind speed in [m/s]
    :return: drag force in [N], drag power in [W]
    """
    drag_force = 0.5*air_density*drag_coeff*area*np.square(speed + wind_speed)
    drag_power = drag_force * speed
    return drag_force, drag_power


def drag_range(energy: float, speed: float, drag_power: float) -> float:
    """
    Calculate the vehicle's range due to aerodynamic drag.

    :param energy: energy in [J]
    :param speed: speed in [m/s]
    :param drag_power: aerodynamic drag power in [W]
    :return: vehicle range in [m]
    """
    return energy*speed/ drag_power


def rolling_resistance(c_r: float, mass: float, speed: Union[float, np.ndarray] = 0.) -> tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:
    """

    :param c_r: coefficient of rolling resistance [unitless]
    :param mass: vehicle mass in [kg]
    :param speed: vehicle speed in [m/s]
    :return: rolling force in [N], rolling power in [W]
    """
    rolling_force = c_r * mass * const.g
    rolling_power = rolling_force * speed
    return rolling_force, rolling_power


def road_load_force(speed: float, coasting_coeffs: tuple[float, float, float]) -> float:
    """

    :param speed: speed in [m/s]
    :param coasting_coeffs: coast-down test coefficients A, B, C
    :return: vehicle road-load force in [N]
    """
    return coasting_coeffs[0] + coasting_coeffs[1]*speed + coasting_coeffs[2]*speed**2

