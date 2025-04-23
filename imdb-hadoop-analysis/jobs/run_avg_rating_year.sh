#!/bin/bash
hdfs dfs -rm -r /user/imdb/output/avg_rating_year

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/imdb/input/imdb_top_1000.csv \
-output /user/imdb/output/avg_rating_year \
-mapper ../scripts/avg_rating_year_mapper.py \
-reducer ../scripts/avg_rating_year_reducer.py \
-file ../scripts/avg_rating_year_mapper.py \
-file ../scripts/avg_rating_year_reducer.py

