

import sys
import os
import shutil
import re
import glob


sftp_in = 'C:\Projects\Projects\PowerApps Project\Python\PPTMerge\In'
sftp_working = 'C:\Projects\Projects\PowerApps Project\Python\PPTMerge\working'
sftp_out = 'C:\Projects\Projects\PowerApps Project\Python\PPTMerge\out'
sftp_dataFile = 'mergeData.json'


from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
  return "Welcome!"

if __name__ == "__main__":
  app.run()