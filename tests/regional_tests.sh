rm -f regional.csv
scrapy crawl regional -t csv -o regional.csv --nolog
line_count=`wc -l regional.csv | cut -c 7-8`
if [ ${line_count} -eq " 0" ]
then
	exit 1
else
	exit 0
fi
