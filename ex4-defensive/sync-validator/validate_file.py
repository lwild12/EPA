"""Command-line script: check one request file with the validator.

Usage : python validate_file.py samples/good.json
Output: OK   or   REJECTED: <field>
Exit  : 0 accepted, 1 rejected, 2 file problem (missing, not a normal file, unreadable)

The file is treated as untrusted: only a normal file is opened and at most MAX_BODY + 1
bytes are read, so a huge file cannot use up memory.
"""
import os
import sys

from sync_validator import MAX_BODY, ValidationError, validate


def main(argv):
    if len(argv) != 2:
        print("usage: python validate_file.py <request.json>")
        return 2
    path = argv[1]
    if not os.path.isfile(path):                 # refuses folders, devices and missing files
        print("ERROR: not a readable file")
        return 2
    try:
        with open(path, "rb") as handle:
            raw = handle.read(MAX_BODY + 1)      # never read more than one byte past the limit
    except OSError:
        print("ERROR: cannot read file")
        return 2
    try:
        validate(raw)
    except ValidationError as err:
        print(f"REJECTED: {err}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
