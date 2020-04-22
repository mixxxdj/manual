#!/bin/sh

DEFAULT_BASE_URL="https://mixxx.org/manual/latest"

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    printf 'Usage: %s [ ( -h | --help ) | base_url ]\n\nArguments:\n    base_url:     The base URL of the manual to use. If this argument is unset,\n                  it will try use the BASE_URL environment variable. If that is\n                  also unset, it defaults to "%s".\n    -h | --help:  Display this help text\n' "$0" "${DEFAULT_BASE_URL}"
    exit 0
fi

# Read the base URL from the environment or the command line arguments, or fall back to the default mixxx
[ -n "$1" ] && BASE_URL="$1"
[ -z "$BASE_URL" ] && BASE_URL="${DEFAULT_BASE_URL}"
printf 'Running tests using base URL: %s\n' "$BASE_URL"

FAILED=0

test_redirect() {
    ORIGINAL_URL="$1"
    REDIRECT_URL="$2"
    shift 2

    if [ "${ORIGINAL_URL}" = "${REDIRECT_URL}" ]; then
        if [ -z "$#" ]; then
            printf 'Do not redirect from "%s"... ' "${ORIGINAL_URL}"
        else
            printf 'Do not redirect from "%s" with args "%s"... ' "${ORIGINAL_URL}" "$*"
        fi
    else
        if [ -z "$#" ]; then
            printf 'Redirect from "%s" to "%s"... ' "${ORIGINAL_URL}" "${REDIRECT_URL}"
        else
            printf 'Redirect from "%s" to "%s" with args "%s"... ' "${ORIGINAL_URL}" "${REDIRECT_URL}" "$*"
        fi
    fi

    EXPECTED_URL="${BASE_URL}/${REDIRECT_URL}"


    # shellcheck disable=SC2086
    RESPONSE="$(curl -s -D- "$@" "${BASE_URL}/$ORIGINAL_URL")"
    ACTUAL_URL=$(printf "%s" "${RESPONSE}" | grep -Po "Location: \K.*" | tr -d '\r')

    # No redirect found, actual URL is the original URL
    [ -z "${ACTUAL_URL}" ] && ACTUAL_URL="${BASE_URL}/${ORIGINAL_URL}"

    if [ "${EXPECTED_URL}" = "${ACTUAL_URL}" ]; then
        printf 'OK\n'
    else
        printf 'FAILED\n'
        printf 'Expected URL: %s\n' "${EXPECTED_URL}" >&2
        printf 'Actual URL:   %s\n' "${ACTUAL_URL}" >&2
        printf 'Server Response:\n%s\n' "${RESPONSE}" >&2
        FAILED=1
    fi
}

test_redirect "" "en/"
test_redirect "chapters" "en/chapters"
test_redirect "chapters/user_interface.html" "en/chapters/user_interface.html"
test_redirect "Mixxx-Manual.pdf" "en/Mixxx-Manual.pdf"

test_redirect "" "de/" -H 'Accept-Language: de'
test_redirect "chapters" "de/chapters" -H 'Accept-Language: de'
test_redirect "chapters/user_interface.html" "de/chapters/user_interface.html" -H 'Accept-Language: de'
test_redirect "Mixxx-Manual.pdf" "de/Mixxx-Manual.pdf" -H 'Accept-Language: de'

test_redirect "" "de-DE/" -H 'Accept-Language: de-DE, de'
test_redirect "chapters" "de-DE/chapters" -H 'Accept-Language: de-DE, de'
test_redirect "chapters/user_interface.html" "de-DE/chapters/user_interface.html" -H 'Accept-Language: de-DE, de'
test_redirect "Mixxx-Manual.pdf" "de-DE/Mixxx-Manual.pdf" -H 'Accept-Language: de-DE, de'

test_redirect "" "de/" -H 'Accept-Language: xxx, de;q=0.9, en;q=0.8'
test_redirect "chapters" "de/chapters" -H 'Accept-Language: xxx, de;q=0.9, en;q=0.8'
test_redirect "chapters/user_interface.html" "de/chapters/user_interface.html" -H 'Accept-Language: xxx, de;q=0.9, en;q=0.8'
test_redirect "Mixxx-Manual.pdf" "de/Mixxx-Manual.pdf" -H 'Accept-Language: xxx, de;q=0.9, en;q=0.8'

test_redirect "es/" "es/"
test_redirect "es/" "es/" -H 'Accept-Language: de'
test_redirect "es/chapters" "es/chapters"
test_redirect "es/chapters" "es/chapters" -H 'Accept-Language: de'
test_redirect "es/chapters/user_interface.html" "es/chapters/user_interface.html"
test_redirect "es/chapters/user_interface.html" "es/chapters/user_interface.html" -H 'Accept-Language: de'
test_redirect "es/Mixxx-Manual.pdf" "es/Mixxx-Manual.pdf"
test_redirect "es/Mixxx-Manual.pdf" "es/Mixxx-Manual.pdf" -H 'Accept-Language: de'

[ "${FAILED}" -ne "0" ] && exit 1
