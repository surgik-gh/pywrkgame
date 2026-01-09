# Publishing PyWRKGame to PyPI

This guide explains how to publish PyWRKGame 3.0.0 to the Python Package Index (PyPI).

## Prerequisites

1. **PyPI Account**: Create accounts on both:
   - Test PyPI: https://test.pypi.org/account/register/
   - Production PyPI: https://pypi.org/account/register/

2. **Install Build Tools**:
   ```bash
   pip install --upgrade build twine
   ```

3. **API Tokens**: Generate API tokens for authentication:
   - Test PyPI: https://test.pypi.org/manage/account/token/
   - Production PyPI: https://pypi.org/manage/account/token/

## Pre-Publishing Checklist

Before publishing, ensure:

- [ ] All tests pass (`python -m pytest tests/python -v`)
- [ ] C++ tests pass (`cd build && ctest --output-on-failure`)
- [ ] Version number is updated in:
  - [ ] `setup.py`
  - [ ] `pyproject.toml`
  - [ ] `CMakeLists.txt`
  - [ ] `README.md`
- [ ] CHANGELOG.md is updated with release notes
- [ ] README.md is up to date
- [ ] LICENSE file exists
- [ ] All documentation is current

## Building the Distribution

### 1. Clean Previous Builds

```bash
# Remove old build artifacts
rm -rf build/ dist/ *.egg-info
```

### 2. Build Source Distribution and Wheel

```bash
# Build distribution packages
python -m build
```

This creates:
- `dist/pywrkgame-3.0.0.tar.gz` (source distribution)
- `dist/pywrkgame-3.0.0-*.whl` (wheel distribution)

### 3. Verify the Build

```bash
# Check the distribution
twine check dist/*
```

## Testing on Test PyPI

Always test on Test PyPI before publishing to production:

### 1. Upload to Test PyPI

```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*
```

Enter your Test PyPI API token when prompted.

### 2. Test Installation

```bash
# Create a test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pywrkgame

# Test the installation
python -c "import pywrkgame; print(pywrkgame.__version__)"

# Deactivate and remove test environment
deactivate
rm -rf test_env
```

## Publishing to Production PyPI

Once testing is complete:

### 1. Upload to PyPI

```bash
# Upload to production PyPI
twine upload dist/*
```

Enter your PyPI API token when prompted.

### 2. Verify Installation

```bash
# Install from PyPI
pip install pywrkgame

# Verify
python -c "import pywrkgame; print(pywrkgame.__version__)"
```

### 3. Create GitHub Release

1. Go to https://github.com/your-org/pywrkgame/releases
2. Click "Draft a new release"
3. Tag version: `v3.0.0`
4. Release title: `PyWRKGame 3.0.0`
5. Add release notes from CHANGELOG.md
6. Attach distribution files from `dist/`
7. Publish release

## Using API Tokens

For automated publishing, configure `.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-API-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-API-TOKEN-HERE
```

**Security Note**: Never commit `.pypirc` to version control!

## Continuous Deployment

For automated releases via GitHub Actions, add these secrets:

- `PYPI_API_TOKEN`: Your PyPI API token
- `TEST_PYPI_API_TOKEN`: Your Test PyPI API token

Then create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine
      
      - name: Build package
        run: python -m build
      
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

## Post-Publishing

After successful publication:

1. **Announce the Release**:
   - Update project website
   - Post on social media
   - Notify community on Discord/forums

2. **Monitor**:
   - Check PyPI page: https://pypi.org/project/pywrkgame/
   - Monitor download statistics
   - Watch for issues and bug reports

3. **Update Documentation**:
   - Ensure installation instructions are current
   - Update version badges in README.md

## Troubleshooting

### Build Failures

If the build fails:
- Ensure all C++ dependencies are available
- Check that pybind11 is installed
- Verify CMake configuration is correct

### Upload Errors

Common upload errors:
- **403 Forbidden**: Check API token permissions
- **400 Bad Request**: Version already exists (increment version)
- **File already exists**: Remove old files from `dist/`

### Installation Issues

If users report installation problems:
- Check platform compatibility
- Verify dependencies are correctly specified
- Test on clean virtual environments

## Version Management

Follow Semantic Versioning (SemVer):
- **Major** (3.x.x): Breaking changes
- **Minor** (x.0.x): New features, backward compatible
- **Patch** (x.x.0): Bug fixes, backward compatible

## Support

For publishing issues:
- PyPI Support: https://pypi.org/help/
- Test PyPI: https://test.pypi.org/help/
- Packaging Guide: https://packaging.python.org/

---

**Remember**: Always test on Test PyPI first! Production releases cannot be deleted, only yanked.
