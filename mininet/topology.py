from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        print('hello! initializing custom topology!')
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(s1, s2)

class MultipathTopo(Topo):
    def __init__(self):
        print('-----')
        print('setting up multipath topology')
        print('-----')
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(h1, s1, bw=1)
        self.addLink(h1, s2, bw=1)
        self.addLink(s1, h2)
        self.addLink(s2, h2)

class TripathTopo(Topo):
    def __init__(self):
        print('-----')
        print('setting up tripath topology')
        print('-----')
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
 
        self.addLink(h1, s1, bw=10)
        self.addLink(h1, s2, bw=10)
        self.addLink(h1, s3, bw=10)
        self.addLink(s1, h2)
        self.addLink(s2, h2)
        self.addLink(s3, h2)

class NonDisjointMultipathTopo(Topo):
    def __init__(self):
        print('-----')
        print('setting up non-disjoint multipath topology')
        print('-----')

        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        self.addLink(h2, s1, bw=1)
        self.addLink(h2, s2, bw=1)
        self.addLink(s1, s3, bw=1)
        self.addLink(s2, s3, bw=1)
        self.addLink(s3, h1, bw=1)

class NonDisjointMultipathTopo2(Topo):
    def __init__(self):
        print('-----')
        print('setting up non-disjoint multipath topology')
        print('-----')
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        self.addLink(h2, s1, bw=1)
        self.addLink(h2, s2, bw=1)
        self.addLink(s1, s3, bw=1)
        self.addLink(s2, s3, bw=1)
        self.addLink(s3, s4, bw=1)
        self.addLink(s3, s5, bw=1)
        self.addLink(s4, s6, bw=1)
        self.addLink(s5, s6, bw=1)
        self.addLink(s6, h1)

class SFOTopology(Topo):
    def __init__(self, bw=10, delay=0, loss=0, bg=0):
        print('-----')
        print('setting up SFO\'s topology with 2 clients')
        print('-----')
        Topo.__init__(self)
        
        server = self.addHost('server', mac='00:00:00:00:01:03')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        self.addLink(h1, s1, bw=bw, delay=delay, loss=loss)
        self.addLink(h2, s1, bw=bw, delay=delay, loss=loss)

        self.addLink(s1, s2, bw=bw, delay=delay, loss=loss)
        self.addLink(s1, s3, bw=bw, delay=delay, loss=loss)
        self.addLink(s2, s4, bw=bw, delay=delay, loss=loss)
        self.addLink(s3, s5, bw=bw, delay=delay, loss=loss)
        self.addLink(s4, s6, bw=bw, delay=delay, loss=loss)
        self.addLink(s5, s6, bw=bw, delay=delay, loss=loss)

        self.addLink(s6, server)

        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')

        self.addLink(h1, s7, bw=bw, delay=delay, loss=loss)
        self.addLink(h2, s7, bw=bw, delay=delay, loss=loss)

        self.addLink(s7, s8, bw=bw, delay=delay, loss=loss)
        self.addLink(s7, s9, bw=bw, delay=delay, loss=loss)
        self.addLink(s8, s10, bw=bw, delay=delay, loss=loss)
        self.addLink(s9, s11, bw=bw, delay=delay, loss=loss)
        self.addLink(s10, s12, bw=bw, delay=delay, loss=loss)
        self.addLink(s11, s12, bw=bw, delay=delay, loss=loss)

        self.addLink(s12, server)

	if bg > 0:
		print("bg is more than 0, adding hosts for generating background traffic")
		bg1a = self.addHost('bg1a', ip='10.13.91.1')
		bg1b = self.addHost('bg1b', ip='10.13.91.2')
		self.addLink(bg1a, s2, bw=bg)
		self.addLink(bg1b, s4, bw=bg)

		bg2a = self.addHost('bg2a', ip='10.13.92.1')
		bg2b = self.addHost('bg2b', ip='10.13.92.2')
		self.addLink(bg2a, s3, bw=bg)
		self.addLink(bg2b, s5, bw=bg)

		bg3a = self.addHost('bg3a', ip='10.13.93.1')
		bg3b = self.addHost('bg3b', ip='10.13.93.2')
		self.addLink(bg3a, s8, bw=bg)
		self.addLink(bg3b, s10, bw=bg)

		bg4a = self.addHost('bg4a', ip='10.13.94.1')
		bg4b = self.addHost('bg4b', ip='10.13.94.2')
		self.addLink(bg4a, s9, bw=bg)
		self.addLink(bg4b, s11, bw=bg)

topos = {
    'mytopo': (
        lambda: MyTopo()
    ),
    'multipath': (
        lambda: MultipathTopo()
    ),
    'tripath': (
        lambda: TripathTopo()
    ),
    'ndmp': (
        lambda: NonDisjointMultipathTopo()
    ),
    'ndmp2': (
        lambda: NonDisjointMultipathTopo2()
    ),
    'sfo': (
        lambda: SFOTopology()
    )
}
