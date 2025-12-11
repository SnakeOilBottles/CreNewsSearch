#!/bin/sh
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple CreNewsSearch
python -m unittest
pip3 uninstall -y CreNewsSearch
pip3 install CreNewsSearch
