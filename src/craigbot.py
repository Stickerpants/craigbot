#!/usr/bin/env python

import discord
import asyncio

class CraigBot():
    def __init__(self):
        self.client = discord.Client()
        self.client.run("YOUR_TOKEN_HERE")
	#

def main():
    CraigBot()

if __name__ == "__main__":
    main()
