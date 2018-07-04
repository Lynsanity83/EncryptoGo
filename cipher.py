from pycipher import ADFGX

class cipherADFGX():

    def __init__(self, text):
        super().__init__()
        self.text = text

        self.key = 'phqgmeaylnofdxkrcvszwbuti'
        self.keyword = 'MELON'

        self.settings = "'A', 'A', 'A'"

    def encipher(self):
        return ADFGX(self.key, self.keyword).encipher(self.text)
    def decipher(self):
        return ADFGX(self.key, self.keyword).decipher(self.text)

class cipherEnigma():

    def __init__(self, text):
        super().__init__()
        self.text = text

    def encipher(self):
        return ''

    def decipher(self):
        return ''