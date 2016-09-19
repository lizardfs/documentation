# Script to convert all files from rst to manpages using pandoc
for i in *.rst
do
/usr/local/bin/pandoc -s -f rst -t man $i | iconv -f utf-8 -tlatin1 > "${i/%.rst/}"
done
