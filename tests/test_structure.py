import unittest

import numpy as np

from selective_search.structure import HierarchicalGrouping


class RegionSizeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.image = np.arange(27, dtype=np.uint8).reshape(3, 3, 3)
        self.segmentation = np.array([[0, 0, 1], [0, 2, 2], [2, 2, 2]])

    def test_regions_count_their_own_pixels(self) -> None:
        grouping = HierarchicalGrouping(self.image, self.segmentation, 'CTSF')
        grouping.build_regions()

        self.assertEqual(grouping.regions[0]['size'], 3)
        self.assertEqual(grouping.regions[1]['size'], 1)
        self.assertEqual(grouping.regions[2]['size'], 5)
        self.assertEqual(sum(r['size'] for r in grouping.regions.values()), 9)
        self.assertEqual(grouping.regions[0]['box'], (0, 0, 2, 2))
        self.assertEqual(grouping.regions[1]['box'], (2, 0, 3, 1))
        self.assertEqual(grouping.regions[2]['box'], (0, 1, 3, 3))

    def test_regions_do_not_require_label_one(self) -> None:
        segmentation = np.array([[0, 0, 4], [0, 7, 7], [7, 7, 7]])
        grouping = HierarchicalGrouping(self.image, segmentation, 'CTSF')
        grouping.build_regions()

        self.assertEqual(grouping.regions[0]['size'], 3)
        self.assertEqual(grouping.regions[4]['size'], 1)
        self.assertEqual(grouping.regions[7]['size'], 5)

    def test_merge_preserves_pixel_count_and_histogram_weights(self) -> None:
        grouping = HierarchicalGrouping(self.image, self.segmentation, 'CTSF')
        grouping.build_regions()
        left = grouping.regions[0]
        right = grouping.regions[1]

        grouping.merge_region(0, 1)

        merged = grouping.regions[3]
        self.assertEqual(merged['size'], 4)
        self.assertEqual(np.count_nonzero(grouping.img_seg == 3), 4)
        for histogram in ('color_hist', 'texture_hist'):
            np.testing.assert_allclose(
                merged[histogram],
                0.75 * left[histogram] + 0.25 * right[histogram],
            )


if __name__ == '__main__':
    unittest.main()
