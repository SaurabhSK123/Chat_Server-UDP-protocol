# Chat_Server-UDP-protocol

Let,s Know about UDP Protocol

The User Datagram Protocol (UDP) is simplest Transport Layer communication protocol available of the TCP/IP protocol suite. It involves minimum amount of communication mechanism. UDP is said to be an unreliable transport protocol but it uses IP services which provides best effort delivery mechanism.

In UDP, the receiver does not generate an acknowledgement of packet received and in turn, the sender does not wait for any acknowledgement of packet sent. This shortcoming makes this protocol unreliable as well as easier on processing.

UDP divides messages into packets, called datagrams, which can then be forwarded by the devices in the network – switches, routers, security gateways – to the destination application/server. While UDP does not number or reassemble the datagrams, it does include port numbers in the datagram header that help distinguish different user requests and an optional checksum capability that can help verify the integrity of the data transferred.

Requirement of UDP :
A question may arise, why do we need an unreliable protocol to transport the data? We deploy UDP where the acknowledgement packets share significant amount of bandwidth along with the actual data. For example, in case of video streaming, thousands of packets are forwarded towards its users. Acknowledging all the packets is troublesome and may contain huge amount of bandwidth wastage. The best delivery mechanism of underlying IP protocol ensures best efforts to deliver its packets, but even if some packets in video streaming get lost, the impact is not calamitous and can be ignored easily. Loss of few packets in video and voice traffic sometimes goes unnoticed.

Features
UDP is used when acknowledgement of data does not hold any significance.

UDP is good protocol for data flowing in one direction.

UDP is simple and suitable for query based communications.

UDP is not connection oriented.

UDP does not provide congestion control mechanism.

UDP does not guarantee ordered delivery of data.

UDP is stateless.

UDP is suitable protocol for streaming applications such as VoIP, multimedia streaming.

<h1>Socket Programming</h1>
What is socket programming?
Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.

