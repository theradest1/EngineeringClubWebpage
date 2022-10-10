##!/usr/bin/python3

import discord
from discord.ext import commands
from subprocess import Popen
import os
import psutil
import git
import time
import signal
import threading
import subprocess

hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

start_file = "/home/server/EngineeringClubWebpage/StartServer.sh"

git_dir = "/home/server/EngineeringClubWebpage"
g = git.cmd.Git(git_dir)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="@", intents = intents)

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
	global server
	server = subprocess.Popen("node app.js", shell = True, stdout=subprocess.PIPE)
	print(server)
	#, shell=True, preexec_fn=os.setsion
	#countThread = threading.Thread(target=countForServer, name="count")
	#countThread.start(server)

def stop_server():
	global server
	print(server)
	#server.kill()
	kill_proc_tree(os.getpid())
	#os.killpg(os.getpgid(server.pid), signal.SIGTERM)
	#subprocess.Popen.kill(server)

def kill_proc_tree(pid):    
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()

@bot.command()
async def server(ctx, arg):
	arg = arg.lower()
	if arg == "start":

		try:
			await ctx.send("Starting")
			start_server()
		except:
			await ctx.send("Server Start Failed (not sure why)")
	if arg == "stop":
		await ctx.send("Stopping")
		stop_server()
		#except:
		#	await ctx.send("Server Stop Failed (not sure why)")
	if arg == "restart":
		try:
			await ctx.send("Stopping")
			stop_server()
		except:
			await ctx.send("Server Stop Failed (not sure why)")
		try:
			await ctx.send("Starting")
			start_server()
		except:
			await ctx.send("Server Start Failed (not sure why)")

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

bot.run(hiddenInfo[1])
