__author__ = 'Jason'

from docutils import nodes
from docutils.parsers.rst import Directive

def setup(app):
    app.add_node(paragraph, html=(visit_paragraph_node, depart_paragraph_node))
    app.add_directive('paragraph', ParagraphDirective)

    app.connect('doctree-resolved', process_paragraph)
    app.connect('env-purge-doc', purge_paragraph)


class paragraph(nodes.General, nodes.Element):
    pass

def visit_paragraph_node(self, node):
    self.visit_admonition(node)

def depart_paragraph_node(self, node):
    self.depart_admonition(node)

def purge_paragraph(app, env, docname):
    return

def process_paragraph(app, doctree, fromdocname):
    return

class ParagraphDirective(Directive):
    required_arguments = 1
    optional_arguments = 1

    def run(self):
        return [paragraph('')]
