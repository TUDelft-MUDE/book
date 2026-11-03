# Deactivate any active conda environment
conda deactivate 2>/dev/null || true

# Clear conda environment variables
unset CONDA_DEFAULT_ENV CONDA_PROMPT_MODIFIER 2>/dev/null || true

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
source venv/Scripts/activate

# Install required packages from requirements.txt and sphinx-autobuild
pip install -r requirements.txt sphinx-autobuild

# Build and serve the Sphinx documentation with auto-reload
# Opens browser automatically and ignores build artifacts and Python files
sphinx-autobuild book book/_build/html --open-browser --ignore "book/_build/**" --ignore "*.py" --ignore "book/references.bib" --ignore "book/_toc_with_local_paths.yml" --pre-build "bash sphinx-autobuild-prebuild.sh"