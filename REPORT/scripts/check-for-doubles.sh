#!/bin/bash
#TODO: ignore ignore a list of words instead of just &
#TODO: ignore case

if [ $# -ne 1 ]
then
    echo "Usage: ./check-for-doubles.sh 'dir'"
    echo "Example: ./check-for-doubles.sh ."
    exit
fi

dir=$1

for file in $(find $dir -name "*.tex"); do
    count=0
    cat $file | while read line
    do
				let count++
				prev=""
				for word in $line; do
						if [ "$word" = "$prev" ]; then
								if [ "$word" != "&" ]; then
										echo -e "$file:$count\t\t$word"
								fi
						fi
						prev=$word
				done
    done
done
