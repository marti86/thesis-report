#!/usr/bin/python

#Allow to pass arguments
import sys

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

from mininet.link import Link, TCLink

def emptyNet():

    "Create an empty network and add nodes to it."
    net = Mininet( controller=RemoteController, link=TCLink, autoSetMacs = True )
    info( '*** Adding controller\n' )
    net.addController( 'c0' , controller=RemoteController,ip=sys.argv[1],port=6633 )
    print 'connecting to:', sys.argv[1]

    info( '*** Adding hosts\n' )
    srcHost1 = net.addHost( 'h1' )
    srcHost2 = net.addHost( 'h2' )
    srcHost3 = net.addHost( 'h3' )
    dstHost1 = net.addHost( 'h4' )
    dstHost2 = net.addHost( 'h5' )
    dstHost3 = net.addHost( 'h6' )

    info( '*** Adding switch\n' )
    switch3 = net.addSwitch( 's3' )
    switch4 = net.addSwitch( 's4' )
    switch5 = net.addSwitch( 's5' )
    switch6 = net.addSwitch( 's6' )
    switch7 = net.addSwitch( 's7' )
    switch8 = net.addSwitch( 's8' )
    switch9 = net.addSwitch( 's9' )
    switch10 = net.addSwitch( 's10' )
    switch11 = net.addSwitch( 's11' )
    switch12 = net.addSwitch( 's12' )
    switch13 = net.addSwitch( 's13' )
    switch14 = net.addSwitch( 's14' )

    info( '*** Creating links\n' )
    srcHost1.linkTo( switch3 )
    srcHost2.linkTo( switch4 )
    srcHost3.linkTo( switch5 )  
    switch3.linkTo( switch6 )
    switch4.linkTo( switch6 )
    switch5.linkTo( switch6 )
    net.addLink( switch6, switch7, bw=3 )
    net.addLink( switch7, switch11, bw=3 )
    net.addLink( switch6, switch11, bw=4  )
    switch6.linkTo( switch8 )
    net.addLink( switch8, switch9, bw=2 )
    net.addLink( switch9, switch10, bw=2 )
    switch10.linkTo( switch11 )
    switch11.linkTo( switch12 )
    switch11.linkTo( switch13 )
    switch11.linkTo( switch14 )
    switch12.linkTo( dstHost1 )
    switch13.linkTo( dstHost2 )
    switch14.linkTo( dstHost3 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()

