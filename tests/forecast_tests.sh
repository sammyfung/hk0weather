rm -f hkoforecast.csv
scrapy crawl hkoforecast -t csv -o hkoforecast.csv --nolog
line_count=`wc -l hkoforecast.csv | cut -c 7-8`
if [ ${line_count} -eq " 0" ]
then
	exit 1
else
	exit 0
fi
