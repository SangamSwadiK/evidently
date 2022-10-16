#!/usr/bin/env python
# coding: utf-8
from .anderson_darling_stattest import anderson_darling_test
from .chisquare_stattest import chi_stat_test
from .cramer_von_mises_stattest import cramer_von_mises
from .fisher_exact_stattest import fisher_exact_test
from .jensenshannon import jensenshannon_stat_test
from .kl_div import kl_div_stat_test
from .ks_stattest import ks_stat_test
from .psi import psi_stat_test
from .registry import PossibleStatTestType
from .registry import StatTest
from .registry import StatTestFuncType
from .registry import get_stattest
from .registry import register_stattest
from .wasserstein_distance_norm import wasserstein_stat_test
from .z_stattest import z_stat_test
