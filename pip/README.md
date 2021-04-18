# PIP instructions

```
python3 setup.py sdist bdist_wheel
pip3 install -e .
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
pip3 install -i https://test.pypi.org/simple/ rafmetrics==0.0.1
python3 -m twine upload dist/*
```
