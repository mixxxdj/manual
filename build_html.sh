#!/bin/sh
# Parse languages and ensure that "en" is built last
# This is necessary because we generate the redirect rules in the same loop
# and want to use "en" as a fallback.
cd source || exit 1
LANGUAGES="$(python -c 'import conf; print(" ".join(sorted((lang for lang in conf.supported_languages.keys() if lang != "en"), reverse=True)))')"
cd .. || exit 1
LANGUAGES="$LANGUAGES en"
NUM_LANGUAGES="$(printf '%s' "$LANGUAGES" | wc -w)"

# Write _redirects file
mkdir -p build/html
printf '/           /latest/               302\n' > build/html/_redirects
printf '/latest/*   /2.3/:splat            301\n' >> build/html/_redirects

i=1
for lang in $LANGUAGES
do
    printf -- '----- Building language "%s"... [%d/%d] -----\n' "$lang" "$i" "$NUM_LANGUAGES"

    if [ "$lang" = "en" ]
    then
        printf '/:version/en/* /:version/en/404.html  404\n' >> build/html/_redirects
        printf '/:version/*    /:version/en/:splat    301\n' >> build/html/_redirects
    else
        printf '/:version/%s/* /:version/%s/404.html  404\n' "$lang" "$lang" >> build/html/_redirects
        printf '/:version/*    /:version/%s/:splat    301 Language=%s\n' "$lang" "$(printf "%s" "$lang"  | sed 's/_/-/g')" >> build/html/_redirects
    fi
    make versionedhtml SPHINXOPTS="-j $(nproc) -Dlanguage=$lang"
    i=$((i + 1))
done
