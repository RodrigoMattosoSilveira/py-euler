import unittest
import helper.functions as f


class MyTestCase(unittest.TestCase):
    def test_compute_digits_sum(self):
        self.my_number = 1
        self.assertEqual(f.compute_digits_sum(self.my_number), 1)
        self.my_number = 3
        self.assertEqual(f.compute_digits_sum(self.my_number), 3)
        self.my_number = 11
        self.assertEqual(f.compute_digits_sum(self.my_number), 2)
        self.my_number = 18
        self.assertEqual(f.compute_digits_sum(self.my_number), 9)
        self.my_number = 111
        self.assertEqual(f.compute_digits_sum(self.my_number), 3)
        self.my_number = 999
        self.assertEqual(f.compute_digits_sum(self.my_number), 27)

    def test_get_multiples_of_three(self):
        self.my_number = 10
        multiples_of_three = [3, 6, 9]
        self.assertEqual(f.get_multiples_of_three(self.my_number), multiples_of_three)
        multiples_of_three = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
        self.my_number = 100
        self.assertEqual(f.get_multiples_of_three(self.my_number), multiples_of_three)

    def test_get_multiples_of_five(self):
        self.my_number = 10
        my_multiples = [0, 5]
        self.assertEqual(f.get_multiples_of_five(self.my_number), my_multiples)

        self.my_number = 100
        my_multiples = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
        self.assertEqual(f.get_multiples_of_five(self.my_number), my_multiples)

    def test_get_last_digit(self):
        self.my_number = 1
        self.assertEqual(f.get_last_digit(self.my_number), 1)
        self.my_number = 10
        self.assertEqual(f.get_last_digit(self.my_number), 0)
        self.my_number = 105
        self.assertEqual(f.get_last_digit(self.my_number), 5)

    def test_multipliers_sum(self):
        self.my_number = 10
        self.assertEqual(f.get_multipliers_sum(self.my_number), 23)
        self.my_number = 40
        self.assertEqual(f.get_multipliers_sum(self.my_number), 413)

    def test_valid_threes(self):
        my_multiples = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207, 210, 213, 216, 219, 222, 225, 228, 231, 234, 237, 240, 243, 246, 249, 252, 255, 258, 261, 264, 267, 270, 273, 276, 279, 282, 285, 288, 291, 294, 297, 300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357, 360, 363, 366, 369, 372, 375, 378, 381, 384, 387, 390, 393, 396, 399, 402, 405, 408, 411, 414, 417, 420, 423, 426, 429, 432, 435, 438, 441, 444, 447, 450, 453, 456, 459, 462, 465, 468, 471, 474, 477, 480, 483, 486, 489, 492, 495, 498, 501, 504, 507, 510, 513, 516, 519, 522, 525, 528, 531, 534, 537, 540, 543, 546, 549, 552, 555, 558, 561, 564, 567, 570, 573, 576, 579, 582, 585, 588, 591, 594, 597, 600, 603, 606, 609, 612, 615, 618, 621, 624, 627, 630, 633, 636, 639, 642, 645, 648, 651, 654, 657, 660, 663, 666, 669, 672, 675, 678, 681, 684, 687, 690, 693, 696, 699, 702, 705, 708, 711, 714, 717, 720, 723, 726, 729, 732, 735, 738, 741, 744, 747, 750, 753, 756, 759, 762, 765, 768, 771, 774, 777, 780, 783, 786, 789, 792, 795, 798, 801, 804, 807, 810, 813, 816, 819, 822, 825, 828, 831, 834, 837, 840, 843, 846, 849, 852, 855, 858, 861, 864, 867, 870, 873, 876, 879, 882, 885, 888, 891, 894, 897, 900, 903, 906, 909, 912, 915, 918, 921, 924, 927, 930, 933, 936, 939, 942, 945, 948, 951, 954, 957, 960, 963, 966, 969, 972, 975, 978, 981, 984, 987, 990, 993, 996, 999]
        baseline = 0
        self.my_number = 1000
        for i in my_multiples:
            baseline += 3
            self.assertEqual(i, baseline)

    def test_valid_fives(self):
        my_multiples = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600, 605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 680, 685, 690, 695, 700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790, 795, 800, 805, 810, 815, 820, 825, 830, 835, 840, 845, 850, 855, 860, 865, 870, 875, 880, 885, 890, 895, 900, 905, 910, 915, 920, 925, 930, 935, 940, 945, 950, 955, 960, 965, 970, 975, 980, 985, 990, 995]
        baseline = -5
        self.my_number = 1000
        for i in my_multiples:
            baseline += 5
            self.assertEqual(i, baseline)

    def test_is_last_digit_in_list(self):
        self.my_number = 1000
        self.assertEqual(f.is_last_digit_in_list(self.my_number), True)

        self.my_number = 1001
        self.assertEqual(f.is_last_digit_in_list(self.my_number), False)

        self.my_number = 1002
        self.assertEqual(f.is_last_digit_in_list(self.my_number), True)

        self.my_number = 1003
        self.assertEqual(f.is_last_digit_in_list(self.my_number), False)

        self.my_number = 1004
        self.assertEqual(f.is_last_digit_in_list(self.my_number), True)

        self.my_number = 1005
        self.assertEqual(f.is_last_digit_in_list(self.my_number), True)

        self.my_number = 1006
        self.assertEqual(f.is_last_digit_in_list(self.my_number), True)

        self.my_number = 1007
        self.assertEqual(f.is_last_digit_in_list(self.my_number), False)

        self.my_number = 1008
        self.assertEqual(f.is_last_digit_in_list(self.my_number), True)

        self.my_number = 1009
        self.assertEqual(f.is_last_digit_in_list(self.my_number), False)

    def test_is_three_a_factor(self):
        self.my_number = 333
        self.assertEqual(f.is_three_a_factor(self.my_number), True)

        self.my_number = 334
        self.assertEqual(f.is_three_a_factor(self.my_number), False)

        self.my_number = 335
        self.assertEqual(f.is_three_a_factor(self.my_number), False)

        self.my_number = 333333
        self.assertEqual(f.is_three_a_factor(self.my_number), True)

    def test_is_any_prime_a_factor(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        self.my_number = 333
        self.assertEqual(f.is_any_prime_a_factor(self.my_number, primes), True)

        self.my_number = 5555
        self.assertEqual(f.is_any_prime_a_factor(self.my_number, primes), True)

        self.my_number = 7777
        self.assertEqual(f.is_any_prime_a_factor(self.my_number, primes), True)

        self.my_number = 1331
        self.assertEqual(f.is_any_prime_a_factor(self.my_number, primes), True)

        self.my_number = 2197
        self.assertEqual(f.is_any_prime_a_factor(self.my_number, primes), True)

    def test_is_number_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        self.my_number = 941
        self.assertEqual(f.is_number_prime(self.my_number, primes), True)

        self.my_number = 942
        self.assertEqual(f.is_number_prime(self.my_number, primes), False)

    def test_is_palindrome(self):
        self.my_number = 9999
        self.assertEqual(f.is_palindrome(self.my_number), True)

        self.my_number = 998
        self.assertEqual(f.is_palindrome(self.my_number), False)

    def test_build_palindromic_numbers(self):
        self.start = 10
        self.end = 99
        self.assertEqual(f.build_palindromic_numbers(self.start, self.end), [99, 88, 77, 66, 55, 44, 33, 22, 11])


