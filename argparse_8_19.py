"""Example from: https://www.idkrtm.com/creating-cli-utilities-with-python/
Uses pythonping to ping
"""

import argparse
from pythonping import ping


# Set description to be printed when using help command
parser = argparse.ArgumentParser(description = "A utility for pinging servers.")

# Add cli arguments and help text
parser.add_argument('-host',
                    help = "What hostname or IP to ping?")
parser.add_argument('-count',
                    help = "How many times to ping host? (Default: 4)",
                    default = 4)

# Parse arguments
args = parser.parse_args()

# Ping host X times
ping = ping(args.host, count = args.count)
print(ping)