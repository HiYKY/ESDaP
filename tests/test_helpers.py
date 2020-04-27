import unittest
import numpy as np


class TestHelpersCalculateBinaryLabels(unittest.TestCase):
    def test_calculate_binary_labels(self):
        from esdap.helpers import calculate_binary_labels

        # logic for segment annotation
        n_samples = 50
        segment_length = 6
        seizures = [(20, 22)]
        preictal_duration = 8 / 60
        postictal_duration = 17 / 60
        # V:   pre-i -----------++++++++--------------------------------     total: 10
        # I:   ictal -------------------+++-----------------------------     total:  3
        # N:  post-i ----------------------+++++++++++++++++------------     total: 17
        # Z: inter-i +++++++++++----------------------------++++++++++++     total: 21
        #   segments [   Z][V   ][V   ][VIN ][  N ][  N ][  N ][   Z]        I: 1, V: 3, N: 4, Z: 2
        #  strided-2   [   Z][V   ][VI  ][ IN ][  N ][  N ][  N ][   Z]      I: 2, V: 2, N: 4, Z: 2
        #  strided-2     [   Z][V   ][VI  ][  N ][  N ][  N ][   Z]          I: 1, V: 2, N: 3, Z: 2
        # timestamps ................................................... Total: 4     7    11     6
        #            ^         ^         ^         ^         ^         ^        -     -    --     -
        #            1         11        21        31        41        51

        # consecutive segments
        stride = segment_length
        segment_start_times = np.array(range(1, (n_samples + 2), stride)[:-1])
        labels = calculate_binary_labels(
            segment_start_times,
            segment_length,
            seizures,
            preictal_duration,
            postictal_duration,
        )
        self.assertEqual(labels.sum(axis=0).tolist(), [1, 3, 4, 2])

        stride = 2
        segment_start_times = np.array(
            range(1, (n_samples + 2 - (segment_length - stride)), stride)[:-1]
        )
        labels = calculate_binary_labels(
            segment_start_times,
            segment_length,
            seizures,
            preictal_duration,
            postictal_duration,
        )
        self.assertEqual(labels.sum(axis=0).tolist(), [4, 7, 11, 6])
