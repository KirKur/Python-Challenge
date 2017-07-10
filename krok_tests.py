# This is just the sample code to print A+B

import sys
total_sum = 0
num_of_terms = int(sys.stdin.readline())
terms = map(int, sys.stdin.readline().split())
for term_num in range(num_of_terms):
    total_sum += terms[term_num]
print total_sum
