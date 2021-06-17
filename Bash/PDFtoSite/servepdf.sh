#!/bin/bash

checkHostFolder() {
    if [[ -d "$hostFolder" ]]; then
        rm -r "$hostFolder"
    fi
}

argumentValidator() {
    local numArgs="$#"
    local file="$(head -c 4 "$1")"
    local portnm="$2"

    if [[ $numArgs -lt 1 || $numArgs -gt 2 ]]; then
        echo 'Choose a PDF-File! Follow syntax -> "servepdf <PDF> [port]"' 1>&2
        exit 1
    elif [[ $file != "%PDF" ]]; then
        echo "$file is not a PDF-file!" 1>&2
        exit 1
    elif [[ -z $portnm ]]; then
        port=8000
    elif [[ $portnm -le 1024 || $portnm -gt 65535 ]]; then
        echo "$portnm is not a valid port! Try again"
        exit 1
    else
        return 0
    fi
}

main() {
    port="$2"
    hostFolder="$HOME/.servepdf"

    # Validating conditions
    argumentValidator "$@"
    checkHostFolder

    # Generating PDF-structure in ~/.servepdf
    echo "Converting PDF..."
    ./pdftosite "$1" "$HOME/.servepdf"

    # Hosting
    echo "Starting server on port $port!"
    cd "$hostFolder" && python3 -m http.server "$port" >server.log 2>&1 
}

main "$@"
