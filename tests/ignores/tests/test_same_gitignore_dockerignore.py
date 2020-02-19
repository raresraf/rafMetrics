import difflib


def test_same_gitignore_dockerignore():
    with open('.gitignore', 'r') as hosts0:
        with open('.dockerignore', 'r') as hosts1:
            diff = difflib.unified_diff(
                hosts0.readlines(),
                hosts1.readlines(),
                fromfile='hosts0',
                tofile='hosts1',
            )
            for line in diff:
                assert line == None
