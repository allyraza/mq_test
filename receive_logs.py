#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('protoapp', 'ppaotorp')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')
queue = channel.queue_declare(exclusive=True)
queue_name = queue.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue=queue_name)

channel.start_consuming()
