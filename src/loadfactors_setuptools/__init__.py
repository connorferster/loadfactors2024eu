"""
A package for calculating Canadian structural load factors as per NBCC-15
"""
version = "0.1.0"

from loadfactors_setuptools.loadfactors import (
    Load,
    open_load_combinations,
    factored_max,
    factored_min,
    factored_max_trace,
    factored_min_trace,
    get_factored_matrix,
    factor_load,
    alias_to_service_loads
)