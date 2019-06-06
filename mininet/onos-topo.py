from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        print('initializing dumbell topology!')
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
	s4 = self.addSwitch('s4')

        self.addLink(h1, s1)
        self.addLink(h2, s4)

        self.addLink(s1, s2, bw=1)
        self.addLink(s2, s4, bw=1)
	self.addLink(s1, s3, bw=1)
	self.addLink(s3, s4, bw=1)


topos = {
    'mytopo': (
        lambda: MyTopo()
    ),
}
