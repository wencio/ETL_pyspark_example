# Big Data ETL Pipeline using PySpark

## Overview

This project demonstrates how to create an ETL (Extract, Transform, Load) pipeline using PySpark. The pipeline extracts data from multiple sources (CSV and JSON), performs transformations (joining, filtering, and aggregating), and loads the transformed data into a data warehouse or data lake.

## Prerequisites

To run this project, you need to have the following installed on your machine:
- Python (3.6 or later)
- Apache Spark (3.x)
- PySpark

### Installing Dependencies

You can install the necessary Python packages using pip:

```bash
pip install pyspark
```

## Project Structure

- `etl_pipeline.py`: The main Python script that runs the ETL pipeline.

## Dataset

The datasets used in this project are hypothetical and represent sales data and customer information. They are stored in CSV and JSON formats, respectively.

## Running the Project

1. **Create a Spark Session**:
   The script starts by creating a Spark session to facilitate data processing.

2. **Extract Data**:
   The script extracts data from a CSV file (sales data) and a JSON file (customer data).

3. **Transform Data**:
   - **Join DataFrames**: Join the sales and customer data on a common key (`customer_id`).
   - **Filter Data**: Filter the joined data to include only relevant records (e.g., sales greater than a certain amount).
   - **Aggregate Data**: Aggregate the data to find total sales per customer.

4. **Load Data**:
   The transformed data is loaded into a data warehouse or data lake. For simplicity, the script writes the data to a CSV file.

### Example Code

Here is the complete code for the project:

```python
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
```

### Steps to Execute

1. **Clone the Repository**:
   If you have the script in a GitHub repository, clone it using:
   ```bash
   git clone https://github.com/yourusername/etl-pipeline-example.git
   cd etl-pipeline-example
   ```

2. **Run the Script**:
   Execute the Python script:
   ```bash
   python etl_pipeline.py
   ```

## Conclusion

This project demonstrates how to create a Big Data ETL pipeline using PySpark. The tasks include extracting data from multiple sources (CSV and JSON), performing transformations (joining, filtering, and aggregating), and loading the transformed data into a data warehouse or data lake. This example can be extended to include more complex transformations and data sources, such as databases or cloud storage.

## Resources

- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/index.html)
- [data.gov](https://www.data.gov/)
- [Apache Spark Documentation](https://spark.apache.org/documentation.html)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to the developers of PySpark and the open-source community for providing valuable tools and resources.
