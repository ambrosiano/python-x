from pygraphviz import *


g = AGraph()

g.node_attr['shape']="record"
g.add_node('struct1',label="<f0> left|<f1> middle|<f2> right")
g.add_node('struct2',label="<f0> one|<f1> two")
g.add_node('struct3',label="hello\\nworld |{ b |{c|<here> d|e}| f}| g | h")
g.add_edge('struct1','struct2',tailport='f1',headport='f0')
g.add_edge('struct1','struct3',tailport='f2',headport='here')


g.layout(prog="dot")
g.draw("test2.png")

