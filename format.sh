isort -y $(find moban_velocity -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 moban_velocity
black -l 79 tests
