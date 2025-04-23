#!/bin/bash

hdfs dfs -rm -r /user/imdb/output/genre_trends

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/imdb/input/imdb_top_1000.csv \
-output /user/imdb/output/genre_trends \
-mapper ../scripts/genre_trends_mapper.py \
-reducer ../scripts/genre_trends_reducer.py \
-file ../scripts/genre_trends_mapper.py \
-file ../scripts/genre_trends_reducer.py
