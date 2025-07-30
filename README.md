# DuckDB-DuckLake Integration Project

A demonstration project showcasing DuckDB's multi-dataframe ecosystem integration, featuring seamless interoperability between pandas, Polars, and PySpark dataframes using DuckDB's DuckLake storage format.

## Overview

This project demonstrates how to leverage DuckDB's powerful analytical capabilities while working with multiple popular Python data processing libraries. It showcases the ability to:

- Store data in DuckDB's DuckLake format for efficient columnar storage
- Convert seamlessly between pandas, Polars, and PySpark dataframes
- Perform SQL operations on data using DuckDB's high-performance engine
- Utilize DuckDB's experimental Spark SQL compatibility layer

## Features

- **Multi-library Integration**: Work with pandas, Polars, and PySpark dataframes interchangeably
- **DuckLake Storage**: Efficient columnar storage format optimized for analytics
- **SQL Interface**: Execute SQL queries directly on your data
- **Zero-copy Operations**: Efficient data transfers between different dataframe libraries
- **Spark Compatibility**: Use familiar Spark SQL syntax with DuckDB's performance

## Prerequisites

- Python 3.11 or higher
- uv package manager (recommended) or pip

## Installation

### Using uv (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd duckdb-ducklake

# Install dependencies using uv
uv sync
```

### Using pip

```bash
# Clone the repository
git clone <repository-url>
cd duckdb-ducklake

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Dependencies

- **duckdb**: High-performance analytical database
- **pandas**: Data manipulation and analysis library
- **polars**: Fast dataframes library with lazy evaluation
- **pyspark**: Python API for Apache Spark
- **typing-extensions**: Enhanced typing support

## Usage

### Basic Example

Run the main demonstration script:

```bash
# Using uv
uv run python main.py

# Or if using activated virtual environment
python main.py
```

### Code Example

```python
import duckdb
import pandas as pd
import polars as pl
from duckdb.experimental.spark.sql import SparkSession as session
from duckdb.experimental.spark.sql.functions import lit, col

# Create Spark session
spark = session.builder.getOrCreate()

# Connect to DuckLake database
with duckdb.connect("ducklake:my_ducklake.db") as con:
    # Create and populate table
    con.sql("CREATE TABLE IF NOT EXISTS my_table (id INTEGER, name VARCHAR, age INTEGER)")
    con.sql("INSERT INTO my_table VALUES (1, 'John', 25), (2, 'Charlie', 32)")

    # Query and convert to different dataframe formats
    pandas_df = con.sql("SELECT * FROM my_table").df()
    polars_df = con.sql("SELECT * FROM my_table").pl()
    pyspark_df = spark.createDataFrame(pandas_df)
```

## Project Structure

```
duckdb-ducklake/
├── README.md                 # Project documentation
├── main.py                   # Main demonstration script
├── pyproject.toml           # Project configuration and dependencies
├── uv.lock                  # Locked dependency versions
├── .python-version          # Python version specification
├── .gitignore              # Git ignore rules
├── .venv/                  # Virtual environment (created after installation)
├── my_ducklake.db          # DuckDB database file
└── my_ducklake.db.files/   # DuckLake storage files
```

## Key Concepts

### DuckLake Format
DuckLake is DuckDB's columnar storage format that provides:
- Efficient compression
- Fast analytical queries
- ACID transactions
- Schema evolution support

### Multi-Dataframe Ecosystem
This project demonstrates DuckDB's ability to work with:
- **Pandas**: Traditional dataframes with rich ecosystem
- **Polars**: High-performance dataframes with lazy evaluation
- **PySpark**: Distributed computing capabilities

### Zero-Copy Integration
DuckDB can work directly with dataframes from other libraries without copying data, providing significant performance benefits.

## Performance Benefits

- **Fast SQL Engine**: DuckDB's vectorized execution engine
- **Efficient Storage**: Columnar format optimized for analytics
- **Memory Efficient**: Zero-copy operations between libraries
- **Scalable**: Handle datasets larger than memory

## Use Cases

- **Data Analysis**: Interactive exploration with multiple tools
- **ETL Pipelines**: Efficient data transformation workflows
- **Prototyping**: Quick experimentation with different libraries
- **Migration**: Gradual transition between dataframe libraries
- **Benchmarking**: Compare performance across different tools

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Resources

- [DuckDB Documentation](https://duckdb.org/docs/)
- [DuckDB Python API](https://duckdb.org/docs/api/python/overview)
- [Polars Documentation](https://pola-rs.github.io/polars-book/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed in your virtual environment
2. **Database Lock**: Close any existing connections before running the script
3. **Memory Issues**: For large datasets, consider using Polars lazy evaluation or PySpark

### Getting Help

- Check the [DuckDB GitHub Issues](https://github.com/duckdb/duckdb/issues)
- Review the documentation links above
- Open an issue in this repository for project-specific problems
