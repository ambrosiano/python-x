from pygraphviz import *


class Module:
    def __init__(self,name,ports):
        self.name = name
        self.ports = ports


class Connect:
    def __init__(self,source,target):
        self.source = source
        self.target = target


class Network:
    def __init__(self,modules,connects):
        self.modules = modules
        self.connects = connects

def makegraph(net):
    g = AGraph(directed=True,strict=False)
    g.node_attr['shape'] = "record"
    modules = net.modules
    for m in modules:
        mname = m.name
        nlabel = mname
        mports = m.ports
        if len(mports)>0:
            nlabel += '|{'
            for i in range(0,len(mports)):
                p = mports[i]
                portlabel = '<'+mname+'.'+p+'>'+p
                nlabel += portlabel
                if i<(len(mports)-1):
                    nlabel += '|'
                else:
                    nlabel += "}"
        print(mname+':'+nlabel)
        g.add_node(mname, label=nlabel)
        connects = net.connects
    for c in connects:
        tail = c[0]
        head = c[1]
        mtail = c[0][0]
        ptail = c[0][1]
        mhead = c[1][0]
        phead = c[1][1]
        tport = mtail+'.'+ptail
        hport = mhead+'.'+phead
        print(mtail+':'+tport+'->'+mhead+':'+hport)
        g.add_edge(mtail, mhead, tailport=tport+':e', headport=hport+':e')
    return g


def main():
    m1 = Module('A',['p1','p2'])
    m2 = Module('B',['p1','p2'])
    c1 = [('A','p1'),('B','p2')]
    c2 = [('B','p1'),('A','p2')]
    net = Network([m1,m2],[c1,c2])
    # connects = net.connects
    # for c in connects:
    #     print(c[0][0]+'.'+c[0][1]+'->'+c[1][0]+'.'+c[1][1])
    g = makegraph(net)
    print(g.to_string())
    g.layout(prog="dot")
    g.draw("modulegraph.png")


if __name__=='__main__':
    main()

