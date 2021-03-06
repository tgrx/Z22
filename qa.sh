#!/usr/bin/env bash

# ---------------------------------------------------------
abort() {
  if test -n "$1"; then
    echo >&2 -e "\n\nFAILED: $1\n\n"
  fi
  exit 1
}

trap 'abort' 0

set -e
set -o pipefail

# ---------------------------------------------------------

function contains() {
    local n=$#
    local value=${!n}
    for ((i=1; i < $#; i++)) {
        if [ "${!i}" == "${value}" ]; then
            echo "y"
            return 0
        fi
    }
    echo "n"
    return 1
}

assert_names() {
  dir_names=$(ls -d homeworks/* | sed -e 's/homeworks\///g')
  github_names=(
    "aleksey_gukov"
    "alexander_sidorov"
    "alexei_rakhmanko"
    "anastasia_husainova"
    "evgeni_gazin"
    "gleb_kovalchuk"
    "ilya_nilov"
    "kirill_revenko"
    "kirill_shevchuk"
    "nikita_marchenkov"
    "polina_korolenko"
    "vladimir_lepeshko"
    "yan_romanovich"
  )

  for n in ${dir_names}; do
    if [[ $n == "__init__.py" ]]; then
      continue;
    fi

    if [[ $(contains "${github_names[@]}" "$n") == "n" ]]; then
      echo "unknown Github name in homeworks/: '$n'"
      return 1
    fi

    pkg_init_py="homeworks/$n/__init__.py"
    if [[ ! -f $pkg_init_py ]]; then
      echo "File $pkg_init_py MUST be added"
      return 1
    fi
  done
}

# ---------------------------------------------------------

rm -rf homeworks/__pycache__

# checks

assert_names || abort "MESS WITH HOMEWORKS USERS"

pipenv run pytest homeworks/ || abort "PYTEST IS NOT HAPPY"
pipenv run pytest lessons/ || abort "ALEX'S TESTS ARE NOT HAPPY"
pipenv run black --check . || abort "BLACK IS NOT HAPPY"
pipenv run flake8 || abort "FLAKE8 IS NOT HAPPY"
pipenv run pylint homeworks/ lessons/ || abort "PYLINT IS NOT HAPPY"


# ---------------------------------------------------------
trap : 0
# ---------------------------------------------------------
