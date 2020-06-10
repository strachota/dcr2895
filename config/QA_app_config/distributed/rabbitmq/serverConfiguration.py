# rabbitmq/serverConfiguration.py
#

Exchanges = {"dacs4Exchange":{"name": "dacs4Exchange",
                          "type": "direct",
                          "durable": True
                          }
             }

Queues = {"DtkPmccqueue":{"name":     "task.detpro.DtkPmcc",
                    "durable":  True
                    },
	  "DtkPmccLatequeue":{"name":     "task.detpro.DtkPmccLate",
                    "durable":  True
                    },
          "StaProQueue":{"name":     "task.detpro.StaPro",
                    "durable":  True
                    },
          "DoneQueue":{"name":     "ex.interval.done",
                    "durable":  True,
                    "arguments": {"x-message-ttl": 1800000}
                    },
          "FailedQueue":{"name":     "ex.interval.failed",
                    "durable":  True,
                    "arguments": {"x-message-ttl": 1800000}
                    },
          "IntervalQueue":{"name": "db.update.interval",
                    "durable":  True
                    },
          "TisCommandQueue":{"name": "xcmd.detpro.TisDetpro",
                            "durable": True,
                            "arguments":{"x-message-ttl": 5000}},
          "TisDtkPmccCommandQueue":{"name": "xcmd.detpro.TisDtkPmcc",
                            "durable": True,
                            "arguments":{"x-message-ttl": 5000}},
          "TisDtkPmccLateCommandQueue":{"name": "xcmd.detpro.TisDtkPmccLate",
                            "durable": True,
                            "arguments":{"x-message-ttl": 5000}},
          "TisLateCommandQueue":{"name": "xcmd.detpro.TisDetproLate",
                            "durable": True,
                            "arguments":{"x-message-ttl": 5000}}
          }

Bindings = {"DtkPmccBinding":{"exchange":       Exchanges["dacs4Exchange"]["name"],
                          "queue"   :       Queues["DtkPmccqueue"]["name"],
                          "routing_key":    "DtkPmcc"
                          },
            "DtkPmccLateBinding":{"exchange":       Exchanges["dacs4Exchange"]["name"],
                          "queue"   :       Queues["DtkPmccLatequeue"]["name"],
                          "routing_key":    "DtkPmccLate"
                          },
            "StaProBinding":{"exchange":    Exchanges["dacs4Exchange"]["name"],
                           "queue"   :      Queues["StaProQueue"]["name"],
                           "routing_key":    "StaProDetpro"
                           },
            "DoneBinding":{"exchange":      Exchanges["dacs4Exchange"]["name"],
                           "queue"   :      Queues["DoneQueue"]["name"],
                           "routing_key":    "Done"
                           },
            "FailedBinding":{"exchange":    Exchanges["dacs4Exchange"]["name"],
                           "queue"   :      Queues["FailedQueue"]["name"],
                           "routing_key":    "Failed"
                           },
            "IntervalBinding":{"exchange":    Exchanges["dacs4Exchange"]["name"],
                           "queue"   :      Queues["IntervalQueue"]["name"],
                           "routing_key":    "UpdateInterval"
                           },
            "TisCommandBinding":{"exchange": Exchanges["dacs4Exchange"]["name"],
                                 "queue": Queues["TisCommandQueue"]["name"],
                                 "routing_key": "TisDetpro"
                                 },
            "TisDtkPmccCommandBinding":{"exchange": Exchanges["dacs4Exchange"]["name"],
                                 "queue": Queues["TisDtkPmccCommandQueue"]["name"],
                                 "routing_key": "TisDtkPmcc"
                                 },
            "TisDtkPmccLateCommandBinding":{"exchange": Exchanges["dacs4Exchange"]["name"],
                                 "queue": Queues["TisDtkPmccLateCommandQueue"]["name"],
                                 "routing_key": "TisDtkPmccLate"
                                 },
            "TisLateCommandBinding":{"exchange": Exchanges["dacs4Exchange"]["name"],
                                 "queue": Queues["TisLateCommandQueue"]["name"],
                                 "routing_key": "TisDetproLate"
                                 }
            }
