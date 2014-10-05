# Copyright (C) 2011  Bradley N. Miller
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'acbart'

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
import json
import os

def setup(app):
    app.add_directive('blockly',Blockly)

    app.add_node(BlocklyNode, html=(visit_block_node, depart_block_node))

    app.connect('doctree-resolved',process_activcode_nodes)
    app.connect('env-purge-doc', purge_activecodes)



class BlocklyNode(nodes.General, nodes.Element):
    def __init__(self,content):
        """

        Arguments:
        - `self`:
        - `content`:
        """
        super(BlocklyNode,self).__init__()
        self.ac_components = content


EXTERNAL = '''
<div id='{0}' class='alert alert-warning' style='max-width:{2}px'>
<div class='directive-status-icon'><img src='../../images/spinner10.gif'/></div>
    <fieldset>
        <legend>Blockly</legend>
    </fieldset>
    <p id='{0}_completed' style='font-size:20px'></p>
    <p>
        <button id='{0}_run' class="btn btn-success">Run</button>
        <button id='{0}_python' class="btn btn-default">Show Python</button>
        <button id='{0}_layout' class="btn btn-default">Layout Blocks</button>
        <button id='{0}_reset' class="btn btn-danger">Reset Code</button>
        <button id='{0}_xml' class="btn btn-success">XML</button>
    </p>
    <iframe id='{0}_iframe' class="blk-iframe" seamless src="/Books/CompThink/html/_static/{1}" width="100%" height="{3}"></iframe>
    <pre class="active_out" id="{0}_pre"></pre>
    <pre class="active_out" id="{0}_xml"></pre>
</div>'''
#
# style="height: 480px; width: 600px;"

START = '''
<html>
<head>
    <script src='blockly_compressed.js' type="text/javascript"> </script>
    <script src='blocks_compressed.js' type="text/javascript"> </script>
    <script src='javascript_compressed.js' type="text/javascript"> </script>
    <script src='python_compressed.js' type="text/javascript"> </script>
    <script src='msg/js/en.js' type="text/javascript"> </script>
    <link rel="stylesheet" href="bootstrap-3.0.0/css/bootstrap.min.css" type="text/css" />
    <link rel="stylesheet" href="video.css" type="text/css" />
    <script type="text/javascript">
    // Get the objects we need to do logging from the parent frame.
    // This seems better than reloading all of jQuery and bookfuncs into the frame. But
    // Makes this a bit more dependent on the Runestone Environment.
    BlocklyDirective = parent.BlocklyDirective
    directiveRemoteCommand = parent.directiveRemoteCommand
    </script>
    <style>
      html, body {
        background-color: #fff;
        margin: 0;
        padding: 0;
      }
      .blocklySvg {
        height: 100%%;
        width: 100%%;
      }
      .active_out {
        margin-top: 5px;
        margin-left: 10px;
        margin-right: 5px;
      }
    </style>
</head>
<body>
<div id="%(divid)s"></div>
'''

CTRL_START = '''<xml id="toolbox" style="display: none">'''
CTRL_END = '''</xml>'''


'''
 <script>console.log("Logging The Init for Blockly Directive \\n"); </script>
  <script>console.log(BlocklyDirective.init); </script>
  <script>console.log("Logging Blockly \\n"); </script>
  <script>console.log(Blockly); </script>
  <script>console.log("Logging Directive \\n"); </script>
  <script>console.log(BlocklyDirective); </script>

  <script>console.log(Blockly); console.log("OKKK \\n"); console.log(BlocklyDirective); console.log("OK \\n"); BlocklyDirective.init(Blockly, '#%(divid)s', '%(preload)s', -1, -1, -1, -1) </script>

'''


END = '''


  <div id='%(divid)s'> </div>
  <script>(new BlocklyDirective()).init(Blockly, '#%(divid)s', document.getElementById('%(divid)s'), '%(preload)s', -1, -1, -1, -1) </script>

  </body>
  </html>
'''

TOOLBOX = '''
* Controls
controls_if
controls_forEach
====
* Logic
logic_compare
logic_operation
logic_negate
logic_boolean
logic_null
====
* Math
math_number
math_arithmetic
math_single
math_trig
math_constant
math_number_property
math_change
math_round
math_modulo
math_random_int
math_random_float
====
* Text
text
text_print
text_length
text_prompt
====
variables
====
* Big Data
weather_get_temperature
weather_get_forecasts
stocks_get_current
stocks_get_past
====
'''.split("\n")

# self for these functions is an instance of the writer class.  For example
# in html, self is sphinx.writers.html.SmartyPantsHTMLTranslator
# The node that is passed as a parameter is an instance of our node class.
def visit_block_node(self, node):

    res = START % (node.ac_components)
    res += CTRL_START
    #
    for ctrl in TOOLBOX+ list(node.ac_components['controls']):
        if ctrl == 'variables':
            res += '<category name="Variables" custom="VARIABLE"></category>'
        elif ctrl == 'functions':
            res += '<category name="Functions" custom="PROCEDURE"></category>'
        elif ctrl == '':
            pass
        elif ctrl[0] == '*':
            res += '<category name="%s">' % (ctrl[2:])
        elif ctrl == '====':
            res += '</category>'
        else:
            res += '<block type="%s"></block>\n' % (ctrl)
    res += CTRL_END
    res += END % (node.ac_components)
    # path = os.path.join(node.ac_components['blocklyHomePrefix'],
    #                     '_static',
    #                     node.ac_components['divid']+'.html')
    path = os.path.join('/Users/Jason/Dropbox/Projects/PyCharmProjects/OpenDSA/Books/CompThink/source/_static',
                        node.ac_components['divid']+'.html')

    with open(path, 'w') as f:
        f.write(res)

    # blockly_directive_init = """<script> BlocklyDirective.init(#%(divid)s, %(preload)s, -1, -1) </script>""".format(node.directive_id, node.preload)

    self.body.append(EXTERNAL.format(node.ac_components['divid'],
                                     node.ac_components['divid']+'.html',
                                     node.ac_components['width'],
                                     node.ac_components['height']))



def depart_block_node(self,node):
    ''' This is called at the start of processing an activecode node.  If activecode had recursive nodes
        etc and did not want to do all of the processing in visit_ac_node any finishing touches could be
        added here.
    '''
    pass


def process_activcode_nodes(app,env,docname):
    pass


def purge_activecodes(app,env,docname):
    pass


class Blockly(Directive):
    required_arguments = 1
    optional_arguments = 1
    has_content = True
    option_spec = {
        'submission': directives.unchanged,
        'comment': directives.unchanged,
        'bigger': directives.flag
        }

    def run(self):
        document = self.state.document
        rel_filename, filename = document.settings.env.relfn2path(self.arguments[0])
        self.options['divid'] = self.arguments[0]
        # We assume that nothing is at the top level... Yeah it's a hack.
        pathDepth = rel_filename.count("/") - 1
        self.options['blocklyHomePrefix'] = "../"*pathDepth

        if 'bigger' in self.options:
            self.options['width'] = 900
            self.options['height'] = 550
        else:
            self.options['width'] = 800
            self.options['height'] = 450

        current_tag = "controls"
        results = {current_tag: ""}
        for line in self.content:
            for tag in ["preload", "output", "function","test"]:
                if line.lstrip().startswith(tag+"::"):
                    current_tag = tag
                    ignore, results[current_tag] = line.split(tag+"::",1)
                    break
            else:
                results[current_tag] += "\n"+line

        self.options['controls'] = results.get('controls', '').split("\n")
        self.options['preload'] = results.get("preload", "").replace("\n", "")
        self.options['test_check'] = "true" if "test" in results else "false"
        self.options['test_code'] = results.get("test", "false").replace('"', '\\"').replace("\n", "\\\n")
        self.options['output'] = results.get("output", "undefined")
        if "function" in results:
            self.options['function_name'], self.options['function_count'], self.options['function_eval'] = results['function'].split(',', 2)
            self.options['function_name'] = self.options['function_name'].strip()
            self.options['function'] = "true"
            self.options['function_eval'] = self.options['function_eval'].replace('"', '\\"').replace("\n", "\\\n")
        else:
            self.options['function_name'], self.options['function_count'], self.options['function_eval'] = "eleonor", 0, ""
            self.options['function'] = "false"

        return [BlocklyNode(self.options)]


# to preload blockly with a finished or partial program, do the following
#
# https://blockly-demo.appspot.com/static/apps/code/index.html?lang=en
#
# Now save the xml string.  And append something like the following to the script after blockly
# is created:
#
#       var xmlText = '<xml>  <block type="variables_set" id="1" inline="true" x="25" y="9">    <field name="VAR">X</field>    <value name="VALUE">      <block type="math_number" id="2">        <field name="NUM">10</field>      </block>    </value>  </block></xml>'
#       xmlDom = Blockly.Xml.textToDom(xmlText);
#       Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, xmlDom);




