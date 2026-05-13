from typing import Union
import numpy as np

def rotor_hz_to_rpm(rotor_hz: float) -> float:
    return rotor_hz*60.


def rotor_rpm_to_hz(rotor_rpm: float) -> float:
    return rotor_rpm/60.


def rotor_speed_hz(omega_r: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    return omega_r * 60./ (2. *np.pi)