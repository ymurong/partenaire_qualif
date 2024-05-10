#!/bin/sh

NEW_VERSION=$1

# Define the function
update_version() {
    # New version number passed as the first argument


    # Check if a new version was provided
    if [ -z "$NEW_VERSION" ]; then
      echo "Usage: update_version <new-version>"
      return 1
    fi

    # File to update
    FILE="setup.py"

    # Use sed to find the version line and replace it with the new version number
    sed -i "s/version=['\"][0-9]*\.[0-9]*\.[0-9]*['\"]\,*/version='$NEW_VERSION',/" $FILE

    echo "Updated version in $FILE to $NEW_VERSION"
}
# update version in setup python file
update_version

# build the project
rm -rf build dist partenaire_qualif.egg-info
python setup.py sdist bdist_wheel

# upload the project
python -m twine upload dist/*