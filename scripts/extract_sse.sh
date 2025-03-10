#!/bin/bash

# Function to extract SSE for a specific K and distance measure
extract_sse() {
    local distance_measure=$1
    local k_value=$2

    mahout seqdumper -i /user/miovi001/Q2/kmeans-${distance_measure}-k${k_value}/clusteredPoints/part-m-00000 > k${k_value}_points_readable.txt
    grep -o "distance: [0-9.]*" k${k_value}_points_readable.txt > k${k_value}_distances.txt
    cat k${k_value}_distances.txt | cut -d" " -f2 | awk '{sum+=$1*$1} END {print sum}' > results/${distance_measure}_k${k_value}_sse.txt
}

# Extract SSE for Cosine Distance
for k in 5 10 15 20; do
    extract_sse "cos" $k
done

# View results
cat results/cos_k*_sse.txt
