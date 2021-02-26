#!/bin/bash

download_link=https://github.com/ArjunSahlot/identify_num/archive/main.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/identify_num-main $1/identify_num \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/identify_num[0m"
