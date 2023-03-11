clean:
	rm -r -f pystru.egg-info
	rm -r -f build
dev:
	pip install .

pypi:
	python setup.py sdist --formats=zip
	twine check dist/*

upload:
	python setup.py sdist --formats=zip
	twine upload dist/*