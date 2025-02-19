# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RLpsolveapi(RPackage):
    """R Interface to 'lp_solve' Version 5.5.2.0.

    The lpSolveAPI package provides an R interface to 'lp_solve', a Mixed
    Integer Linear Programming (MILP) solver with support for pure linear,
    (mixed) integer/binary, semi-continuous and special ordered sets (SOS)
    models."""

    cran = "lpSolveAPI"

    version('5.5.2.0-17.7', sha256='9ebc8e45ad73eb51e0b25049598a5bc758370cf89508e2328cf4bd93d68d55bb')
