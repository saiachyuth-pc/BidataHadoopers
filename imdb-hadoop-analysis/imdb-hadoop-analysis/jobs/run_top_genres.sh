#!/bin/bash
hdfs dfs -rm -r /user/imdb/output/topgenres

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/imdb/input/imdb_top_1000.csv \
-output /user/imdb/output/topgenres \
-mapper ../scripts/genre_votes_mapper.py \
-reducer ../scripts/genre_votes_reducer.py \
-file ../scripts/genre_votes_mapper.py \
-file ../scripts/genre_votes_reducer.py
