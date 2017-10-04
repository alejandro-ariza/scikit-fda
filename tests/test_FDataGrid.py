import unittest
from fda.FDataGrid import FDataGrid
import numpy
import os
from fda import math_basic
from fda import kernel_smoothers
from fda import kernels
import scipy.stats.mstats
import pickle
import matplotlib.pyplot as plt

PHONEME_DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/phoneme_data.csv')
PHONEME_ARGVALS_PATH = os.path.join(os.path.dirname(__file__), '../data/phoneme_argvals.csv')


class TestFDataGrid(unittest.TestCase):

    def setUp(self):
        self.phoneme_data = numpy.genfromtxt(PHONEME_DATA_PATH, delimiter=',', skip_header=1)
        self.phoneme_argvals = numpy.genfromtxt(PHONEME_ARGVALS_PATH, delimiter=',', skip_header=1)
        with open('phoneme.pkl', 'rb') as input_file:
            self.phoneme = pickle.load(input_file)

    def test_init(self):
        fd = FDataGrid([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
        numpy.testing.assert_array_equal(fd.data_matrix, numpy.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]))
        self.assertSequenceEqual(fd.argvals_range, (0, 1))
        numpy.testing.assert_array_equal(fd.argvals, numpy.array([0., 0.25, 0.5, 0.75, 1.]))
        fd = FDataGrid(self.phoneme_data, self.phoneme_argvals)
        numpy.testing.assert_array_equal(fd.data_matrix, self.phoneme_data)
        t1 = numpy.linspace(0, 1, 51)
        t2 = numpy.linspace(0, 1, 31)
        z = [[[(i*a)*(b**i) for b in t2] for a in t1] for i in range(4)]
        argvals = [t1, t2]
        FDataGrid(numpy.array(z), argvals)

    def test_mean(self):
        fd = FDataGrid([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
        mean = math_basic.mean(fd)
        numpy.testing.assert_array_equal(mean.data_matrix[0], numpy.array([1.5, 2.5, 3.5, 4.5, 5.5]))
        self.assertSequenceEqual(fd.argvals_range, (0, 1))
        numpy.testing.assert_array_equal(fd.argvals, numpy.array([0., 0.25, 0.5, 0.75, 1.]))

    def test_gmean(self):
        fd = FDataGrid([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
        mean = math_basic.gmean(fd)
        numpy.testing.assert_array_equal(mean.data_matrix[0],
                                         scipy.stats.mstats.gmean(numpy.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])))
        self.assertSequenceEqual(fd.argvals_range, (0, 1))
        numpy.testing.assert_array_equal(fd.argvals, numpy.array([0., 0.25, 0.5, 0.75, 1.]))

    def test_derivate(self):
        deriv = self.phoneme.derivate()
        # TODO retreive data from the R library to compare

if __name__ == '__main__':
    print()
    unittest.main()