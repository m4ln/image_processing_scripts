mkdir ../jpg

for f in *.tiff
do  
    echo "Converting $f" 
    convert "$f"  "../jpg/$(basename "$f" .tiff).jpg" 
done
