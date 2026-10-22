import os
import re

from mkdocs.structure.files import File

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PASTA = "tutoriais"
LINK_ABSOLUTO = re.compile(r"\]\(/(" + PASTA + r"/[^)\s]+)")


def on_files(files, config):
    for base, _, nomes in os.walk(os.path.join(RAIZ, PASTA)):
        for nome in nomes:
            caminho = os.path.relpath(os.path.join(base, nome), RAIZ).replace(os.sep, "/")
            files.append(File(caminho, RAIZ, config["site_dir"], config["use_directory_urls"]))
    return files


def on_page_markdown(markdown, page, config, files):
    origem = os.path.dirname(page.file.src_uri)
    return LINK_ABSOLUTO.sub(lambda m: "](" + os.path.relpath(m.group(1), origem or ".").replace(os.sep, "/"), markdown)
