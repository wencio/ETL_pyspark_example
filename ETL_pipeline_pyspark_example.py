from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("ETL Pipeline Example") \
    .getOrCreate()

# Load CSV data
csv_file_path = "path/to/sales_data.csv"
sales_df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Load JSON data
json_file_path = "path/to/customer_data.json"
customer_df = spark.read.json(json_file_path)

# Perform join operation
joined_df = sales_df.join(customer_df, on="customer_id", how="inner")

# Filter data
filtered_df = joined_df.filter(joined_df.sales_amount > 1000)

# Aggregate data
aggregated_df = filtered_df.groupBy("customer_id").agg({"sales_amount": "sum"})
aggregated_df = aggregated_df.withColumnRenamed("sum(sales_amount)", "total_sales")

# Write the transformed data to a CSV file
output_path = "path/to/transformed_data.csv"
aggregated_df.write.csv(output_path, header=True)

# Stop Spark session
spark.stop()
