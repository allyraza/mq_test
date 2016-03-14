#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('protoapp', 'ppaotorp')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'gauges.update'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
