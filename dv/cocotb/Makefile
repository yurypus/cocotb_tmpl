# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

# defaults
#SIM ?= verilator
SIM ?= icarus

SIM_BUILD = ./build
COCOTB_RESULTS_FILE = $(SIM_BUILD)/results.xml
#export PYTHONPYCACHEPREFIX=./build/tmp

ifeq ($(SIM), verilator)
COVERAGE=1
EXTRA_ARGS += -Wno-fatal --coverage
EXTRA_ARGS += --trace --trace-fst --trace-structs
SIM_ARGS +=  +verilator+coverage+file+$(SIM_BUILD)/coverage.dat --trace-file $(SIM_BUILD)/dump.fst
endif

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += ../../hw/rtl/dut.sv 

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = dut

# MODULE is the basename of the Python test file
MODULE = test_dut

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

coverage: 
	verilator_coverage --annotate logs $(SIM_BUILD)/coverage.dat
	
rm: 
	rm -Rf ./build
	rm -Rf ./__pycache__
