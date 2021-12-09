import unittest

from morse_code_decoder import MorseCodeDecoder


class TestMorseCodeDecoder(unittest.TestCase):
    morse_codes_test_list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                             '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--',
                             '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.',
                             '-----']

    morse_incorrect_result_list = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN',
                                   'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ', '11', '22',
                                   '33', '44', '55', '66', '77', '88', '99', '1010']

    morse_decoded_result_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                                 '9', '10']

    code_hello_friend = '.... . .-.. .-.. --- ..-. .-. .. . -. -..'
    code_cesar_labs = '-.-. . ... .- .-. .-.. .- -... ...'
    code_i_am_hired = '.. .- -- .... .. .-. . -..'

    def setUp(self):
        self.morse_decoder = MorseCodeDecoder()

    def test_data_correction(self):
        correct_count = 0

        for i in range(len(self.morse_codes_test_list)):
            try:
                if self.morse_decoded_result_list[i] == self.morse_decoder.decode_code(self.morse_codes_test_list[i]):
                    correct_count += 1
            except AssertionError as error:
                print(error)

        self.assertEqual(
            len(self.morse_codes_test_list),
            correct_count,
            'test data correction is not equal'
        )

    def test_incorrect_result(self):
        correct_count = 0

        for i in range(len(self.morse_codes_test_list)):
            try:
                assert self.morse_incorrect_result_list[i] == self.morse_decoder.decode_code(
                    self.morse_codes_test_list[i])
                correct_count += 1
            except AssertionError as error:
                print(error)

        self.assertEqual(0, correct_count, 'test result is not incorrect')

    def test_decode_hello_friend(self):
        expected_result = 'H E L L O F R I E N D'
        self.assertEqual(
            expected_result,
            self.morse_decoder.decode_code(self.code_hello_friend),
            'test decode "hello friend" is not the expected'
        )

    def test_decode_cesar_labs(self):
        expected_result = 'C E S A R L A B S'
        self.assertEqual(
            expected_result,
            self.morse_decoder.decode_code(self.code_cesar_labs),
            'test decode "cesar labs" is not the expected'
        )

    def test_decode_i_am_hired(self):
        expected_result = 'I A M H I R E D'
        self.assertEqual(
            expected_result,
            self.morse_decoder.decode_code(self.code_i_am_hired),
            'test decode "i am hired" is not the expected'
        )
