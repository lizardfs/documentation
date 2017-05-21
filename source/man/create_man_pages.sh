# Script to convert all files from rst to manpages using pandoc
mkdir -p manpages
for i in *.rst
do
/usr/local/bin/pandoc -s -f rst -t man $i | iconv -f utf-8 -t latin1 > "manpages/${i/%.rst/}"
done
