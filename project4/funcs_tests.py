# Name:       Acacia Moran
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Project 1
# Term:       Spring 2017

import unittest
import finder_funcs

class TestCases(unittest.TestCase):
    
    
    def test_get_row_1(self):
        puzzle_string = ("aklstgbv"
        "cdanhgfdsewdnjh"
        "ygtvfsnpokjiuhg"
        "tvnkmlpoihygjhg"
        "fdswertnbvcfghy"
        "trmjngfdwstrnkh"
        "ygtfdrejkiolkmngt")

        self.assertEqual(finder_funcs.get_row(puzzle_string, 0, 10),\
                          "aklstgbvcd")
    
    def test_get_row_2(self):
        puzzle_string = ("aklstgbvcdanhgfdsewdnjhygtvfsnpokjiuhgtvn"
                        "kmlpoihygjhgfdswertnbvcfghytrmjngfdwstrnkhy"
                        "gtfdrejkiolkmngt")

        self.assertEqual(finder_funcs.get_row(puzzle_string, 90, 100),\
                         "jkiolkmngt")
    
    def test_get_row_3(self):
        puzzle_string = ("aklstgbvcdanhgfdsewdnjhygtvfsnpokjiuhgtvn"
                        "kmlpoihygjhgfdswertnbvcfghytrmjngfdwstrnkhy"
                        "gtfdrejkiolkmngt")

        self.assertEqual(finder_funcs.get_row(puzzle_string, 10, 20),\
                         "anhgfdsewd")
    
    
    def test_get_rows_1(self):
        puzzle_string = ("aklstgbvcdanhgfdsewdnjhygtvfsnpokjiuhgtvnkmlpoihygjh"
                        "gfdswertnbvcfghytrmjngfdwstrnkhygtfdrejkiolkmngt")
        self.assertEqual(finder_funcs.get_rows(puzzle_string), \
                        ["aklstgbvcd", "anhgfdsewd",\
                         "njhygtvfsn", "pokjiuhgtv", "nkmlpoihyg",\
                         "jhgfdswert",\
                         "nbvcfghytr", "mjngfdwstr", "nkhygtfdre","jkiolkmngt"])

    def test_get_rows_2(self):
        puzzle_string = ("acsstgbvcdanhgfdsewdnjhygtvfsnpokjiu"
                        "hgtvnkmlpoihygjhgfdswertnbvcfghytrmjng"
                        "fdwstrnkhygtfdrekliolkmngt")
        self.assertEqual(finder_funcs.get_rows(puzzle_string),\
                          ["acsstgbvcd", "anhgfdsewd", "njhygtvfsn",\
                           "pokjiuhgtv", "nkmlpoihyg", "jhgfdswert",\
                           "nbvcfghytr", "mjngfdwstr", "nkhygtfdre",\
                           "kliolkmngt"])
    
    def test_get_rows_3(self):
        puzzle_string = ("ffffffffffffffffffffffffffffffffffffffff"
                        "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
        self.assertEqual(finder_funcs.get_rows(puzzle_string), (["ffffffffff", "ffffffffff", "ffffffffff", "ffffffffff", "ffffffffff", 
                                                                "ffffffffff", "ffffffffff", "ffffffffff", "ffffffffff", "ffffffffff"]))


    def test_get_column_1(self):
        puzzle_string = ("acsstgbvcdanhgfdsewdnjhygtvfsnpok"
                        "jiuhgtvnkmlpoihygjhgfdswertnbvcfgh"
                        "ytrmjngfdwstrnkhygtfdrekliolkmngt")
        self.assertEqual(finder_funcs.get_column(puzzle_string, 0),\
                         "aanpnjnmnk")
    
    def test_get_column_2(self):
        puzzle_string = ("acsstgbvcdanhgfdsewdnjhygtvfsnpokjiuhgtvn"
                        "kmlpoihygjhgfdswertnbvcfghytrmjngfdwstrnkhy"
                        "gtfdrekliolkmngt")
        self.assertEqual(finder_funcs.get_column(puzzle_string, 1),\
                         "cnjokhbjkl")
    
    def test_get_column_3(self):
        puzzle_string = ("acsstgbvcdanhgfdsewdnjhygtvfsnpokjiuhgtvnkm"
                        "lpoihygjhgfdswertnbvcfghytrmjngfdwstrnkhygtfd"
                        "rekliolkmngt")
        self.assertEqual(finder_funcs.get_column(puzzle_string, 9),\
                         "ddnvgtrret")


    def test_get_columns_1(self):
        puzzle_string = ("acsstgbvcdanhgfdsewdnjhygtvfsnpokjiuhgtvnk"
                        "mlpoihygjhgfdswertnbvcfghytrmjngfdwstrnkhygt"
                        "fdrekliolkmngt")
        self.assertEqual(finder_funcs.get_columns(puzzle_string),\
                        ["aanpnjnmnk", "cnjokhbjkl", "shhkmgvnhi","sgyjlfcgyo",\
                         "tfgipdffgl", "gdtuosgdtk", "bsvhiwhwfm", "vefgheysdn", \
                         "cwstyrttrg", "ddnvgtrret"])
    
    def test_get_columns_2(self):
        puzzle_string = ("fcsstgbvcdanhgfdsewdnjhygtvfsnpokjiuhgtvnkmlp"
                        "oihygjhgfdswertnbvcfghytrmjngfdwstr"
                        "nkhygtfdrekliolkmngg")
        self.assertEqual(finder_funcs.get_columns(puzzle_string), ["fanpnjnmnk", "cnjokhbjkl"\
                        , "shhkmgvnhi", "sgyjlfcgyo", "tfgipdffgl", "gdtuosgdtk", "bsvhiwhwfm",\
                        "vefgheysdn", "cwstyrttrg", "ddnvgtrreg"])
    
    def test_get_columns_3(self):
        puzzle_string = ("assstgbvsdanhgfdsewdnjhygtvfsnpokjiuhgtv"
                        "nkmlpoihygjhgfdswertnbvcfghytrmjngfdwstrnk"
                        "hygtfdrekliolhmngt")
        self.assertEqual(finder_funcs.get_columns(puzzle_string),\
                        ["aanpnjnmnk", "snjokhbjkl", "shhkmgvnhi",\
                        "sgyjlfcgyo",\
                         "tfgipdffgl", "gdtuosgdth", "bsvhiwhwfm",\
                         "vefgheysdn" ,\
                         "swstyrttrg", "ddnvgtrret"])

    
    def test_reverse_word_1(self):
        word = 'hello'
        self.assertEqual(finder_funcs.reverse_word(word), 'olleh')
    
    def test_reverse_word_2(self):
        word = 'acacia'
        self.assertEqual(finder_funcs.reverse_word(word), 'aicaca')
    
    def test_reverse_word_3(self):
        word = 'going'
        self.assertEqual(finder_funcs.reverse_word(word), 'gniog')

    
    def test_row_check_1(self):
        word = 'assist'
        row = 'assistbvsd'
        self.assertEqual(finder_funcs.row_check(word, row), (0, -1))
    
    def test_row_check_2(self):
        word = 'got'
        row = 'jkutoghju'
        self.assertEqual(finder_funcs.row_check(word, row), (-1, 5))
    
    def test_row_check_3(self):
        word = 'got'
        row = 'gottoghju'
        self.assertEqual(finder_funcs.row_check(word, row), (0, 5))

    
    def test_rows_check_1(self):
        word = 'katie'
        puzzle_string = ("acsstgbvcdkatiedsewdnjhygtvfsn"
                        "pokjiuhgtvnkmlpoihygjhgfdswertn"
                        "bvcfghytrmjngfdwstrnkhygtfdrekliolkmngt")
        self.assertEqual(finder_funcs.rows_check(puzzle_string, word),\
                         (1, 0, 'FORWARD'))
    
    def test_rows_check_2(self):
        word = 'acacia'
        puzzle_string = ("acaciabvcdkatiedsewdnjhygtvfsnpok"
                        "jiuhgtvnkmlpoihygjhgfdswertnbvcfgh"
                        "ytrmjngfdwstrnkhygtfdrekliolkmngt")
        self.assertEqual(finder_funcs.rows_check(puzzle_string, word),\
                        (0, 0, 'FORWARD'))
    
    def test_rows_check_3(self):
        word = 'row'
        puzzle_string = ("acsstgbvcdkatiedsewdnjhygtvfsnpok"
                        "jiuhgtvnkmlpoihygjhgfdswertnbvcfghy"
                        "trmjngfdwstrnkhygtfdrekliolkmwor")
        self.assertEqual(finder_funcs.rows_check(puzzle_string, word),\
                         (9, 9, 'BACKWARD'))

    
    def test_column_check_1(self):
        word = 'got'
        column = 'gottoghju'
        self.assertEqual(finder_funcs.row_check(word, column), (0, 5))
    
    def test_column_check_2(self):
        word = 'meow'
        column = 'gotmeowhju'
        self.assertEqual(finder_funcs.row_check(word, column), (3, -1))
    
    def test_column_check_3(self):
        word = 'me'
        column = 'emttogmeu'
        self.assertEqual(finder_funcs.row_check(word, column), (6, 1))
    
    
    def test_columns_check_1(self):
        word = 'katie'
        puzzle_string = ("kcsstgbvcdaatiedsewdtjhygtvfsnii"
                         "kjiuhgtvekelpoihygjhgfdswertnbvcf"
                         "ghytrmjngfdwstrnkhygtfdrekliolkmngt")
        self.assertEqual(finder_funcs.columns_check(puzzle_string, word),\
                         (0, 0, 'DOWN'))
    
    def test_columns_check_2(self):
        word = 'cat'
        puzzle_string = ("kcsstgbvcdcatiedsewdajhyg"
                        "tvfsntikjiuhgtvekelpoihygj"
                        "hgfdswertnbvcfghytrmjngfdwstrnkhygtfdrekliolkmngt")
        self.assertEqual(finder_funcs.columns_check(puzzle_string, word),\
                         (1, 0, 'DOWN'))

    def test_columns_check_3(self):
        word = 'puzzle'
        puzzle_string = ("kcsstgbvcdaatiedsewdtjhygtvfsni"
                         "ikjiuhgtvekelpoihgejhgfdswetlnbv"
                         "cfghytzmjngfdwstznkhygtfdrukliolkmngp")
        self.assertEqual(finder_funcs.columns_check(puzzle_string, word),\
                         (9, 9, 'UP'))
    
    def test_wordsearch_1(self):
        puzzle_string = ("kcsstgbvcdaatiedsewdtjhygtvf"
                        "sniikjiuhgtvekelpoihgejhgfdsw"
                        "etlnbvcfghytzmjngfdwstznkhygtfdrukliolkmngp")
        word = "puzzle"
        self.assertEqual(finder_funcs.wordsearch(puzzle_string, word),\
                        (9, 9, 'UP'))
    
    def test_wordsearch_2(self):
        puzzle_string = ("ccsstgbvcdaatiedsewdtjhygtvfsnii"
                        "kjiuhgtvekelpoihgejhgfdswetlnbvcf"
                        "ghytzmjngfdwstznkhygtfdrukliolkmngp")
        word = "cat"
        self.assertEqual(finder_funcs.wordsearch(puzzle_string, word),\
                         (0, 0, 'DOWN'))
    
    def test_wordsearch_3(self):
        puzzle_string = ("kidstgbvcdaatiedsewdtjhygtvfs"
                         "niikjiuhgtvekelpoihgejhgfdswet"
                         "lnbvcfghytzmjngfdwstznkhygtfdrukliolkmngp")
        word = "kid"
        self.assertEqual(finder_funcs.wordsearch(puzzle_string, word),\
                        (0, 0, 'FORWARD'))
    
    def test_wordsearch_4(self):
        puzzle_string = ("tacstgbvcdaatiedsewdtjhygtv"
                        "fsniikjiuhgtvekelpoihgejhgfd"
                        "swetlnbvcfghytzmjngfdwstznkhygtfdrukliolkmngp")
        word = "cat"
        self.assertEqual(finder_funcs.wordsearch(puzzle_string, word),\
                         (0, 2, 'BACKWARD'))
    
    def test_wordsearch_5(self):
        puzzle_string = ("ccsstgbvcdaatiedsewdtjhygtvfsn"
                        "iikjiuhgtvekelpoihgejhgfdswetln"
                        "bvcfghytzmjngfdwstznkhygtfdrukliolkmngp")
        word = "hello"
        self.assertEqual(finder_funcs.wordsearch(puzzle_string, word), None)
    
                
if __name__ == "__main__":
    unittest.main()
