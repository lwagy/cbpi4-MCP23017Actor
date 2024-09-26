
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *
from .MCP23017_I2C import *

logger = logging.getLogger(__name__)

@parameters([Property.Select(label="MCPPin", options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], description="Pin number on MCP chip"),
             Property.Select(label="MCPAddress", options=["0x20", "0x21","0x22","0x23","0x24","0x25","0x26","0x27"], description="MCP address"),
             Property.Select(label="MCPInverted", options=["True", "False"], description="Inverted pin")
             ])
class CustomActor(CBPiActor):

    SetValueOff=0
    SetValueOn=1
    
    @action("action", parameters={})
    async def action(self, **kwargs):
        print("Action Triggered", kwargs)
        pass
    
    
    def on_start(self):
        self.state = False
        pass
    
       
    def __init__(self, cbpi, id, props):
        self.MCPPin = int(self.props.get("MCPPin"))
        self.MCPAddress = int(self.props.get("MCPAddress"),16)
        self.MCPInverted = self.props.get("MCPInverted")
        if self.MCPInverted == "True":
            self.SetValueOn=0
            self.SetValueOff=1
        else:  
            self.SetValueOn=1
            self.SetValueOff=0
            
        self.value = 0
        self.state = False
        pass  
    
    
    async def on(self, power=0):
        self.MCP = MCP23017_I2C("MCP23017", self.MCPAddress , "16bit")
        self.MCP.set_mode(int(self.MCPPin)-1, "output")
        self.MCP.output(int(self.MCPPin)-1, self.SetValueOn)
        print("Actor ON {0}".format(self.id))
        
        logger.info("ACTOR 1111 %s ON" % self.id)
        self.state = True


    async def off(self):
        self.MCP = MCP23017_I2C("MCP23017", self.MCPAddress , "16bit")
        self.MCP.set_mode(int(self.MCPPin)-1, "output")
        self.MCP.output(int(self.MCPPin)-1, self.SetValueOff)
        print("Actor OFF {0}".format(self.id))
        
        logger.info("ACTOR %s OFF " % self.id)
        self.state = False


    def get_state(self):
        return self.state
    
    
    async def run(self):
        pass


def setup(cbpi):
    cbpi.plugin.register("cbpi4-MCP23017Actor", CustomActor)
    pass
