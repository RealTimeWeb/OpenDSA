__author__ = 'Jason'

# TODO directive_id cannot be the same as div_id since if you decide to remove a problem fromt the RST file
# TODO then a new directive could be tied to an old directive id in the database
TEXT_AREA = '<div id={div_id} directive_id={div_id}> <textarea rows="4" cols="50"> {content} </textarea> </div>'

from docutils import nodes
from docutils.parsers.rst import Directive

def setup(app):
    app.add_node(ParagraphNode, html=(visit_paragraph_node, depart_paragraph_node))
    app.add_directive('paragraph', ParagraphDirective)

    app.connect('doctree-resolved', process_paragraph)
    app.connect('env-purge-doc', purge_paragraph)


class ParagraphNode(nodes.General, nodes.Element):

    def __init__(self, content):
        """
        Arguments:
        - `self`:
        - `content`:
        """
        super(ParagraphNode, self).__init__()
        self.ac_components = content


def visit_paragraph_node(self, node):
    self.visit_admonition(node)
    self.body.append(TEXT_AREA.format(div_id=node.ac_components['div_id'], content=node.ac_components['content']))


def depart_paragraph_node(self, node):
    self.depart_admonition(node)


def purge_paragraph(app, env, docname):
    return


def process_paragraph(app, doctree, fromdocname):
    return


class ParagraphDirective(Directive):

    required_arguments = 1
    has_content = True

    def run(self):
        # document = self.state.document
        self.assert_has_content()
        self.options['div_id'] = self.arguments[0]
        self.options['content'] = self.content[0]
        return [ParagraphNode(self.options)]
