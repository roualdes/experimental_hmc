import pytest

import experimentalhmc as ehmc

import numpy as np

# borrow from Stan
# https://github.com/stan-dev/stan/blob/develop/src/test/unit/mcmc/stepsize_adaptation_test.cpp#L99
def test_dualaverage_01():
    da = ehmc.DualAverage(1, 0.5, 2.488109515349, 0.05, 0.75, 10)
    # begin: not part of API
    # only setting for testing
    da.counter = 273
    da.sbar = 0.00513820936953773
    da.xbar = 0.886351350781597
    # end
    da.update(1)

    assert np.isclose(da.optimum(smooth = False), 3.95863527373545)


def test_dualaverage_02():
    da = ehmc.DualAverage(1, 0.5, 4.13018724667137, 0.05, 0.75, 10)
    # begin: not part of API
    # only setting for testing
    da.counter = 79
    da.sbar = 0.0209457573689391
    da.xbar = 0.821976337071218
    # end
    da.update(0.728285153733299)

    assert np.isclose(da.optimum(smooth = False), 2.40769920051673)
    assert np.isclose(da.counter, 80)
    assert np.isclose(da.sbar, 0.0181765250233587)
    assert np.isclose(da.xbar, 0.824095816988227)
    assert np.isclose(da.mu, 4.13018724667137)
    assert np.isclose(da.delta, 0.5)
    assert np.isclose(da.gamma, 0.05)
    assert np.isclose(da.kappa, 0.75)
    assert np.isclose(da.t0, 10)


def test_dualaverage_03():
    da = ehmc.DualAverage(1, 0.5, 4.13018305456267, 0.05, 0.75, 10)
    # begin: not part of API
    # only setting for testing
    da.counter = 79
    da.sbar = 0.0206811620891896
    da.xbar = 0.825842987938587
    # end
    da.update(0.684248188546772)

    assert np.isclose(da.optimum(smooth = False), 2.31161210908631)
    assert np.isclose(da.counter, 80)
    assert np.isclose(da.sbar, 0.0184041693043455)
    assert np.isclose(da.xbar, 0.826295412288499)
    assert np.isclose(da.mu, 4.13018305456267)
    assert np.isclose(da.delta, 0.5)
    assert np.isclose(da.gamma, 0.05)
    assert np.isclose(da.kappa, 0.75)
    assert np.isclose(da.t0, 10)
