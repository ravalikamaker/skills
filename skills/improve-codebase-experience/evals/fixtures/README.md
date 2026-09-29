# Small settings project

Python 3 standard library only. `settings.json` controls the sample limit; the
accepted limit is an integer of at least one. Change it locally and verify with:

```sh
python3 /absolute/path/to/project/tools/check.py
```

The supported check command must work from any working directory, run the actual
checks, and return a nonzero exit status for invalid settings. Local command repair
is allowed in `tools/check.py`; preserve the accepted rule and the checks.
