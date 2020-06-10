#!/usr/bin/python
"""
==============================================================================

 NAME
        createQueues - Script to populate RabbitMQ message broker

 FILE
        createQueues.py

 SYNOPSIS

        This file contains Python statements to create Exchanges,
        Queues and Bindings on a RabbitMQ broker, as specified in the
        server configuration .py file.

 DESCRIPTION

        createQueues.py
                          This file.

        ${DISTRIBUTED-DIR}/rabbitmq/serverConfiguration.py
                          Python file defining the RabbitMQ server
                          configuration variables: Exchanges, Queues
                          and Bindings

        ConfigLoader      Python class used to load the RabbitMQ
                          configuration variables.

 DIAGNOSTICS

        Script will exit in case of error.

 AUTHORS

        Martin Ertl, Jan Kianicka (2014-04-15) Initial version.

==============================================================================
"""
import pika
import time
import sys
from configurationInit.configLoader import ConfigLoader

if __name__ == "__main__":
        
    # Loading RabbitMQ configuration variables
    
    cl = ConfigLoader()
    cl.loadParameters()
    
    connectionPars = cl.getConnectionPars()
    exchanges      = cl.getExchanges()
    queues         = cl.getQueues()
    bindings       = cl.getBindings()
    
    # Creating artifacts
    
    credentials = pika.PlainCredentials(connectionPars["user"], connectionPars["password"])
    parameters = pika.ConnectionParameters(connectionPars["host"],
                                           connectionPars["port"],
                                           connectionPars["vhost"],
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    # artificial delay to verify correctness of credentials
    print ("go to sleep")
    time.sleep (10)
    #sys.exit(0)
    #
    channel = connection.channel(1)
    print("Creating exchanges:")
    try:
        channelRes = channel.exchange_declare(exchange = exchanges["dacs4Exchange"]["name"],
                             type = exchanges["dacs4Exchange"]["type"], passive=True,
                             durable = bool(exchanges["dacs4Exchange"]["durable"]))
        print("- %s exists in vhost."%(exchanges["dacs4Exchange"]["name"]))
    except:
        print("%s does not exists, will be created."%(exchanges["dacs4Exchange"]["name"]) )
        connection.close()
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel(1)       
    
        channelRes = channel.exchange_declare(exchange = exchanges["dacs4Exchange"]["name"],
                             type = exchanges["dacs4Exchange"]["type"],
                             durable = bool(exchanges["dacs4Exchange"]["durable"]))
        print("Created exchange: %s, %s, %s, %s"%(exchanges["dacs4Exchange"]["name"], exchanges["dacs4Exchange"]["type"],
                                              exchanges["dacs4Exchange"]["durable"], channelRes))
        
    print("Creating queues:")
    for queueDict in queues.itervalues():
        
        if(queueDict.has_key("arguments")):
            try:
                queueResult = channel.queue_declare(queue=queueDict["name"], 
                                            durable=bool(queueDict["durable"]),
                                            passive=True,
                                            arguments=queueDict["arguments"])
                print("- %s exists on vhost."%(queueDict["name"]))
            except:
                print("%s does not exists, will be created."%(queueDict["name"]) )
                connection.close()
                connection = pika.BlockingConnection(parameters)
                channel = connection.channel(1) 
                queueResult = channel.queue_declare(queue=queueDict["name"], 
                                            durable=bool(queueDict["durable"]),
                                            arguments=queueDict["arguments"])
                print "Created queue: %s, %s"%( queueDict["name"],queueResult)
        else:
            try:
                queueResult = channel.queue_declare(queue=queueDict["name"], passive=True, 
                                                    durable=bool(queueDict["durable"]))
                print("- %s exists on vhost."%(queueDict["name"]))
            except:
                print("%s does not exists, will be created."%(queueDict["name"]) )
                connection.close()
                connection = pika.BlockingConnection(parameters)
                channel = connection.channel(1) 
                queueResult = channel.queue_declare(queue=queueDict["name"], 
                                            durable=bool(queueDict["durable"]))
                print "Created queue: %s, %s"%( queueDict["name"],queueResult)
        
        
    print("Creating bindings:")
    for bingingDict in bindings.itervalues():
        
        bingingRes  =  channel.queue_bind(exchange  = bingingDict["exchange"],
                                          queue     = bingingDict["queue"],
                                          routing_key = bingingDict["routing_key"])
        print("Binding %s created/confirmed, %s"%( bingingDict["routing_key"],bingingRes))
    connection.close()
