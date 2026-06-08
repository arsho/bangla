# PyPI Package Update
## Update package repo

- Update the version in `pyproject.toml`.
- Update `Changelog.rst`.
- Commit and push.

## Build and upload to PyPI

- Install or upgrade build tools:

```bash
python -m pip install --upgrade build twine
```

- Clean old build files:

```bash
rm -rf build dist *.egg-info
```

- Build the package:

```bash
python -m build
```

- Check the package:

```bash
python -m twine check dist/*
```

- Upload to PyPI:

```bash
python -m twine upload dist/*
```

- Use the stored PyPI API token.