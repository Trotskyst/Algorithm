from django.test import TestCase
from alg_list.generation_algorithm import *


class Test_sort(TestCase):

    def test1(self):
        list_current = []
        list_result = []
        test = 'Test1'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test2(self):
        list_current = [1, 2]
        list_result = [1, 2]
        test = 'Test2'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по Test_sort не пройден")

    def test3(self):
        list_current = [1, 2, 1]
        list_result = [1, 1, 2]
        test = 'Test3'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test4(self):
        list_current = [76, 4, 70, 64, 78, 58, 28, 22, 48, 6]
        list_result = [4, 6, 22, 28, 48, 58, 64, 70, 76, 78]
        test = 'Test4'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test5(self):
        list_current = [29, 98, 12, 15, 89, 46, 18, 25, 7, 96]
        list_result = [7, 12, 15, 18, 25, 29, 46, 89, 96, 98]
        test = 'Test5'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test6(self):
        list_current = [46, 1, 79, 78, 27, 74, 40, 7, 87, 83]
        list_result = [1, 7, 27, 40, 46, 74, 78, 79, 83, 87]
        test = 'Test6'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test7(self):
        list_current = [717, 828, 108, 871, 399, 563, 288, 390, 410, 425, 311, 178, 738, 825, 729, 75, 394, 153, 536,
                        116, 894, 409, 743, 283, 474, 229, 634, 748, 518, 341, 18, 303, 156, 313, 873, 748, 50, 45, 796,
                        343, 327, 611, 341, 919, 47, 495, 281, 425, 607, 987, 681, 455, 515, 776, 969, 461, 841, 386,
                        701, 109, 879, 775, 271, 436, 459, 146, 252, 252, 479, 571, 601, 904, 64, 580, 654, 985, 496,
                        567, 918, 603, 510, 448, 605, 585, 779, 461, 752, 242, 13, 540, 44, 77, 334, 6, 772, 608, 670,
                        2, 948, 905]
        list_result = [2, 6, 13, 18, 44, 45, 47, 50, 64, 75, 77, 108, 109, 116, 146, 153, 156, 178, 229, 242, 252, 252,
                       271, 281, 283, 288, 303, 311, 313, 327, 334, 341, 341, 343, 386, 390, 394, 399, 409, 410, 425,
                       425, 436, 448, 455, 459, 461, 461, 474, 479, 495, 496, 510, 515, 518, 536, 540, 563, 567, 571,
                       580, 585, 601, 603, 605, 607, 608, 611, 634, 654, 670, 681, 701, 717, 729, 738, 743, 748, 748,
                       752, 772, 775, 776, 779, 796, 825, 828, 841, 871, 873, 879, 894, 904, 905, 918, 919, 948, 969,
                       985, 987]
        test = 'Test7'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test8(self):
        list_current = [168, 724, 621, 96, 873, 24, 846, 76, 86, 935, 84, 921, 212, 608, 397, 969, 8, 34, 930, 756, 196,
                        438, 598, 132, 935, 445, 61, 444, 838, 888, 594, 367, 952, 82, 734, 88, 291, 462, 221, 816, 14,
                        309, 266, 228, 595, 446, 387, 227, 878, 50, 422, 128, 835, 338, 737, 625, 590, 647, 556, 638,
                        405, 493, 557, 242, 286, 841, 35, 247, 304, 290, 267, 614, 204, 300, 388, 392, 617, 328, 825,
                        712, 24, 90, 401, 65, 877, 232, 393, 658, 707, 388, 542, 182, 833, 76, 96, 883, 206, 526, 1,
                        973]
        list_result = [1, 8, 14, 24, 24, 34, 35, 50, 61, 65, 76, 76, 82, 84, 86, 88, 90, 96, 96, 128, 132, 168, 182,
                       196, 204, 206, 212, 221, 227, 228, 232, 242, 247, 266, 267, 286, 290, 291, 300, 304, 309, 328,
                       338, 367, 387, 388, 388, 392, 393, 397, 401, 405, 422, 438, 444, 445, 446, 462, 493, 526, 542,
                       556, 557, 590, 594, 595, 598, 608, 614, 617, 621, 625, 638, 647, 658, 707, 712, 724, 734, 737,
                       756, 816, 825, 833, 835, 838, 841, 846, 873, 877, 878, 883, 888, 921, 930, 935, 935, 952, 969,
                       973]
        test = 'Test8'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test9(self):
        list_current = [351, 481, 98, 711, 67, 696, 387, 44, 381, 249, 773, 301, 820, 648, 759, 120, 313, 651, 897, 30,
                        630, 299, 590, 278, 263, 722, 168, 595, 665, 683, 746, 422, 529, 415, 50, 263, 699, 619, 468,
                        837, 260, 95, 104, 144, 177, 730, 846, 95, 639, 611, 462, 783, 310, 730, 18, 154, 863, 286, 1,
                        802, 155, 301, 450, 61, 39, 331, 325, 685, 972, 549, 734, 481, 382, 986, 483, 976, 851, 855,
                        111, 780, 649, 457, 176, 809, 314, 809, 985, 443, 500, 785, 326, 757, 934, 815, 515, 753, 378,
                        276, 966, 82]
        list_result = [1, 18, 30, 39, 44, 50, 61, 67, 82, 95, 95, 98, 104, 111, 120, 144, 154, 155, 168, 176, 177, 249,
                       260, 263, 263, 276, 278, 286, 299, 301, 301, 310, 313, 314, 325, 326, 331, 351, 378, 381, 382,
                       387, 415, 422, 443, 450, 457, 462, 468, 481, 481, 483, 500, 515, 529, 549, 590, 595, 611, 619,
                       630, 639, 648, 649, 651, 665, 683, 685, 696, 699, 711, 722, 730, 730, 734, 746, 753, 757, 759,
                       773, 780, 783, 785, 802, 809, 809, 815, 820, 837, 846, 851, 855, 863, 897, 934, 966, 972, 976,
                       985, 986]
        test = 'Test9'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test10(self):
        list_current = [860, 245, 908, 286, 557, 62, 876, 200, 594, 616, 287, 421, 460, 570, 469, 871, 56, 36, 709, 245,
                        993, 539, 565, 697, 259, 428, 940, 150, 191, 535, 825, 220, 515, 664, 799, 728, 369, 335, 448,
                        170, 300, 269, 771, 748, 456, 493, 881, 111, 9, 780, 396, 53, 20, 947, 574, 469, 780, 750, 712,
                        302, 3, 272, 27, 291, 225, 509, 172, 69, 98, 953, 347, 156, 7, 967, 706, 685, 862, 576, 705,
                        176, 67, 256, 44, 2, 201, 412, 490, 857, 282, 934, 700, 727, 94, 162, 758, 700, 28, 93, 899, 5]
        list_result = [2, 3, 5, 7, 9, 20, 27, 28, 36, 44, 53, 56, 62, 67, 69, 93, 94, 98, 111, 150, 156, 162, 170, 172,
                       176, 191, 200, 201, 220, 225, 245, 245, 256, 259, 269, 272, 282, 286, 287, 291, 300, 302, 335,
                       347, 369, 396, 412, 421, 428, 448, 456, 460, 469, 469, 490, 493, 509, 515, 535, 539, 557, 565,
                       570, 574, 576, 594, 616, 664, 685, 697, 700, 700, 705, 706, 709, 712, 727, 728, 748, 750, 758,
                       771, 780, 780, 799, 825, 857, 860, 862, 871, 876, 881, 899, 908, 934, 940, 947, 953, 967, 993]
        test = 'Test10'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

    def test11(self):
        list_current = [2.0780590717299576, 1.0702947845804989, 0.8855291576673866, 0.03538928210313448,
                        1.1944444444444444, 0.9671361502347418, 0.6640926640926641, 0.6078914919852034, 1.0,
                        0.4189189189189189, 1.7865853658536586, 0.10316529894490035, 0.2326923076923077,
                        1.244956772334294, 3.0586080586080584, 0.5881326352530541, 1.5234113712374582,
                        2.6370967741935485, 0.907563025210084, 2.43731778425656, 1.017563117453348, 1.919315403422983,
                        2.6923076923076925, 0.13141025641025642, 16.0, 0.6927083333333334, 1.064207650273224,
                        8.45945945945946, 2.6904761904761907, 1.4972067039106145, 1.0347938144329898,
                        0.2206896551724138, 22.21875, 1.0232558139534884, 1.1116279069767443, 14.310344827586206,
                        0.06656804733727811, 0.3316062176165803, 0.7107692307692308, 1.782312925170068,
                        0.49349240780911063, 1.0378681626928472, 5.372781065088757, 2.4496314496314495,
                        0.5397590361445783, 0.22169811320754718, 0.7041343669250646, 3.9306930693069306,
                        1.4687022900763358, 864.0, 1.1278350515463917, 0.2953813104189044, 2.1864406779661016,
                        0.2850061957868649, 0.8886576482830385, 0.7595628415300546, 0.6473509933774835,
                        1.24597364568082, 44.55555555555556, 0.6653439153439153, 0.2949886104783599, 1.046242774566474,
                        1.418103448275862, 4.474025974025974, 1.9154078549848943, 0.12179487179487179,
                        0.9337606837606838, 0.8265895953757225, 0.22783083219645292, 5.061538461538461,
                        0.7355769230769231, 3.061320754716981, 1.426183844011142, 0.47963340122199594,
                        1.2129760225669957, 3.823529411764706, 0.16271186440677965, 0.8810289389067524,
                        1.8303571428571428, 0.7870239774330042, 1.2242225859247136, 1.606153846153846,
                        0.6952380952380952, 0.796711509715994, 1.2420212765957446, 0.8126721763085399,
                        0.45769622833843016, 0.9697950377562028, 4.709677419354839, 3.662721893491124,
                        4.433734939759036, 1.0697399527186762, 0.10268378063010501, 1.032219570405728,
                        2.3714285714285714, 0.1724137931034483, 0.8281622911694511, 3.6964285714285716,
                        0.49842931937172774, 0.7265135699373695]
        list_result = [0.03538928210313448, 0.06656804733727811, 0.10268378063010501, 0.10316529894490035,
                       0.12179487179487179, 0.13141025641025642, 0.16271186440677965, 0.1724137931034483,
                       0.2206896551724138, 0.22169811320754718, 0.22783083219645292, 0.2326923076923077,
                       0.2850061957868649, 0.2949886104783599, 0.2953813104189044, 0.3316062176165803,
                       0.4189189189189189, 0.45769622833843016, 0.47963340122199594, 0.49349240780911063,
                       0.49842931937172774, 0.5397590361445783, 0.5881326352530541, 0.6078914919852034,
                       0.6473509933774835, 0.6640926640926641, 0.6653439153439153, 0.6927083333333334,
                       0.6952380952380952, 0.7041343669250646, 0.7107692307692308, 0.7265135699373695,
                       0.7355769230769231, 0.7595628415300546, 0.7870239774330042, 0.796711509715994,
                       0.8126721763085399, 0.8265895953757225, 0.8281622911694511, 0.8810289389067524,
                       0.8855291576673866, 0.8886576482830385, 0.907563025210084, 0.9337606837606838,
                       0.9671361502347418, 0.9697950377562028, 1.0, 1.017563117453348, 1.0232558139534884,
                       1.032219570405728, 1.0347938144329898, 1.0378681626928472, 1.046242774566474, 1.064207650273224,
                       1.0697399527186762, 1.0702947845804989, 1.1116279069767443, 1.1278350515463917,
                       1.1944444444444444, 1.2129760225669957, 1.2242225859247136, 1.2420212765957446,
                       1.244956772334294, 1.24597364568082, 1.418103448275862, 1.426183844011142, 1.4687022900763358,
                       1.4972067039106145, 1.5234113712374582, 1.606153846153846, 1.782312925170068, 1.7865853658536586,
                       1.8303571428571428, 1.9154078549848943, 1.919315403422983, 2.0780590717299576,
                       2.1864406779661016, 2.3714285714285714, 2.43731778425656, 2.4496314496314495, 2.6370967741935485,
                       2.6904761904761907, 2.6923076923076925, 3.0586080586080584, 3.061320754716981, 3.662721893491124,
                       3.6964285714285716, 3.823529411764706, 3.9306930693069306, 4.433734939759036, 4.474025974025974,
                       4.709677419354839, 5.061538461538461, 5.372781065088757, 8.45945945945946, 14.310344827586206,
                       16.0, 22.21875, 44.55555555555556, 864.0]
        test = 'Test11'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")


    def test12(self):
        list_current = [0, 100, 51, 58, 92, 12, 44, 63, 55, 34, 71]
        list_result = [0, 12, 34, 44, 51, 55, 58, 63, 71, 92, 100]
        test = 'Test12'
        self.assertEqual(sort_booble_sort(list_current), list_result, test + " по sort_booble_sort не пройден")
        self.assertEqual(sort_selection_sort(list_current), list_result, test + " по sort_selection_sort не пройден")
        self.assertEqual(sort_insertion_sort(list_current), list_result, test + " по sort_insertion_sort не пройден")
        self.assertEqual(sort_shaker_sort(list_current), list_result, test + " по sort_shaker_sort не пройден")
        self.assertEqual(sort_comb_sort(list_current), list_result, test + " по sort_comb_sort не пройден")
        self.assertEqual(sort_shell_sort(list_current), list_result, test + " по sort_shell_sort не пройден")
        self.assertEqual(sort_quick_sort(list_current), list_result, test + " по sort_quick_sort не пройден")
        self.assertEqual(sort_merge_sort(list_current), list_result, test + " по sort_merge_sort не пройден")
        self.assertEqual(sort_radix_sort(list_current), list_result, test + " по sort_radix_sort не пройден")

if __name__ == '__main__':
    unittest.main()
