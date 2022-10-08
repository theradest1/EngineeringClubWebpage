#!/usr/bin/python3

import discord
from discord.ext import commands
from subprocess import Popen
import os
import git
import time
import signal
import threading

hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

start_file = "/home/landonbakken/Desktop/MinecraftModThings/Paper-1.18/start.sh"

git_dir = "/home/landonbakken/Desktop/MinecraftModThings/Paper-1.18/plugins/Skript/scripts"
g = git.cmd.Git(git_dir)

bot = commands.Bot(command_prefix="@")

#max_on_time = 30

""" def countForServer(server):
	global mcserver, max_on_time
	on_time = 0
	time.sleep(30) #wait untill the server is actually on
	while on_time < max_on_time:
		try:
			if mcserver.status.players.online == 0:
				on_time += 1
				time.sleep(1)
			else:
				on_time = 0
		except:
			return
	os.killpg(os.getpgid(server.pid), signal.SIGTERM) """


def start_server():
	server = Popen(start_file, shell=True, preexec_fn=os.setsid)
	#countThread = threading.Thread(target=countForServer, name="count")
	#countThread.start(server)
	return server
	

@bot.command()
async def server(ctx, arg):
	arg = arg.lower()	
	if arg == "start":

		""" try:"""
		await ctx.send("Starting")
		"""except:
			await ctx.send("Starting server...")
			start_server()
			await ctx.send("The server is up")
	elif arg == "stop":
		try:
			os.killpg(os.getpgid(server.pid), signal.SIGTERM)
			await ctx.send("Server stopped")
		except:
			await ctx.send("The server was not running") """
	#else:
		""" try:
			if arg == "ping":
				await ctx.send(mcserver.ping())
			elif arg == "status":
				status = mcserver.status()
				if status.players.online != 1:
					await ctx.send(f"{status.players.online} players with {status.latency} milliseconds of latency")
				else:
					await ctx.send(f"{status.players.online} player with {status.latency} milliseconds of latency")
		except ConnectionRefusedError:
			await ctx.send("The server is not up at the moment, if you want to start the server, run the command '@server start'") """
		

@bot.command()
async def git(ctx, arg):
	arg = arg.lower()
	if arg == "pull":
		try:
			g.pull()
			await ctx.send(f"Git pull successful")
		except:
			await ctx.send("Git was not able to do a pull request (not sure why)")

@bot.command()
async def die(ctx):
	await ctx.send("Bye (:")
	exit()

bot.run(hiddenInfo[0])