import socket
import os

class Kernel:
  def __init__(self):
      self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server.bind((socket.gethostname(), 8080))
      self.running = False
      self.
      self.commands = {
          "help": self.help,
          "exit": self.exit,
          "conn": self.conn,
          "disconn": self.disconn,
          "open": self.open,
          "move": self.move,
          "dele": self.dele,
          "create": 
      }
  def start(self):
      self.running = True
      print("=========LOGOS V1.0=========")
      print("2024 Copyright Logan Johnson")
      print(" ")
      print("Type 'help' for a list of commands")
      while self.running:
          command = input("> ").strip()
          self.execute_command(command)

  def execute_command(self, command):
      parts = command.split(" ")
      cmd = parts[0]
      args = parts[1:]
      if cmd in self.commands:
          self.commands[cmd](*args)
      else:
          print("Command not found. Type 'help' for available commands.")

  def help(self):
      print("Available commands:")
      for cmd in self.commands:
          print("-", cmd)

  def exit(self):
      print("Exiting kernel.")
      self.running = False
  def conn(self, ip):
      self.client.connect((ip, 8080))
      print(f"Connected to {ip}")
  def disconn(self):
      self.client.close()
      print("Disconnected")
  def open(self, file):
      if ".py" in file:
        exec(file)
      elif ".pypic" in file:
        exec(f"import {file}", locals(), globals())
  def move(self, file, dir):
    try:
      os.rename(file, dir)
    except:
      print("File or directory invalid ")
  def dele(self, file):
    try:
      os.remove(file)
    except:
      print("File or directory invalid")
  def create(self, file, contents):
    if ".py" in file:
      with open(file, "w") as f:
        f.write(contents)
    elif ".pypic" in file:
      with open(file, "w") as f:
        f.write(contents)
    else:
      print("File or directory invalid: invalid file type or name")
if __name__ == "__main__":
  kernel = Kernel()
  kernel.start()