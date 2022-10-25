from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DistributionGraphs").getOrCreate()
#CSV

df_1_CSV= spark.read.format("csv").option("header", "true").option("sep", ",").load("data/YearSample.csv") 

#MonthDistribution

#fire.nodes.graph.NodeGraphMonthDistribution not yet implemented!.
#WeekDayDistribution

#fire.nodes.graph.NodeGraphWeekDayDistribution not yet implemented!.
#YearDistribution

#fire.nodes.graph.NodeGraphYearDistribution not yet implemented!.
