#!/bin/bash
hdfs dfs -rm -r /user/imdb/output/top10movies

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/imdb/input/imdb_top_1000.csv \
-output /user/imdb/output/top10movies \
-mapper ../scripts/top_movies_mapper.py \
-reducer ../scripts/top_movies_reducer.py \
-files ../scripts/top_movies_mapper.py \
-files ../scripts/top_movies_reducer.py

