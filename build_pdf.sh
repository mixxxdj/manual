#!/bin/sh
# Parse languages and ensure that "en" is built last
cd source || exit 1
LANGUAGES="$(python -c 'import conf; print(" ".join(sorted((lang for lang in conf.supported_languages.keys() if lang != "en"), reverse=True)))')"
cd .. || exit 1
LANGUAGES="$LANGUAGES en"
NUM_LANGUAGES="$(printf '%s' "$LANGUAGES" | wc -w)"

i=1
for lang in $LANGUAGES
do
    printf -- '----- Building language "%s"... [%d/%d] -----\n' "$lang" "$i" "$NUM_LANGUAGES"
    make versionedlatexpdf SPHINXOPTS="-Q -j $(nproc) -Dlanguage=$lang" >/dev/null
    i=$((i + 1))
done

cd build/latex || exit 1
mkdir ../pdf
for file in */*/Mixxx-Manual.pdf
do
    newfilename="mixxx-manual-$(dirname "$file" | tr "/" "-")"
    cp "$file" "../pdf/${newfilename}.pdf"
done
find ../pdf -type f
