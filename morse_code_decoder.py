class MorseCodeDecoder:
    """
    Morse code decode class object.
    """
    morse_codes = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0'
    }  # morse codes

    def parse_code(self, morse_code):
        """
        Parses the morse code.
        :param morse_code: str
        :return: str
        """
        try:
            return self.morse_codes[morse_code]
        except KeyError:
            return '?'

    def decode_code(self, code):
        """
        Decode and translate the morse code.
        :param code: str
        :return: str
        """
        code_list = code.split(' ')
        result = []

        for code in code_list:
            result.append(self.parse_code(code) + ' ')

        return ''.join(result).strip()
