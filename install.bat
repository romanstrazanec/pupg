@echo off

rm -rf build
rm -rf dist
rm -rf src/*.egg-info
py -m build
twine upload dist/*
