from typing import Union
import numpy as np
import pint


def mpg_canada_to_us(mpg_ca):
    u_reg = pint.UnitRegistry()
    u_reg.define('_100km = 100 * kilometer')
    u_reg.define('mpg = 1 * mile / gallon')
    fuel_ec_canada = mpg_ca * u_reg.L / u_reg._100km
    fuel_ec_us = (1 / fuel_ec_canada).to(u_reg.mpg)
    return fuel_ec_us

def mpg_us_to_canada(us_mpg):
    u_reg = pint.UnitRegistry()
    u_reg.define('_100km = 100 * kilometer')
    u_reg.define('mpg = 1 * mile / gallon')
    u_reg.define('Lp100km = L/ _100km')
    fuel_ec_us = us_mpg * u_reg.mpg
    fuel_ec_ca = (1/ fuel_ec_us).to(u_reg.Lp100km)
    return fuel_ec_ca




