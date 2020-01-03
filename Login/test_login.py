from Login.app import index


def test_index():
    ret_index_msg = index()
    assert ret_index_msg == "Hello, world!"
