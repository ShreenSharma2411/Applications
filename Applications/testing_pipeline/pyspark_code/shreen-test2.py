from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("shreen-test2").getOrCreate()
#Read CSV

df_1_ReadCSV= spark.read.format("csv").option("header", "true").option("sep", ",").load("\spark3\fire\data\creditcard.csv") 

#Drop Rows With Null

#fire.nodes.etl.NodeDropRowsWithNull not yet implemented!.
#Imputing With Constant

df_3_ImputingWithConstant=null.na.fill("", ["[Ljava.lang.String;@5bf04bbe"])
.na.fill("", ["[Ljava.lang.String;@5bf04bbe"])

#Flag Outlier

#fire.nodes.ml.NodeFlagOutlier not yet implemented!.
