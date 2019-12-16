## About this Repository

This repo my python scripts on the following:
![logo](<https://img.icons8.com/color/16/000000/python.png)

|Directory               |Component|
|------------------------|-----------------------------------------------|
|[../CropImages]         |*A python based Image Cropper. Run the cropper.py file to sit back and let the images be cropped.*|
|[../Script-1]           |*Just place the files in the folder where there are mp3 files. The file auto.bat is the windows batch file, which automatically runs the python script Script-1.py after the startup of the computer. While doing any kinda work, one can press 0, 1, 2, ..., 9 to play the song.*|
|[../Script-2]           |*A python script using winsound, to produce beeps on press of keys. This is for ensuring that a key has been pressed. The file autobeep.bat is the windows batch file, which automatically runs the python script Script-2.py after the startup of the computer.*|


## Contributing

First, read the [contribution guidelines](CONTRIBUTING.md). Ensure you understand the code.
### Setup

The following instructions describe how to fork this repository in order 
to contribute to this:

1. Fork this repository, see <https://help.github.com/articles/fork-a-repo/>.

2. Clone your fork:
    
    `git clone https://github.com/<username>/Python_Script.git`
    
    Where `<username>` is your github username.

3. Add the base repository as a remote:
    
    `git remote add upstream https://github.com/digitalPlayer1125/Python_Script.git`

4. Follow the instructions in the README files of each of the directories listed under [About this Repository](#about-this-repository) section of this readme to set up your development environment.

### Development Workflow

After you have forked and cloned the repository, use the following steps to
make and manage changes. After you have finished making changes, you can 
submit them to the base repository using a pull request. 

1. Pull changes from the base repository's master branch:
    
    `git pull upstream master`

1. Create a new branch to track your changes:
    
    `git checkout -b <branch>`
    
    Where `<branch>` is a meaningful name for the branch you'll use to track
    changes.

1. Make and test changes locally.

1. Add your changes to the staging area:
    
    `git add <files>`
    
    Where `<files>` are the files you changed.
    
    > **Note:** Run `git add .` to add all currently modified files to the staging area.

1. Commit your changes:
    
    `git commit -m <message>`
    
    Where `<message>` is a meaningful, short message describing the purpose of
    your changes.

1. Pull changes from the base repository's master branch, resolve conflicts if
   necessary:
      
    `git pull upstream master`

1. Push your changes to your github account:
    
    `git push -u origin <branch>`
    
    Where `<branch>` is the branch name you used in step 2.

1. Create a [pull request](https://help.github.com/articles/about-pull-requests/) to have your changes reviewed and merged into the base 
repository.

    For more information on creating pull requests, see <https://help.github.com/articles/creating-a-pull-request/>. 
    
    To learn more about referencing issues in your pull request or commit messages, see <https://help.github.com/articles/closing-issues-using-keywords/>.

1. Celebrate!
