"""Script to perform MNIST data pre-processing to prepare it for encoder
training.
"""
import argparse
import random
import pathlib
import sys

from ai4eosc_exercises import config


# Script arguments definition ---------------------------------------
parser = argparse.ArgumentParser(
    prog="PROG",
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="See '<command> --help' to read about a specific sub-command.",
)
parser.add_argument(
    "--debug", 
    action=argparse.BooleanOptionalAction,
    help="Sets the logging level (default: %(default)s)",
)
parser.add_argument(
    "output",
    help="Output folder for files (default: %(default)s)",
    type=pathlib.Path,
)


# Script command actions --------------------------------------------
def _run_command(output, **options):
    # Common operations
    pass

    # Generate dataset values
    values = [f"{x}" for x in range(config.DATA_SIZE)]
    random.shuffle(values)

    # Store values in a txt file
    with open(output, "w") as file:
        file.write(", ".join(values))

    # End of program
    pass

# Main call ---------------------------------------------------------
if __name__ == "__main__":
    try:
        args = parser.parse_args()
        _run_command(**vars(args))
    except TypeError as err:
        sys.exit(1)
    except Exception as err:
        sys.exit(1)
    sys.exit(0)
