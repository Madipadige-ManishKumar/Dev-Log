echo "Enter a Number"
read n
t=$n
rev=0

while [ $n -gt 0 ]
do
    rev=$(( (rev * 10) + (n % 10) ))
    n=$((n / 10))
done

echo "$rev"

if [ $rev -eq $t ]
then
    echo "$t is an Palindrome Number"
else
    echo "$t is not an Palindrome Number"
fi
