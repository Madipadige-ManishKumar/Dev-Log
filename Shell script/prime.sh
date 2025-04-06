echo "enter a Number"
read num

for ((i=2;i<=$((num/2));i++))
do
    if [ $((num%i)) -eq 0 ];
    then
        echo "not a prime"
        exit 0
    fi
done
echo "is prime"
