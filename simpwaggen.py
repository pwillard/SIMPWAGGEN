#!/usr/bin/python
# -*- coding: utf-8 -*-
#===============================================================================
#  SSSS  III  M   M PPPP  W   W  AAA   GGGG  GGGG EEEEE N   N       PPPP  Y   Y 
# S       I   MM MM P   P W   W A   A G     G     E     NN  N       P   P  Y Y  
#  SSS    I   M M M PPPP  W W W AAAAA G GGG G GGG EEEE  N N N       PPPP    Y   
#     S   I   M M M P     W W W A   A G   G G   G E     N  NN  ..   P       Y   
# SSSS   III  M   M P      W W  A   A  GGG   GGG  EEEEE N   N  ..   P       Y   
#===============================================================================
 
#===============================================================================
# Program:      SimpWagGen.py
# Author:       Pete Willard
# Email:        petewillard@gmail.com
# Version:      1.0
# Target:       ORTS WAG FILE
# Date:         2021/05/23
# Time:         10:27:00
# Notes:        uses PYTHON 3
# Reference:    
#===============================================================================
# Pete Willard  Contact: petewillard@gmail.com
#
# USAGE
#   -h, --help      GET HELP
#   --config_path   USe an alternate INI file
#   --loaded        Create a LOADED WAG file from the INI file instead of the 
#                   default empty car.
#
#=====[ MODULE IMPORTS ]========================================================
import configparser
import argparse
from decimal import Decimal

#===============================================================================
#=====[ VARIABLES ]=============================================================
# Command Line Arguments 
ar = argparse.ArgumentParser()
ar.add_argument("--config_path",
    help="Path to configuration file",
    default='./'
)

ar.add_argument('--loaded',
    action='store_true',
    help="Configure the device as a loaded freight car [Default is Empty]",
)

args = ar.parse_args()

config_file = args.config_path + '/config.ini'

cfg = configparser.ConfigParser() 
cfg.read(config_file)

##############################################################################  
# Pre-loaded variables
CarMassMT = cfg.get("DEFAULT","mtWeight")
CarMassLD = cfg.get("DEFAULT","ldWeight")

if args.loaded:
    CarMass = CarMassLD
    CarStatus = "_LD"
    CarStatusText = " Loaded "
else:
    CarMass = CarMassMT
    CarStatus = "_MT" 
    CarStatusText =  " Unloaded "

CarName = cfg.get("DEFAULT","reportingMark") + '_' + cfg.get("DEFAULT","carNumber") + '_' + cfg.get("DEFAULT","carType") 

length = cfg.get("DEFAULT","length") 
width = cfg.get("DEFAULT","width") 
height =  cfg.get("DEFAULT","height")
frontal = str(Decimal(width) * Decimal(height)) 

 
#===============================================================================
#=====[ FUNCTIONS ]=============================================================
def main():
    out = []
    # HEADER
    out.append([
        'SIMISA@@@@@@@@@@JINX0D0t______',
        '\n\n',
    ])
    # START OF CAR DEFINITION
    out.append("Comment (##############################################################################)\n")
    out.append("Comment (# ORTS WAGON FILE: "+ CarStatusText  + cfg.get("DEFAULT","reportingMark") + ' ' + cfg.get("DEFAULT","carNumber") + ' ' +cfg.get("DEFAULT","desc") + ' ' + cfg.get("DEFAULT","carType") + '\n')
    out.append("Comment (##############################################################################)\n\n")
    out.append("Wagon (" + CarName + CarStatus + "\n") 
    out.append(" Type ( FREIGHT ) \n")
    out.append(" WagonShape ( " + CarName + ".s ) \n")
    out.append(" Size ( " + width + "m " + height + "m "  + length + "m )\n" )
    out.append(" Mass( " + CarMass + " ) \n")
    out.append(" WheelRadius ( " +cfg.get("DEFAULT","wheelRadius") + " ) \n" )
    out.append(" NumWheels (4) \n")
    out.append(" AntiSlip (0) \n\n")

    # COUPLING
    out.append("Comment (##############################################################################)\n")
    out.append("Comment (# COUPLER\n")
    out.append("Comment (##############################################################################)\n\n")
    out.append([
    '	Comment ( AAR Standard Coupler )	\n',
    '	        Coupling (	\n',
    '	                Type ( Automatic )	\n',
    '	                Spring (	\n',
    '	                        Stiffness ( 1.1e6N/m 4.8e6N/m )	\n',
    '	                        Damping ( 1.1e6N/m/s 1.1e6N/m/s )	\n',
    '	                        Break ( 1.6e6N 1.6e6N )	\n',
    '	                        r0 ( 20cm 30cm )	\n',
    '	                )	\n',
    '	                Velocity ( 0.1m/s )	\n',
    '	        )	\n',
    '	        Coupling (	\n',
    '	                Type ( Automatic )	\n',
    '	                Spring (	\n',
    '	                        Stiffness ( 1.1e6N/m 4.8e6N/m )	\n',
    '	                        Damping ( 1.1e6N/m/s 1.1e6N/m/s )	\n',
    '	                        Break ( 1.6e6N 1.6e6N )	\n',
    '	                        r0 ( 20cm 30cm )	\n',
    '	                )	\n',
    '	                Velocity ( 0.1m/s )	\n',
    '	        )	\n',
    '	        Buffers (	\n',
    '	                Spring (	\n',
    '	                        Stiffness ( 1e6N/m 5e6N/m )	\n',
    '	                        Damping ( 1.1e6N/m/s 1.1e6N/m/s )	\n',
    '	                        r0 ( 0m 1e9 )	\n',
    '	                )	\n',
    '	                Centre ( 0.5 )	\n',
    '	                Radius ( 1 )	\n',
    '	                Angle ( 0.5deg )	\n',
    '	        )	\n'
        ])

    out.append("Comment (##############################################################################)\n")
    out.append("Comment (# FRICTION\n")
    out.append("Comment (##############################################################################)\n\n")
    # PHYSICS SECTION
    out.append([
    '   Comment (/!\ Friction Settings - GENERIC - FIX AS NEEDED )\n',
    '   Comment ( ==== Level Resistance ==== )\n',    
    '	 ORTSBearingType ( Roller )	\n',
    '	 ORTSDavis_A ( 184.784lb )	\n',
    '	 ORTSDavis_B ( 2.3800lbf/mph )	\n',
    '	 ORTSDavis_C ( 0.06458lbf/mph^2 )	\n',
    '    \n\n'  
    '   Comment ( ==== Wind Resistance ==== )\n',
    '    ORTSWagonFrontalArea ( ' + frontal + 'ft^2 )\n',
    '    ORTSDavisDragConstant ( 0.0012 )\n',
        '    \n\n'  
   ])


    out.append("Comment (##############################################################################)\n")
    out.append("Comment (# BRAKING\n")
    out.append("Comment (##############################################################################)\n\n")
    # Brake Section
    out.append([    
    '	BrakeEquipmentType( "Handbrake, Triple_valve, Auxilary_reservoir, Emergency_brake_reservoir" )	\n',
    '	BrakeSystemType( "Air_single_pipe" )	\n',
    '	MaxBrakeForce( 50kN )	\n',
    '	\n',
    '	MaxHandbrakeForce( 35kN )	\n',
    '	NumberOfHandbrakeLeverSteps( 100 )	\n',
    '	\n',
    '	TripleValveRatio( 2.5 )	\n',
    '	MaxReleaseRate( 50 )	\n',
    '	MaxApplicationRate( 50 )	\n',
    '	MaxAuxilaryChargingRate( 20 )	\n',
    '	EmergencyResCapacity( 7 )	\n',
    '	EmergencyResChargingRate( 20 )	\n',
    '	EmergencyBrakeResMaxPressure( 90 )	\n',
    '	BrakeCylinderPressureForMaxBrakeBrakeForce( 50 ) \n',
    '\n\n'
    ])
    out.append("Comment (##############################################################################)\n")
    out.append("Comment (# SOUNDS\n")
    out.append("Comment (##############################################################################)\n\n")
    # Sound Section
    out.append(' Comment ( Sound Settings )\n')  
    out.append('  Sound (    "GenFreightWag2.sms" )\n')
    # END of File
    out.append(") \n")

    # CREATE OUTPUT FILE
    out_name = CarName + CarStatus + '.wag'
    with open (out_name, 'w', encoding='utf-16-le') as output:
        for i in out: output.write("".join(i))

#===============================================================================
#=====[ MAIN CODE ]=============================================================

main()

#===============================================================================
