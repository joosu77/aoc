
if [ ! -f "i$1" ]; then
    wget https://adventofcode.com/2023/day/$1/input --header "Cookie: session=53616c7465645f5fb899465286119d01c0a36a689e2c0160dd107c474d7b867326c9e40cfa0487d622d68ae1370b051a5b3964cbc934096a8de0535c4c07d892"
    mv input i$1
fi
echo Part 1
for f in i$1*; do
	echo $f
	python3 d$1-1.py $f
done

echo part 2
for f in i$1*; do
	echo $f
	python3 d$1-2.py $f
done
