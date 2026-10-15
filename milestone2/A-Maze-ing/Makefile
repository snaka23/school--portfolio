# 変数定義
PYTHON			:= python3
MAIN_SCRIPT		:= a_maze_ing.py
CONFIG_FILE		:= config.txt
LINT_TARGETS		:= .

MYPY_FLAGS		:= --explicit-package-bases \
					--warn-return-any \
					--warn-unused-ignores \
					--ignore-missing-imports \
					--disallow-untyped-defs \
					--check-untyped-defs

.PHONY: all install run debug lint lint-strict clean fclean re

all:	run

install:
		$(PYTHON) -m pip install --upgrade pip
		$(PYTHON) -m pip install "mypy>=2.1.0" "flake8>=7.3.0" "build>=1.5.0"

run:
		$(PYTHON) $(MAIN_SCRIPT) $(CONFIG_FILE)

debug:
		$(PYTHON) -m pdb $(MAIN_SCRIPT) $(CONFIG_FILE)

lint:
		@echo "==> Running flake8..."
		flake8 $(LINT_TARGETS)
		@echo "==> Running mypy..."
		mypy $(MYPY_FLAGS) $(LINT_TARGETS)

lint-strict:
		@echo "==> Running flake8..."
		flake8 $(LINT_TARGETS)
		@echo "==> Running mypy (Strict)..."
		mypy $(MYPY_FLAGS) --strict $(LINT_TARGETS)

clean:
		@echo "==> Cleaning cache files... "
		@find . -type d -name "__pycache__" -exec rm -rf {} +
		@find . -type d -name ".mypy_cache" -exec rm -rf {} +
		@find . -type d -name ".pytest_cache" -exec rm -rf {} +
		@find . -type f -name "*.pyc" -delete 
		@rm -rf __pycache__ .mypy_cache .pytest.cache *.egg-info build dist

fclean:		clean

re:	fclean all