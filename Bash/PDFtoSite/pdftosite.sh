#!/bin/bash 

generatePageHTML() {
    local title="$1"
    local text="$2"
    local dest="$3"

    cat <<HTML > "$dest"
<!DOCTYPE html>
<html>
 <head>
  <meta charset="UTF-8">
  <title>$title</title>
  <style>
   img {
    border: 1px solid black;
   }
  </style>
 </head>
 <body>
  <pre>
$text
  </pre>
  $imageHTML
 </body>
</html>
HTML
}

checkArguments() {
    local numOfArgs="$#"
    if [[ ! "$numOfArgs" -eq 2 ]]; then
        echo "Bad arguments. Please try again."
        exit 1
    fi
}

checkFile() {
    local file="$(file "$1" | cut -d " " -f 2)"
    if [ "$file" != "PDF" ]; then
        echo "Not a PDF-file. Please try again."
        exit 1
    fi
}

checkDestination() {
    local destination="$1"
    if [ -d "$destination" ]; then
        echo "Destination already exists."
        exit 1
    else    
        mkdir "$destination"
    fi
}

getImagesHTML() {
    local pageNm="$1"
    local destination="$2"
    local imageeees=$(basename -a "$destination"/page*/*.jpg)

    imageHTML=""

    for image in $imageeees; do
        echo "$image"
        echo "$imageHTML"
        imageHTML+="<li><img src=\"$(basename "$image")\"/></li>"
    done
}

getPdfContent() {
    local pdf="$1"
    local destination="$2"
    local title=$(basename "$pdf" | cut -d "." -f 1 )
    for ((page = 1 ; page <= "$numOfPages" ; page++)); do
        mkdir "$destination"/page"$page"
        text=$(pdftotext "$pdf" -f "$page" -l "$page" - )
        pdfimages "$pdf" -f "$page" -l "$page" "$destination"/page"$page"/image
        getImagesHTML "$page" "$destination"
        generatePageHTML "$title" "$text" "$destination"/page"$page"/index.html "$page"
    done

}

convertPdfImages() {
    local counter=1
    local pdf="$1"
    local destination="$2"

    for image in "$destination"/page*/*.ppm; do
        pagePath=$(dirname "$image")
        pnmscale -xsize 600 "$image" | ppmtopgm | ppmtojpeg > "$pagePath"/image"$counter".jpg
        ((counter++))
        rm "$image"
    done
}

main() {
    pdf="$1"
    destination="$2"

    checkArguments "$@"
    checkFile "$pdf"
    checkDestination "$destination"

    numOfPages=$(pdfinfo "$pdf" | grep "Pages: " | tr -s " " | cut -d ":" -f 2)

    getPdfContent "$pdf" "$destination"
    convertPdfImages "$pdf" "$destination"

}

main "$@"

