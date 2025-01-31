# src/extract_logs.py
import sys
import os
from datetime import datetime
import mmap

def binary_search_date(mm, target_date):
    left, right = 0, mm.size() - 1
    
    while left <= right:
        mid = (left + right) // 2
        mm.seek(mid)
        
        # Find start of line
        while mid > 0 and mm.read(1) != b'\n':
            mid -= 1
            mm.seek(mid)
            
        # Read line
        line = mm.readline().decode('utf-8')
        try:
            current_date = line[:10]  # Extract YYYY-MM-DD
            
            if current_date < target_date:
                left = mm.tell()
            elif current_date > target_date:
                right = mid - 1
            else:
                # Found matching date, backtrack to first occurrence
                while mid > 0:
                    mm.seek(mid - 1)
                    if mm.read(10).decode('utf-8') != target_date:
                        return mid
                    mid -= 1
                return 0
        except:
            right = mid - 1
            
    return -1

def extract_logs(date):
    if not os.path.exists('output'):
        os.makedirs('output')
        
    output_file = f'output/output_{date}.txt'
    
    try:
        with open('test_logs.log', 'rb') as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            
            # Find start position for date
            start_pos = binary_search_date(mm, date)
            if start_pos == -1:
                print(f"No logs found for date {date}")
                return
                
            mm.seek(start_pos)
            
            with open(output_file, 'w') as out:
                while True:
                    line = mm.readline().decode('utf-8')
                    if not line or not line.startswith(date):
                        break
                    out.write(line)
                    
            print(f"Logs extracted to {output_file}")
            
    except FileNotFoundError:
        print("Log file not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
        
    date = sys.argv[1]
    try:
        datetime.strptime(date, '%Y-%m-%d')
        extract_logs(date)
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")