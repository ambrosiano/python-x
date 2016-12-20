from pygraphviz import *

g = AGraph()

g.add_node("A")
g.add_node("B")
g.add_node("C")

g.add_edge("A","B")
g.add_edge("B","C")
g.add_edge("C","A")

g.layout(prog="dot")
g.draw("test.svg")

