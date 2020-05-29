if [ $# -ne 1 ]
then
    echo "Syntax: ${0} SPIDER_NAME"
    exit 1
else
    SPIDER=${1}
    scrapy list | grep ${SPIDER} > /dev/null
    if [ $? -ne 0 ]
    then
        echo "Error: Spider ${SPIDER} is not found."
        exit 1
    fi
fi

OSTYPE=`uname`

rm -f ${SPIDER}.csv
scrapy crawl ${SPIDER} -t csv -o ${SPIDER}.csv --nolog

if [ ${OSTYPE} = "Linux" ]
then
    line_count=`wc -l ${SPIDER}.csv | cut -f 1 -d ' '`
    if [ ${line_count} = "0" ]
    then
        wc -l ${SPIDER}.csv
        exit 1
    else
        exit 0
    fi
elif [ ${OSTYPE} = "Darwin" ]
then
    line_count=`wc -l ${SPIDER}.csv | cut -c 7-8`
    if [ "${line_count}" = " 0" ]
    then
        wc -l ${SPIDER}.csv
        exit 1
    else
        exit 0
    fi
fi