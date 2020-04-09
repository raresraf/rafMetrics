from tools.js_beautify.js_beautify import opts


def test_jsbeautifier_driver():
    assert opts.indent_size == 2
