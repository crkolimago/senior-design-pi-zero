echo "$1"
echo "$2"
obexftp -b "$1" -v -p "$2"
