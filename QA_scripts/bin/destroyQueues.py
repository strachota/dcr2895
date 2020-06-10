#!/usr/bin/python
"""
==============================================================================

 NAME
        destroyQueues - Script to remove artifacts from
                            RabbitMQ message broker

 FILE
        destoryQueues.py

 SYNOPSIS

        This file contains Python statements to remove Exchanges and
        Queues (and Bindings) from a RabbitMQ broker, as specified in
        the server configuration .py file.

 DESCRIPTION

        destroyQueues.py
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
from configurationInit.configLoader import ConfigLoader


if __name__ == "__main__":
    # Loading RabbitMQ configuration variables
    
    cl = ConfigLoader()
    cl.loadParameters()
    
    connectionPars = cl.getConnectionPars()
    exchanges      = cl.getExchanges()
    queues         = cl.getQueues()
    
    # Destroying artifacts
    
    credentials = pika.PlainCredentials(connectionPars["user"], connectionPars["password"])
    parameters = pika.ConnectionParameters(connectionPars["host"],
                                           connectionPars["port"],
                                           connectionPars["vhost"],
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    
    channel = connection.channel(1)
    print("Deleting exchanges:")
    try:
        channelRes = channel.exchange_declare(exchange = exchanges["dacs4Exchange"]["name"],
                                 passive=True)
        print("- %s exists on vhost"%(exchanges["dacs4Exchange"]["name"]))
        channelRes = channel.exchange_delete(exchange = exchanges["dacs4Exchange"]["name"])
        print ("%s deleted, %s"%(exchanges["dacs4Exchange"]["name"], channelRes))
    except:
        print("- %s does not exists on vhost"%(exchanges["dacs4Exchange"]["name"]))
        connection.close()
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel(1)     
    
    
    
    print("Deleting queues:")
    for queueDict in queues.itervalues():
        try:
            queueResult = channel.queue_declare(queue=queueDict["name"],
                                                passive=True)
            print("- %s exists on vhost"%(queueDict["name"]))
            queueResult = channel.queue_delete(queue=queueDict["name"])
            print("%s deleted, %s "%(queueDict["name"], queueResult)) 
        except:
            connection.close()
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel(1)            
            print "- %s does not exist on vhost"%(queueDict["name"]) 
            
    
    connection.close()


