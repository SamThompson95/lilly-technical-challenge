# Lilly Technical Challenge - Software Engineer Placement Students
A repository containing the Eli Lilly student developer technical challenge.

## Getting Started
This challenge consists of a backend written in [Python](https://www.python.org/) and a frontend written using HTML, CSS and JavaScript.

1. You will need to install Python in order to run the backend server. See the link above or go [here](https://www.python.org/downloads/).
2. You will need to install Git to handle committs and source code management. You can download Git [here](https://git-scm.com/downloads). When prompted, ensure you add the Git executable to your system's `PATH`. If you get errors like `not found: Git`, follow [this guide](https://stackoverflow.com/questions/26620312/git-installing-git-in-path-with-github-client-for-windows) to add it to `PATH` manually.
3. You will likely want to use an Integrated Development Environment (IDE) or Code Editor. We recommend [Visual Studio Code](https://code.visualstudio.com/Download).
4. You will need a GitHub account in order to [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository and [commit](https://github.com/git-guides/git-commit) your changes.

### Verifying Installation
Run the following commands to confirm that your installations succeeded:
```bash
python --version
git -v
```
You should see version numbers in the terminal (or whatever command-executing environment you ran the above commands in) if they were installed correctly. If you get errors, ensure the installation was successful and that the Python and Git executables were added to your [system `PATH`](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho).

### Git Beginner Guide

If you are struggling to get started with the GitHub side of things, you can follow the below basic instructions:

1. Make a new folder on your local machine that you would like to store this challenge's source code in.
2. Open a terminal (Linux, MacOS) or PowerShell (Windows), or alternatively use the built-in terminal of your IDE (i.e. VSCode terminal), and traverse to the folder you created in step one.
3. Clone the challenge repository into the folder:

```bash
git clone https://github.com/SamThompson95/lilly-technical-challenge
cd lilly-technical-challenge
```

4. When you make changes you would like to commit (save), you can follow the below steps:
```bash
git add <file-name-that-has-changes>
git commit -m "<meaningful-commit-message>"
git push
```
*Ensure you have a remote repository set up on GitHub. You will be committing and pushing changes from your local Git repository to the remote GitHub repository. You can go [here](https://github.com/new) to create a new repository, and [here](https://docs.github.com/en/get-started/using-git/about-git) to understand the basics of Git. You may need to specify the upstream (i.e. remote GitHub repository) repo that you want to push to. See [this guide](https://devopscube.com/set-git-upstream-respository-branch/) on how to do that.*


## Objectives
- Fetch data from the backend server from the frontend, and display it in a user-friendly way.
- A data engineer had some issues migrating data, leaving some gaps in our database. How can you ensure that the frontend handles missing/invalid data returned from the APIs without crashing?
- You can send data to the backend via API(s), however it is not particularly user-friendly. How will you create a user-friendly solution that allows users to input data on the site and send it to the backend?
- The frontend site's design leaves a lot to be desired. Can you make any improvement to the overall design and user experience? (this one is open-ended; feel free to be creative here!)
- You are provided a documentation template and are encouraged to fill this out as you work through this challenge. This will help when it comes time to present your work.

## Optional Objectives
*These objectives can be completed if you have time or would like to be challenged.*
  
- The raw data returned from the backend is a little hard to digest. Can you create a backend function for averaging prices for a particular medicine?

## Scope

### In Scope

### Out of Scope
