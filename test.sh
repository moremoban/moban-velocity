pip freeze
nosetests --with-coverage --cover-package moban_velocity --cover-package tests tests  docs/source moban_velocity && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
