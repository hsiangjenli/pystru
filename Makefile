clean:
	rm -r -f test
	rm -r -f pystru.egg-info
	rm -r -f build


dev:
	rm -r -f test
	mkdir test
	rm -r -f pystru.egg-info
	rm -r -f build
	pip install .
	cd test; pystru create --type basic --name test --demo True


pypi:
	python setup.py sdist --formats=zip
	twine check dist/*


upload:
	python setup.py sdist --formats=zip
	twine upload dist/*

serve:
	cp README.md docs/index.md
	mkdocs serve