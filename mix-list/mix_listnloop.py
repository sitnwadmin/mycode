#!/usr/bin/env python3

def main():
    # below is a list of  lists containing the drivers needed to switch
    # IP addresses
    networklists = [['ios', '10.0.2.1'], ['ios', '10.0.55.1'], ['junos', '10.0.10.1'],  ['eos', '10.0.14.1']]
    
    for driveandip in networklists:
        print(f"SSH to {driveandip[1]} using driver {driveandip[0]}")

main()
