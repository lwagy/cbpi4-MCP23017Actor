# -*- coding: utf-8 -*-
import os
from MCP23017_I2C import *

class MCP23017Actor:
    
    def __init__(self,MCPPin,MCPAddress,MCPInverted):
        self.SetValueOff=0
        self.SetValueOn=1
    
        self.MCPPin = MCPPin #1
        self.MCPAddress = MCPAddress #0x27
        self.MCPInverted = MCPInverted #False
        if self.MCPInverted == "True":
            self.SetValueOn=0
            self.SetValueOff=1
        else:  
            self.SetValueOn=1
            self.SetValueOff=0

    def on(self):
        self.MCP = MCP23017_I2C("MCP23017", self.MCPAddress , "16bit")
        self.MCP.set_mode(int(self.MCPPin)-1, "output")
        self.MCP.output(int(self.MCPPin)-1, self.SetValueOn)
        print("Actor ON")

    def off(self):
        self.MCP = MCP23017_I2C("MCP23017", self.MCPAddress , "16bit")
        self.MCP.set_mode(int(self.MCPPin)-1, "output")
        self.MCP.output(int(self.MCPPin)-1, self.SetValueOff)
        print("Actor OFF")
         
while True:

    Actor = MCP23017Actor(1,0x27,False)
    Actor.on()
    time.sleep(5)
    Actor.off()
    time.sleep(5)




   



