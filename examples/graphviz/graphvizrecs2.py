from pygraphviz import *


g = AGraph(directed=True)

g.node_attr['shape']="record"
g.add_node('module1',label="Module 1|{<f0>p0|<f1>p1|<f2>p2}")
g.add_node('module2',label="Module 2|{<f3>p3|<f4>p4|<f5>p5}")
g.add_node('module3',label="Module 3|{<f6>p6|<f7>p7|<f8>p8}")

g.add_edge('module1','module2',tailport='f0',headport='f5')
g.add_edge('module2','module3',tailport='f4',headport='f7')


g.layout(prog="dot")
g.draw("test3.png")

