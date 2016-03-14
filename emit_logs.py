#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('protoapp', 'ppaotorp')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] Sent %r" % message)
connection.close()
