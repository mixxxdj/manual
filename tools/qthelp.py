#!/usr/bin/env python3
import argparse
import os
import pathlib
import shutil
import subprocess
import xml.etree.ElementTree as ET


def get_qthelpproject_info(path):
    tree = ET.parse(path)
    custom_filter = tree.getroot()[2]
    assert custom_filter.tag == "customFilter"
    assert custom_filter.attrib["name"].startswith("Mixxx ")
    version = custom_filter.attrib["name"].partition(" ")[2]
    assert version
    filter_section = tree.getroot()[3]
    assert filter_section.tag == "filterSection"
    toc = None
    keywords = None
    files = set()
    for element in filter_section:
        if element.tag == "toc":
            toc = element
        elif element.tag == "keywords":
            keywords = element
        elif element.tag == "files":
            files = set(filter(None, (x.strip() for x in element.itertext())))
    assert toc is not None
    assert keywords is not None
    return (version, toc, keywords, files)


def generate_qhp(inputpath, outputpath, name, namespace, attributes):
    languages = {}
    languagefiles = {}
    outputfiles = {}
    for proj_file in inputpath.glob("*/*.qhp"):
        language = proj_file.parent.name
        version, toc, keywords, files = get_qthelpproject_info(proj_file)
        languages[language] = version, toc, keywords
        languagefiles[language] = files

    shared_files = None
    for files in languagefiles.values():
        if shared_files is None:
            shared_files = files
        else:
            shared_files.intersection_update(files)

    root = ET.Element("QtHelpProject", attrib={"version": "1.0"})
    ET.SubElement(root, "namespace").text = namespace
    ET.SubElement(root, "virtualFolder").text = "doc"

    for language in languages:
        custom_filter = ET.SubElement(
            root,
            "customFilter",
            attrib={
                "name": language,
            },
        )
        for attribute in (*attributes, language):
            ET.SubElement(custom_filter, "filterAttribute").text = attribute

    if shared_files:
        filter_section = ET.SubElement(root, "filterSection")
        for attribute in attributes:
            ET.SubElement(filter_section, "filterAttribute").text = attribute
        files = ET.SubElement(filter_section, "files")
        for filename in shared_files:
            ET.SubElement(files, "file").text = filename
            outputfiles[filename] = inputpath.joinpath(language, filename)

        for language in languages:
            languagefiles[language].difference_update(shared_files)

    for language, content in languages.items():
        filter_section = ET.SubElement(root, "filterSection")
        for attribute in (*attributes, language):
            ET.SubElement(filter_section, "filterAttribute").text = attribute

        filter_section.append(toc)
        filter_section.append(keywords)
        files = ET.SubElement(filter_section, "files")
        for filename in languagefiles[language]:
            ET.SubElement(files, "file").text = filename
            outputfiles[filename] = inputpath.joinpath(language, filename)

    for dest, source in outputfiles.items():
        destpath = outputpath.joinpath(dest)
        os.makedirs(destpath.parent, exist_ok=True)
        shutil.copyfile(source, destpath)

    tree = ET.ElementTree(root)
    tree.write(outputpath.joinpath(name + ".qhp"))


def generate_qhcp(outputpath, name, namespace, title):
    root = ET.Element("QHelpCollectionProject", attrib={"version": "1.0"})
    assistant = ET.SubElement(root, "assistant")
    url = "qthelp://" + namespace + "/doc/index.en.html"
    ET.SubElement(assistant, "title").text = title
    ET.SubElement(assistant, "homePage").text = url
    ET.SubElement(assistant, "startPage").text = url
    docfiles = ET.SubElement(root, "docFiles")
    generate = ET.SubElement(docfiles, "generate")
    file = ET.SubElement(generate, "file")
    ET.SubElement(file, "input").text = name + ".qhp"
    ET.SubElement(file, "output").text = name + ".qch"
    register = ET.SubElement(docfiles, "register")
    ET.SubElement(register, "file").text = name + ".qch"

    tree = ET.ElementTree(root)
    outputfile = outputpath.joinpath(name + ".qhcp")
    tree.write(outputfile)
    return outputfile


def generate_qhc(qhcpfile):
    executable = os.getenv("QHELPGENERATOR", "qhelpgenerator")
    subprocess.call((executable, qhcpfile))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=pathlib.Path)
    parser.add_argument("output_path", type=pathlib.Path)
    args = parser.parse_args(argv)

    name = "mixxx-manual"
    namespace = "org.mixxx.manual"
    attributes = ("mixxx", "manual")
    title = "Mixxx User Manual"
    generate_qhp(
        args.input_path,
        args.output_path,
        name,
        namespace,
        attributes,
    )
    qhcpfile = generate_qhcp(args.output_path, name, namespace, title)
    generate_qhc(qhcpfile)


if __name__ == "__main__":
    main()
