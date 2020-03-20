Functional Principal Component Analysis (FPCA)
==============================================

This module provides tools to analyse functional data using FPCA. FPCA is
a common tool used to reduce dimensionality while preserving the maximum
quantity of variance in the data. FPCA be applied to a functional data object
in either a basis representation or a discretized representation. The output
of FPCA are orthogonal functions (usually a much smaller sample than the input
data sample) that represent the most important modes of variation in the
original data sample.

For a detailed example please view :ref:`sphx_glr_auto_examples_plot_fpca.py`,
where the process is applied to several datasets in both discretized and basis
forms.

FPCA for functional data in a basis representation
----------------------------------------------------------------

.. autosummary::
   :toctree: autosummary

   skfda.preprocessing.dim_reduction.projection.FPCABasis

FPCA for functional data in a discretized representation
----------------------------------------------------------------

.. autosummary::
   :toctree: autosummary

   skfda.preprocessing.dim_reduction.projection.FPCADiscretized