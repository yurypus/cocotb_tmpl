# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

import logging
import random
import math
import itertools
import cocotb
import os


from cocotb.triggers import FallingEdge, RisingEdge, Timer, Event
from cocotb.regression import TestFactory
from cocotb.clock import Clock


async def cycle_reset(dut):
    dut.arstn.setimmediatevalue(0)
    for i in range(10):
        await RisingEdge(dut.aclk)
        
    dut.arstn.setimmediatevalue(1)
    for i in range(10):
        await RisingEdge(dut.aclk)
   
   
async def run_test(dut, delay=0):
    dut.arstn.setimmediatevalue(0)
    cocotb.start_soon(Clock(dut.aclk, 10, units="ns").start())
    
    await cycle_reset(dut)
        
    await Timer(delay, units="ns")


def full_test():
    for test in [run_test]:
        factory = TestFactory(test)
        factory.add_option("delay", [0, 40, 100])
        factory.generate_tests()
    
if cocotb.SIM_NAME:
    full_test()
    

