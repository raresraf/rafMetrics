  998  python3 setup.py sdist bdist_wheel
  999  pip3 install -e .
 1007  python3 -m pip install --upgrade twine
 1009  python3 -m twine upload --repository testpypi dist/*
 1023  pip3 install -i https://test.pypi.org/simple/ rafmetrics==0.0.1

