import unittest
import mymodule

class TestRemoveTags(unittest.TestCase):
    def test_empty_input(self):
        inputString = ""
        self.assertEqual(mymodule.removeTags(inputString), "")

    def test_1(self):
        inputString = "<h2>     fetr fertgg     gh</h2>"
        self.assertEqual(mymodule.removeTags(inputString), "     fetr fertgg     gh")

    def test_one_tag(self):
        inputString = "<a></a>"
        output = mymodule.removeTags(inputString)
        self.assertEqual(output, "")

    def test_one_tag_with_spaces(self):
        inputString = "<a>    </a>"
        output = mymodule.removeTags(inputString)
        self.assertEqual(output, "    ")

    def test_one_tag_with_spaces_and_newlines(self):
        inputString = """<a>

</a>"""
        output = mymodule.removeTags(inputString)
        self.assertEqual(output, """

""")

    def test_lots_of_tags_with_spaces_and_newlines(self):
        inputString = """<a> TITLE
            POIRER
        </a><span>treter</span>"""
        output = mymodule.removeTags(inputString)
        expectedOutput = """ TITLE
            POIRER
        treter"""
        self.assertEqual(output, expectedOutput)

    def test_lots_of_tags_with_spaces_and_newlines_with_unicode(self):
        inputString = """<a> 日本語
            POIRER ひらがな <p>See for yourself</p>
        </a>"""
        output = mymodule.removeTags(inputString)
        expectedOutput = """ 日本語
            POIRER ひらがな See for yourself
        """
        self.assertEqual(output, expectedOutput)

class TestStringSpaces(unittest.TestCase):
    def test_empty_input(self):
        inputString = ""
        self.assertEqual(mymodule.stripSpaces(inputString), "")
    def test_1(self):
        inputString = "     fetr fertgg     gh"
        self.assertEqual(mymodule.stripSpaces(inputString), "fetr fertgg gh")



class TestMymodule(unittest.TestCase):

    def test_empty_input(self):
        inputString = ""
        self.assertEqual(mymodule.myfunction(inputString), "")

    def test_1(self):
        inputString = "<h2>     fetr fertgg     gh</h2>"
        self.assertEqual(mymodule.myfunction(inputString), "fetr fertgg gh")

    def test_one_tag(self):
        inputString = "<a></a>"
        output = mymodule.myfunction(inputString)
        self.assertEqual(output, "")

    def test_one_tag_with_spaces(self):
        inputString = "<a>    </a>"
        output = mymodule.myfunction(inputString)
        self.assertEqual(output, "")

    def test_one_tag_with_spaces_and_newlines(self):
        inputString = """<a>

         </a>"""
        output = mymodule.myfunction(inputString)
        self.assertEqual(output, "")

    def test_lots_of_tags_with_spaces_and_newlines(self):
        inputString = """<a> TITLE
            POIRER
        </a><span>treter</span>"""
        output = mymodule.myfunction(inputString)
        expectedOutput = "TITLE POIRER treter"
        self.assertEqual(output, expectedOutput)

    def test_lots_of_tags_with_spaces_and_newlines_with_unicode(self):
        inputString = """<a> 日本語
            POIRER ひらがな <p>See for yourself  </p>
        </a>"""
        output = mymodule.myfunction(inputString)
        expectedOutput = "日本語 POIRER ひらがな See for yourself"
        self.assertEqual(output, expectedOutput)
