# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from __future__ import annotations
from typing import List
from typing import (
    List,
    Optional,
    Set,
    Tuple,
    Union,
)


def Alshul_1952(Re: float, eD: float) -> float: ...


def Avci_Karagoz_2009(Re: float, eD: float) -> float: ...


def Barr_1981(Re: float, eD: float) -> float: ...


def Blasius(Re: float) -> float: ...


def Brkic_2011_1(Re: float, eD: float) -> float: ...


def Brkic_2011_2(Re: float, eD: float) -> float: ...


def Buzzelli_2008(Re: float, eD: float) -> float: ...


def Chen_1979(Re: float, eD: float) -> float: ...


def Churchill_1973(Re: float, eD: float) -> float: ...


def Churchill_1977(Re: float, eD: float) -> float: ...


def Clamond(Re: float, eD: float, fast: bool = ...) -> float: ...


def Colebrook(Re: float, eD: float, tol: Optional[int] = ...) -> float: ...


def Eck_1973(Re: float, eD: float) -> float: ...


def Fang_2011(Re: float, eD: float) -> float: ...


def Haaland(Re: float, eD: float) -> float: ...


def Jain_1976(Re: float, eD: float) -> float: ...


def Manadilli_1997(Re: float, eD: float) -> float: ...


def Moody(Re: float, eD: float) -> float: ...


def Papaevangelo_2010(Re: float, eD: float) -> float: ...


def Prandtl_von_Karman_Nikuradse(Re: float) -> float: ...


def Rao_Kumar_2007(Re: float, eD: float) -> float: ...


def Romeo_2002(Re: float, eD: float) -> float: ...


def Round_1980(Re: float, eD: float) -> float: ...


def Serghides_1(Re: float, eD: float) -> float: ...


def Serghides_2(Re: float, eD: float) -> float: ...


def Shacham_1980(Re: float, eD: float) -> float: ...


def Sonnad_Goudar_2006(Re: float, eD: float) -> float: ...


def Swamee_Jain_1976(Re: float, eD: float) -> float: ...


def Tsal_1989(Re: float, eD: float) -> float: ...


def Wood_1966(Re: float, eD: float) -> float: ...


def Zigrang_Sylvester_1(Re: float, eD: float) -> float: ...


def Zigrang_Sylvester_2(Re: float, eD: float) -> float: ...


def friction_factor(
    Re: float,
    eD: float = ...,
    Method: Optional[str] = ...,
    Darcy: bool = ...
) -> float: ...


def friction_factor_curved(
    Re: float,
    Di: float,
    Dc: float,
    roughness: float = ...,
    Method: Optional[str] = ...,
    Rec_method: str = ...,
    laminar_method: str = ...,
    turbulent_method: str = ...,
    Darcy: bool = ...
) -> float: ...


def friction_factor_curved_methods(
    Re: float,
    Di: float,
    Dc: float,
    roughness: float = ...,
    check_ranges: bool = ...
) -> List[str]: ...


def friction_factor_methods(Re: float, eD: float = ..., check_ranges: bool = ...) -> List[str]: ...


def friction_laminar(Re: float) -> float: ...


def friction_plate_Kumar(Re: float, chevron_angle: float) -> float: ...


def friction_plate_Martin_1999(Re: float, plate_enlargement_factor: float) -> float: ...


def friction_plate_Martin_VDI(Re: float, plate_enlargement_factor: float) -> float: ...


def friction_plate_Muley_Manglik(Re: float, chevron_angle: float, plate_enlargement_factor: float) -> float: ...


def ft_Crane(D: float) -> float: ...


def fuzzy_match(name: str, strings: Set[str]) -> str: ...


def helical_Re_crit(Di: float, Dc: float, Method: str = ...) -> float: ...


def helical_laminar_fd_Mori_Nakayama(Re: float, Di: float, Dc: float) -> float: ...


def helical_laminar_fd_Schmidt(Re: float, Di: float, Dc: float) -> float: ...


def helical_laminar_fd_White(Re: float, Di: float, Dc: float) -> float: ...


def helical_transition_Re_Ito(Di: float, Dc: float) -> float: ...


def helical_transition_Re_Kubair_Kuloor(Di: float, Dc: float) -> float: ...


def helical_transition_Re_Kutateladze_Borishanskii(Di: float, Dc: float) -> float: ...


def helical_transition_Re_Schmidt(Di: float, Dc: float) -> float: ...


def helical_transition_Re_Seth_Stahel(Di: float, Dc: float) -> float: ...


def helical_transition_Re_Srinivasan(Di: float, Dc: float) -> float: ...


def helical_turbulent_fd_Czop(Re: float, Di: float, Dc: float) -> float: ...


def helical_turbulent_fd_Guo(Re: float, Di: float, Dc: float) -> float: ...


def helical_turbulent_fd_Ju(Re: float, Di: float, Dc: float, roughness: float = ...) -> float: ...


def helical_turbulent_fd_Mandal_Nigam(
    Re: float,
    Di: float,
    Dc: float,
    roughness: float = ...
) -> float: ...


def helical_turbulent_fd_Mori_Nakayama(Re: float, Di: float, Dc: float) -> float: ...


def helical_turbulent_fd_Prasad(
    Re: float,
    Di: float,
    Dc: float,
    roughness: float = ...
) -> float: ...


def helical_turbulent_fd_Schmidt(
    Re: float,
    Di: float,
    Dc: float,
    roughness: float = ...
) -> float: ...


def helical_turbulent_fd_Srinivasan(Re: float, Di: float, Dc: float) -> float: ...


def material_roughness(ID: str, D: Optional[float] = ..., optimism: Optional[bool] = ...) -> float: ...


def nearest_material_roughness(name: str, clean: Optional[bool] = ...) -> str: ...


def one_phase_dP(
    m: float,
    rho: float,
    mu: float,
    D: float,
    roughness: float = ...,
    L: float = ...,
    Method: None = ...
) -> float: ...


def one_phase_dP_dz_acceleration(m: float, D: float, rho: float, dv_dP: float, dP_dL: float, dA_dL: float) -> float: ...


def one_phase_dP_gravitational(angle: float, rho: float, L: float = ..., g: float = ...) -> float: ...


def roughness_Farshad(
    ID: Optional[str] = ...,
    D: Optional[float] = ...,
    coeffs: Optional[Tuple[float, float]] = ...
) -> float: ...


def transmission_factor(fd: Optional[float] = ..., F: Optional[float] = ...) -> float: ...


def von_Karman(eD: float) -> float: ...

__all__: List[str]