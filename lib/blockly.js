
function BlocklyDirective() {
    this.Blockly = -1;
    this.directive_id = -1;
    this.preload = -1;
    this.width = -1;
    this.height = -1;
}

BlocklyDirective.prototype.init = function(Blockly, id, iframe_id, preload, width, height, outputCheck, testCheck) {
    this.Blockly = Blockly;
    this.directive_id = id;
    this.preload = preload;
    this.width = width;
    this.height = height;

    this.Blockly.inject(iframe_id, {
        path: './',
        scrollbars: false,
        toolbox: document.getElementById('toolbox')
    });

    this.load_from_server(id);

    $(this).append("<button> ALign Blocks </button>")

};

BlocklyDirective.prototype.load_from_server = function(id) {
//    ajax.post('load/blockly/persitence', {'id': id}, function(data) {
//        // handle load
//    });
};

BlocklyDirective.prototype.align = function() {

    var blocks = this.Blockly.getMainWorkspace().getTopBlocks();
    var y = 20;
    for (var i = 0; i < blocks.length; i++){
        blocks[i].moveTo(this.Blockly.Toolbox.width+20, y);
        y += blocks[i].getHeightWidth().height;
        y += 20; // buffer
    }

};

BlocklyServer= {};

var FIRST_LOAD_FLAG = true;

//BlocklyServer.load = function(directive_id) {
//    directiveRemoteCommand('get_blockly_success', BlocklyDirective.directive_id,
//        {}, function(data) {
//            if (data.finished) {markSuccess(false);}
//        },
//        function(data) {console.log(data.message);});
//    directiveRemoteCommand('activecode/load_program', directive_id,
//        {'div_id': directive_id},
//        function(data) {
//            if (data.code) {
//                setXml(data.code);
//            }
//            if (storage.has(directive_id)) {
//                if (storage.is_new(directive_id, data.timestamp)) {
//                    storage.remove(directive_id);
//                } else {
//                    setXml(storage.get(directive_id));
//                    BlocklyServer.submit(directive_id);
//                }
//            }
//            if (FIRST_LOAD_FLAG) {
//                BlocklyDirective.Blockly.addChangeListener(function () {
//                    addDelay(BlocklyDirective.directive_id, function() {
//                        BlocklyServer.submit(BlocklyDirective.directive_id);
//                        FIRST_LOAD_FLAG = false;
//                    });
//                });
//            }
//        },
//        function(data) {
//            console.log(data.message);
//        });
//};
//BlocklyServer.submit = function(directive_id) {
//    var value = getXml();
//    storage.set(directive_id, value);
//    directiveRemoteCommand('activecode/save_program',  directive_id,
//        {'code': value, 'div_id': directive_id},
//        function(data) {
//            directiveRemoteCommand('set_assess_response',  directive_id,
//                {'text': getPython(), 'type': 'blockly'},
//                function(data) {
//                    storage.remove(directive_id);
//                },
//                function(data) {
//                    console.log(data.message);
//                });
//        },
//        function(data) {
//            console.log(data.message);
//        }
//    );
//};

function resetCode() {
    var xmlText = BlocklyDirective.preload;
    setXml(xmlText);
}

window.onload = function() {
    resetCode();
//    BlocklyServer.load("%(divid)s");
    jQuery(BlocklyDirective.directive_id + "_run").click(runCode);
    jQuery(BlocklyDirective.directive_id + "_xml").click(showXml);
    jQuery(BlocklyDirective.directive_id + "_python").click(showCode);
    jQuery(BlocklyDirective.directive_id + "_reset").click(resetCode);
//    jQuery(BlocklyDirective.directive_id + "_layout").click(align);
};

if (!String.prototype.encodeHTML) {
    String.prototype.encodeHTML = function () {
        return this.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&apos;');
    };
}

function showCode() {
    // Generate JavaScript code and display it.
    parent.createModal("Python Code", "<pre>"+getPython()+"</pre>", "500px");
}
function getPython() {
//    BlocklyDirective.Blockly.Python.INFINITE_LOOP_TRAP = null;
//    return BlocklyDirective.Blockly.Python.workspaceToCode();
}
function getXml() {
//    var dom = BlocklyDirective.Blockly.Xml.workspaceToDom(BlocklyDirective.Blockly.mainWorkspace);
//    return BlocklyDirective.Blockly.Xml.domToPrettyText(dom);
}
function setXml(code) {
//    BlocklyDirective.Blockly.mainWorkspace.clear();
//    if (code != "") {
//        var xml = BlocklyDirective.Blockly.Xml.textToDom(code);
//        BlocklyDirective.Blockly.Xml.domToWorkspace(BlocklyDirective.Blockly.mainWorkspace, xml);
//        align();
//    }
}
function showXml() {
    jQuery(Blockly.directive_id + "_pre").html(getXml().encodeHTML());
}

function runCode() {
    // Generate JavaScript code and run it.
    window.LoopTrap = 1000;
    jQuery(Blockly.directive_id + "_pre").html("");
    BlocklyDirective.Blockly.JavaScript.INFINITE_LOOP_TRAP = 'if (--window.LoopTrap == 0) markFailure("When Blockly tried to run your code, it found an infinite loop. A common reason is that you are calling your function INSIDE of the definition of your function.");\\n';
    var code = BlocklyDirective.Blockly.JavaScript.workspaceToCode();
    BlocklyDirective.Blockly.JavaScript.INFINITE_LOOP_TRAP = null;

    if(logBookEvent) {
        logBookEvent({'event': 'blockly', 'act': 'run', 'div_id': Blockly.directive_id});
    } else {
        console.log('logBookEvent is not defined.  This should be defined in the parent frame')
    }

    try {
        eval(code);
    } catch (e) {
        markFailure("Something is critically wrong with your code. Double check it. The error was: "+e);
    }
//
//    if ("%(output)s" !== "undefined") {
//        if (testCodeOutput("%(output)s")) {
//            markSuccess(true);
//        } else {
//            markFailure("That is not the expected output!");
//        }
//    } else if (%(test_check)s) {
//        success = eval("%(test_code)s")
//        if (success === true) {
//            markSuccess(true);
//        } else {
//            markFailure(success);
//        }
//    } else if (%(function)s) {
//        if (typeof %(function_name)s == 'function') {
//            if (%(function_name)s.length == %(function_count)s) {
//                success = eval("%(function_eval)s")
//                if (success === true) {
//                    markSuccess(true);
//                } else {
//                    markFailure(success);
//                }
//            } else {
//                markFailure("Incorrect number of arguments!");
//            }
//        } else {
//            markFailure("Please make sure your function is named exactly '%(function_name)s'!");
//        }
//    }

}

function markFailure(error) {
    logRunError(Blockly.directive_id, getPython(), error);
    jQuery("#" + Blockly.directive_id + "_completed").html(error);
}
function markSuccess(notify_server) {
    jQuery("#" + Blockly.directive_id + "_completed").html("<span class='label label-success'><span class='glyphicon glyphicon-ok'></span>&emsp;Completed!</span>");
    if (notify_server) {
        directiveRemoteCommand('set_blockly_success', Blockly.directive_id, {}, function(data) {},
            function(data) { console.log(data.message);});
    }
}

function testCodeOutput(expected) {
    return jQuery.trim(expected) === jQuery.trim(current_printed_result);
}

//Blockly.JavaScript['text_print'] = function(block) {
//    // Print statement override.
//    var argument0 = Blockly.JavaScript.valueToCode(block, 'TEXT',
//        Blockly.JavaScript.ORDER_NONE) || '\\'\\'';
//    return 'my_custom_print(' + argument0 + ', "%(divid)s" );\\n';
//};

var current_printed_result = "";
function my_custom_print(text,divid) {
    current = jQuery(Blockly.directive_id + "_pre").html();
    current_printed_result = current+text+"\\n";
    jQuery(Blockly.directive_id + "_pre").html(current+text+"\\n");
}

//align();
