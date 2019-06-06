from topology import TripathTopo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import RemoteController

topo = TripathTopo()
controller = RemoteController('onos')
net = Mininet(topo=topo, link=TCLink, controller=controller)
h1, h2 = net.hosts

h1_intfs = h1.intfList()
h2_intfs = h2.intfList()

h1_intfs[0].setIP('10.0.0.1/24')
h1_intfs[0].setMAC('00:01:00:00:00:01')
h1_intfs[1].setIP('10.0.1.1/24')
h1_intfs[1].setMAC('00:01:00:00:00:02')
h1_intfs[2].setIP('10.1.0.1/24')
h1_intfs[2].setMAC('00:01:00:00:00:03')

h2_intfs[0].setIP('10.0.0.2/24')
h2_intfs[0].setMAC('00:02:00:00:00:01')
h2_intfs[1].setIP('10.0.1.2/24')
h2_intfs[1].setMAC('00:02:00:00:00:02')
h2_intfs[2].setIP('10.1.0.2/24')
h2_intfs[2].setMAC('00:02:00:00:00:03')

h2.cmd('ip rule add from 10.0.1.2 table 2')
h2.cmd('ip route add default via 10.0.1.1 table 2')
h2.cmd('ip rule add from 10.1.0.2 table 3')
h2.cmd('ip route add default via 10.1.0.1 table 3')

net.start()
net.interact()
