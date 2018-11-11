
#!/bin/bash
echo "resize image who is bigger than 20k";
for i in `find . -size +20k`;
do
convert $i -resize 50% $i;
echo "resize image $i to 50%";
done