"""
Useful script for pointing the example recipes to a custom temporary directory
Will just swap all "workingdir" parameters for the user input
"""

import argparse
from pathlib import Path
import json
import logging
import os

from nested_lookup import nested_lookup, nested_update


def set_directory(recipe: Path, working_directory: str):
    """Set all the workingdir parameters to the working_directory provided"""

    # Read json in
    try:
        Path(working_directory)
        with open(recipe, "r") as recipe_file:
            recipe_json = json.load(recipe_file)
            # print(recipe_json)
            # Check that the working directory parameter exists
            assert nested_lookup(
                "workingdir", recipe_json
            ), f"Did not find occurences of 'workingdir' in {recipe}"
        # Open file for writing
        with open(recipe, "w") as recipe_file:
            # Get updated recipe
            updated_recipe_json = nested_update(
                recipe_json, "workingdir", str(working_directory)
            )
            try:
                json.dump(updated_recipe_json, recipe_file, indent=4)
            except:
                logging.error(f"Issue putting updated value in {recipe}")
                # Clear output and put back the original recipe
                recipe_file.seek(0)
                recipe_file.truncate()
                json.dump(recipe_json, recipe_file, indent=4)
                raise
    except TypeError as e:
        logging.error(
            f"Expected file path as working directory, got {working_directory}\n{e}"
        )
        raise
    except (FileNotFoundError, PermissionError) as e:
        logging.error(f"Could not load json from {recipe}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid json found in {recipe}\n{e}")
        raise
    except AssertionError as e:
        logging.error(e)
        raise


def main():

    parser = argparse.ArgumentParser(
        description="This script is designed to set up the example recipes for you. "
        "Provide a working directory which you can access and all of the "
        "example recipes will use that as their working directory to "
        "output files and logs to."
    )
    parser.add_argument(
        "working_directory",
        type=Path,
        help="set recipes working directories to this path (should be accessible to your user account)",
    )
    parser.add_argument(
        "--recipes",
        type=str,
        nargs="+",
        help="optionally add list of recipes to change",
    )

    args = parser.parse_args()

    if args.recipes:
        recipes = args.recipes
    else:
        recipes = [
            f
            for f in Path(os.path.realpath(__file__)).parent.iterdir()
            if f.suffix == ".json"
        ]

    error_count = 0
    for rec in recipes:
        try:
            set_directory(rec, args.working_directory)
        except:
            error_count += 1

    if error_count:
        print(f"Problems in {error_count} of {len(recipes)} recipes parsed")
    else:
        print(f"All recipes updated with workingdir of {args.working_directory}")


if __name__ == "__main__":
    main()
