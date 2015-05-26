import cssx
import unittest

class TestCr(unittest.TestCase):
    def expect(self, source, expected):
        output = cssx.expand_expression(source)
        self.assertEqual(output, expected)

    def test_unparseables(self):
        self.expect('hi', 'hi')

    def test_display_block(self):
        self.expect('db', 'display: block;')

    def test_display_block_with_indent(self):
        self.expect('  db', '  display: block;')

    def test_unparseables_with_indent(self):
        self.expect('  hi', '  hi')

    def test_numeric(self):
        self.expect('m0', 'margin: 0;')

    def _test_multi_numeric(self):
        self.expect('m0 3px', 'margin: 0 3px;')

    def test_numeric_with_em_as_default_unit(self):
        self.expect('lh3', 'line-height: 3em;')

    def test_numeric_with_implied_unit(self):
        self.expect('w10', 'width: 10px;')

    def test_border_0(self):
        self.expect('b0', 'border: 0;')

    def test_skip_non_numeric_properties(self):
        self.expect('fw0', 'fw0')

    def test_numeric_negative_with_implied_value(self):
        self.expect('w-10', 'width: -10px;')

    def test_numeric_em_short(self):
        self.expect('m2m', 'margin: 2em;')

    def _test_numeric_em(self):
        self.expect('m2em', 'margin: 2em;')

    def _test_numeric_decimal_em(self):
        self.expect('m2.5m', 'margin: 2.5em;')

    def _test_auto_comma(self):
        self.expect('  font-weight: 400', '  font-weight: 400;')

class TestSpace(unittest.TestCase):
    def expect(self, source, expected):
        output = cssx.expand_property(source)
        self.assertEqual(output, expected)

    def test_simple(self):
        self.expect('m', 'margin:')

    def test_display(self):
        self.expect('d', 'display:')

    def test_display_fuzzying(self):
        self.expect('dis', 'display:')
        self.expect('disp', 'display:')
        self.expect('displ', 'display:')

    def test_alias_fuzzying(self):
        self.expect('bgcolor', 'background-color:')

    def _test_border(self):
        self.expect('bor', 'border:')

    def test_simple_2(self):
        self.expect('tt', 'text-transform:')

class TestBalanced(unittest.TestCase):
    def expect(self, input, expected):
        output = cssx.is_balanced_rule(input)
        self.assertEqual(output, expected)

    def test_simple(self):
        self.expect("margin: 0", True)

    def test_scale(self):
        self.expect("transform: scaleX(3)", True)

    def test_dont_double_semicolon(self):
        self.expect("font-weight: 400;", False)

    def test_hyphens(self):
        self.expect("font-weight: 400", True)

    def test_empty(self):
        self.expect("", False)

    def test_word(self):
        self.expect("xxx", False)

    def test_no_values(self):
        self.expect("font-weight: ", False)

    def test_unbalanced(self):
        self.expect("background: linear-gradient(to bottom", False)

if __name__ == '__main__':
    unittest.main()
