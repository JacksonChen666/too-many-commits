#!/bin/bash
cd "$(dirname "$0")"
commit() { git commit --allow-empty --no-edit -m "Commit no. $1" -q || ((c-=1)) }; c=$(git rev-list --all --count) && echo "$c"; while true ; do while [[ $(($c % 10000)) != 0 ]]; do ((c+=1)) && commit $c; done; echo $c; echo -en "Cleaning up..."; git gc --auto --force -q; echo -en "\r\033[K"; ((c+=1)); commit $c; done
