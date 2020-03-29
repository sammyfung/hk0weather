rm -f hko9dayforecast.csv
scrapy crawl hko9dayforecast -t csv -o hko9dayforecast.csv --nolog
line_count=`wc -l hko9dayforecast.csv | cut -c 7-8`
if [ ${line_count} -eq " 0" ]
then
	exit 1
else
	exit 0
fi
