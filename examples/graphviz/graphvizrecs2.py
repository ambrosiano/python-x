from pygraphviz import *


g = AGraph(directed=True)

g.node_attr['shape']="record"
g.add_node('module1',label="Module 1|{<module1.p0>p0|<module1.p1>p1|<module1.p2>p2}")
g.add_node('module2',label="Module 2|{<module2.p0>p0|<module2.p1>p1|<module2.p2>p2}")
g.add_node('module3',label="Module 3|{<module3.p0>p0|<module3.p1>p1}")

g.add_edge('module1','module2',tailport='module1.p0:e',headport='module2.p1:e')
g.add_edge('module2','module3',tailport='module2.p2:e',headport='module3.p1:e')
g.add_edge('module1','module3',tailport='module1.p0:e',headport='module3.p0:e')


g.layout(prog="dot")
g.draw("test3.png")

