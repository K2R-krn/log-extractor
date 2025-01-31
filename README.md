# Log Extractor

A high-performance solution to extract logs from a 1TB log file for a specific date.

## Features
- Memory-mapped file handling
- Binary search implementation
- Efficient memory usage
- Date-based log extraction

## Usage
python
python src/extract_logs.py YYYY-MM-DD

##Output
Creates files in output/output_YYYY-MM-DD.txt
Contains all logs for specified date

##Requirements
Python 3.x
Sufficient disk space for output

##Performance
Optimized for 1TB log files
Memory efficient
Fast retrieval using binary search
