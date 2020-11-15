#!/usr/bin/bash

echo "Test start ...."

input_sires_1=("2" "12" "32" "12." "12.2" "13.6" "13.222233" "13.0")
input_sires_2=("2" "10" "33" "12.0" "12.22" "13.8" "13.232233" "13.001")

outputs=("A_EQ_B" "A_GT_B" "A_LT_B" "A_EQ_B" "A_LT_B" "A_LT_B" "A_LT_B" "A_LT_B")

total_len=8

for (( n=0; n<$total_len; n++ ))
do
  res=$( python3 basic.py ${input_sires_1[$n]} ${input_sires_2[$n]} )
  if ! [[ $res = ${outputs[$n]} ]]; then
    percent=$((  ($n+1) * 100 / $total_len  ))
    echo "Program faild at $percent % ::"
    echo $n
    echo GOT = $res
    echo  EXPECTED = ${outputs[$n]}
  fi
done

echo "100% complete testing."
