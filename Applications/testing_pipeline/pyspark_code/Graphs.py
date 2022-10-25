from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Graphs").getOrCreate()
#DatasetStructured

df = spark.read.csv("").option("header", True).option("sep", ",")
#GraphValues

#fire.nodes.graph.NodeGraphValues not yet implemented!.
