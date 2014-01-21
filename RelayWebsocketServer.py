from __future__ import print_function
from twisted.internet import protocol, reactor
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

# Requires:
#  Twisted: http://twistedmatrix.com
#  Autobahn: http://autobahn.ws/python/

clients = set()

class RelayProtocol(WebSocketServerProtocol):
   def onConnect(self, request):
      print("Client connected")

   def onOpen(self):
      clients.add(self)

   def onMessage(self, payload, isBinary):
      print("Client sent: " + payload)


   def onClose(self, wasClean, code, reason):
      clients.remove(self)
      print("Client disconnected")

class MessageReceiver(protocol.DatagramProtocol):
    def datagramReceived(self, datagram, address):
        print("Broadcasting: " + datagram)
        for c in clients:
            c.sendMessage(datagram, False)

if __name__ == '__main__':
   factory = WebSocketServerFactory("ws://localhost:9000")
   factory.protocol = RelayProtocol

   reactor.listenTCP(9000, factory)
   reactor.listenUDP(43000, MessageReceiver())
   
   reactor.run()
