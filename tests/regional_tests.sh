scrapy crawl regional -t csv -o test.csv
line_count=`wc -l test.csv | cut -c 7-8`
if [ ${line_count} -eq " 0" ]
then
	exit 1
else
	exit 0
fi
