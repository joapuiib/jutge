#!/usr/bin/env python3

import csv
import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( 'csv_filename' )
    parser.add_argument( '-d', '--dirname' )
    args = parser.parse_args()

    filename = args.csv_filename
    dirname = args.dirname

    csvfile = open( filename, 'r' )
    reader = csv.reader( csvfile, delimiter=',' )

    for alumne, repo in reader :
        # alumne = alumne.split()
        # nom = ".".join([alumne[i] for i in [0,2]])
        nom = alumne

        repo = repo.replace("https://gitlab.com/", "git@gitlab.com:")

        print(nom, " => ", repo)
        repo_dir = "/".join([dirname, nom])
        if repo:
            if os.path.isdir(repo_dir):
                subprocess.call(["git", "-C", repo_dir, "pull", "--force", "--tags"])
            else:
                subprocess.call(["git", "clone", repo, repo_dir])

if __name__ == "__main__":
    main()
