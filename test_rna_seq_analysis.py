import unittest
import pandas as pd
import numpy as np
from rna_seq_analysis import read_excel, compute_statistics

class TestRNASeqAnalysis(unittest.TestCase):

    def setUp(self):
        self.input_file = 'rnaseq.xlsx'
        self.df = read_excel(self.input_file)

    def test_compute_statistics(self):
        result_df = compute_statistics(self.df.copy())

        expected_naive_mean = [818.33, 264, 14129]  
        expected_naive_sd = [217.08, 30.51, 2571.7]      
        expected_injured_mean = [1000, 277, 10341.67] 
        expected_injured_sd = [121.62, 81.84, 39.55]     

        np.testing.assert_almost_equal(result_df['Naive_Mean'].values[:3], expected_naive_mean, decimal=2)
        np.testing.assert_almost_equal(result_df['Naive_SD'].values[:3], expected_naive_sd, decimal=2)
        np.testing.assert_almost_equal(result_df['Injured_Mean'].values[:3], expected_injured_mean, decimal=2)
        np.testing.assert_almost_equal(result_df['Injured_SD'].values[:3], expected_injured_sd, decimal=2)

if __name__ == '__main__':
    unittest.main()