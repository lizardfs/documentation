# Script to convert all files from rst to manpages using pandoc
for i in *.rst
do
/usr/local/bin/pandoc -s -f rst -t man $i > "${i/%.rst/}"
done
