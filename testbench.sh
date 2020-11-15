#!/usr/bin/bash

# This is a test bench for our program that checks all of the
# cases that our program should handle.

echo "Hello $(whoami)"
echo ">>" $(date "+ %Y-%m-%d %H:%M:%S")
echo ">> Test start ...."

# Total inputs to check
input_sires_1=("2" "12" "32" "12." "12.2" "13.6" "13.222233" "13.0")
input_sires_2=("2" "10" "33" "12.0" "12.22" "13.8" "13.232233" "13.001")

# Results based on the inputs
outputs=("A_EQ_B" "A_GT_B" "A_LT_B" "A_EQ_B" "A_LT_B" "A_LT_B" "A_EQ_B" "A_LT_B")

# len of the arrays
total_len=${#outputs[@]}

# Loop of testing
for (( n=0; n<$total_len; n++ ))
do
  # Running the program and keeping the result txt
  res=$( python3 basic.py ${input_sires_1[$n]} ${input_sires_2[$n]} )

  if ! [[ $res = ${outputs[$n]} ]]; then # If a test case goes wrong
    percent=$((  ($n+1) * 100 / $total_len  ))
    # an statistics showing to user
    echo "Program faild at $percent % ::"
    echo $n
    echo GOT = $res
    echo  EXPECTED = ${outputs[$n]}
    # a little waiting
    sleep 3
  fi
done

# Final results
echo ">>" $(date "+ %Y-%m-%d %H:%M:%S")
echo ">> 100% complete testing."
echo ">>" $total_len "cases checked."