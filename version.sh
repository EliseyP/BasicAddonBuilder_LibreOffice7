#!/usr/bin/env bash

MAJOR="0"
MINOR="6"
MICRO="9"

SRC="src"
UPDATE="BasicAddonBuilder_LO.update.xml" 
README="README.md"

if [[ -z "$1" ]]; then
  grep_upd=`egrep -o '0\.[0-9]+\.[0-9]+' $UPDATE`
  grep_src=`egrep -oh '0\.[0-9]+\.[0-9]+' -R $SRC`
  grep_readme=`egrep -o '0\.[0-9]+\.[0-9]+' $README`
  (echo "$grep_upd"; echo "$grep_src"; echo "$grep_readme") |  sort -u

elif [[ $1 == '-v' ]]; then
  echo "Set version to: $MAJOR.$MINOR.$MICRO"
  find src -type f -exec sed -i -re "s/([$MAJOR]\.[$MINOR])\.[^$MICRO]/\1.$MICRO/g" {} \;
  sed -i -re "s/([$MAJOR]\.[$MINOR])\.[^$MICRO]/\1.$MICRO/g" $UPDATE
  sed -i -re "s/([$MAJOR]\.[$MINOR])\.[^$MICRO]/\1.$MICRO/g" $README
fi






#sed -i -re 's/(0\.6\.)[^7]/\17/g' $UPDATE
