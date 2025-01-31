# Discussion.md
# Log Extractor Solution

## Solutions Considered

1. **Simple Line-by-Line Reading**
   - Pros: Simple implementation
   - Cons: Very inefficient for 1TB file
   
2. **Memory Mapping with Binary Search**
   - Pros: 
     - Efficient memory usage
     - Fast search using binary search
     - Handles large files well
   - Cons:
     - More complex implementation
     
3. **Parallel Processing**
   - Pros: Could be faster
   - Cons: More complex, potential overhead

## Final Solution Summary

Chosen approach: Memory Mapping with Binary Search because:
- Efficient for large files
- Minimizes memory usage
- Reasonable implementation complexity
- Fast search capabilities

## Steps to Run

1. Clone the repository
2. Navigate to src directory
3. Run: `python extract_logs.py YYYY-MM-DD`
4. Output will be in output/output_YYYY-MM-DD.txt