import pytest

import experimentalhmc as ehmc

import numpy as np

def test_convergence():
    x = [0.239407691, -0.62282776, 0.24356776, -1.10368191,
         -1.507900223, -0.97702220, -0.49290339, -0.04632925,
         -1.421186419, -0.73568277, 0.04301316, -0.15462371,
         -0.770254789, -1.32197653, -0.71799675, -0.05134798,
         0.003243823, -0.05474649, -1.00474817, 0.52814719,
         2.118660239, 0.29459794, -1.15549545, -0.27780754,
         -0.548916260, -0.14347794, 1.47567766, 0.16420936,
         -0.847931550, 0.11253483, 1.66249639, 2.36078238,
         0.847943703, -0.44757236, -1.08864716, 0.92910897,
         0.699827332, 0.50092564, -0.30425246, -0.32194831,
         -1.070388865, 0.69792782, -0.31303889, -0.29153897,
         0.688964769, 0.08287254, 0.19910818, 0.15701755,
         -0.782429086, 1.67931003, -0.14829945, -0.22959858,
         -0.925853513, -0.85916121, 0.04880209, -0.04997852,
         0.391888329, -0.87161484, -0.03473023, 0.93634380,
         0.016131943, -1.79682200, -0.84479692, -0.98430272,
         0.276388510, -1.50788909, -1.52233697, -1.48942141,
         -0.433214020, 0.57052300, 0.88867629, -0.53208358,
         -0.682587678, 0.41141717, 0.62939699, 0.04428697,
         1.798689555, 0.38975660, -0.72060527, 1.12196227]
    draws = np.reshape(x, (20, 1, 4))

    assert np.isclose(ehmc.ess_mean(draws), 75.95232, atol = 1e-5)
    assert np.isclose(ehmc.ess_tail(draws), 65.7112, atol = 1e-5)
    assert np.isclose(ehmc.ess_quantile(draws, 0.75), 89.15154, atol = 1e-5)
    assert np.isclose(ehmc.ess_std(draws), 68.86159, atol = 1e-5)

    assert np.isclose(ehmc.rhat_basic(draws), 0.9629473, atol = 1e-5)
    assert np.isclose(ehmc.rhat_max(draws), 1.009791, atol = 1e-3) # why 1e-3

    assert np.isclose(ehmc.mcse_mean(draws), 0.1010431, atol = 1e-5)
    assert np.isclose(ehmc.mcse_std(draws), 0.07730264, atol = 1e-5)

    # not enough draws
    assert np.isnan(ehmc.ess_mean(draws[0:1, :, :]))
    assert np.isnan(ehmc.rhat_basic(draws[0:1, :, :]))

    # NaN in draws
    draws[0, 0, 0] = np.nan
    assert np.isnan(ehmc.ess_mean(draws))
    assert np.isnan(ehmc.rhat_basic(draws))
