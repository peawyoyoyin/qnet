import argparse

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
from topology import SFOTopology

def readCLIArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--loss', dest='loss', type=float, default=0.0)
    parser.add_argument('--delay', dest='delay', type=float, default=0.0)
    parser.add_argument('--bw', dest='bw', type=float, default=10.0)
    parser.add_argument('--bg', dest='bg', type=float, default=0.0)

    args = parser.parse_args()
    return args

def setUp(config):
    topo = SFOTopology(bw=config.bw, delay=config.delay, loss=config.loss, bg=config.bg)
    net = Mininet(topo=topo, controller=RemoteController('onos'), link=TCLink, autoSetMacs=True)

    server = net.get('server')
    h1 = net.get('h1')
    h2 = net.get('h2')

    server.intfs[1].setIP('10.0.1.3/24')
    server.cmd('ip rule add from 10.0.1.3 table 2')
    server.cmd('ip route add default dev server-eth1 table 2')

    # configure additional interfaces
    h1.intfs[0].setIP('10.0.0.1/24')
    h1.intfs[1].setIP('10.0.1.1/24')
    h1.cmd('ip rule add from 10.0.1.1 table 2')
    h1.cmd('ip route add default dev h1-eth1 table 2')
    h2.intfs[0].setIP('10.0.0.2/24')
    h2.intfs[1].setIP('10.0.1.2/24')
    h2.cmd('ip rule add from 10.0.1.2 table 2')
    h2.cmd('ip route add default dev h2-eth1 table 2')

    net.start()
    net.interact()
    net.stop()

if __name__ == '__main__':
    args = readCLIArgs()
    print(args)
    setUp(args)
