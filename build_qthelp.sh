#!/bin/sh
cd "source"
export VERSION="$(python -c 'import conf; print(conf.version)')"
export LANGUAGES="$(python -c 'import conf; print(" ".join(sorted((lang for lang in conf.supported_languages.keys()), reverse=True)))')"
cd ..
for language in ${LANGUAGES};
do
  mkdir -p "build/qthelp/lang/${language}"
  sphinx-build -b qthelp -d "build/qthelp/.doctrees" -a -j auto "-Dqthelp_basename=manual-${language}" "-Dlanguage=${language}" "-Dqthelp_language_suffix=True" source "build/qthelp/lang/${language}"
done
mkdir -p "build/qthelp/multilang"
tools/qthelp.py "build/qthelp/lang" "build/qthelp/multilang"
mkdir -p "deploy/manual/${VERSION}"
cp "build/qthelp/multilang/mixxx-manual.qch" "build/qthelp/multilang/mixxx-manual.qhc" "deploy/manual/${VERSION}/"
