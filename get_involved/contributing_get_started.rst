.. meta::
   :description: Do your first steps with Kdenlive video editor, contributing get started
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, contributing, git, gitlab, started

.. metadata-placeholder

   :authors: - add your name here

   :license: Creative Commons License SA 4.0

..  This is a remark and only show up in the file itself


.. _contributing_get_started:

***********
Get started
***********


Editing the Manual
==================

Contributing to the manual is done by GitLab and git, this to make sure that the contribution is checked before the input is added to the documentation.
The scheme looks as following:

.. figure:: /images/contributing_gitlab_git.png
   :width: 450px 
   :alt: Contributing GitLab Git
      
   Scheme of Gitlab and git

In a nutshell
-------------

The Kdenlive manual lives in a GitLab repository. Because it’s not your own repository you have to fork (copy) the manual to your own GitLab account (Git does not allow you to add code to someone else's repository without access rights. You have read-only access to Kdenlive manual). You have to fork only once.

Git is the control software which tracks: code changes, who made changes.

From your GitLab fork you make a copy of the manual to your local PC.

Make a branch. A branch is a new/separate version of the master branch.

Now you can start making changes. 

Once done you stage (select the files you want to upload) and commit it. The you can push your changes to your GitLab repository. And from there by merge request to the Kdenlive manual. 

Then it gets checked by a “Developer” and if OK it gets merged into the Kdenlive manual.

Before you start making new changes again you have to pull the latest status from the Gitlab Kdenlive manual repository to your GitLab fork and then to your local repository. This is to make sure you work on the latest manual status as other contributors could have merged changes to other parts of the manual in the meantime.

Now the process starts again with making changes.


Prerequisites
============

To edit and preview the manual locally you only need a simple text editor and a terminal. Alternatively an IDE like Visual Studio Code makes things easier for you as it eg. shows you broken or missing links, has automated code completion and highlights typos and shows a preview of the rendered result.

To build the manual you also need to install a few things on you PC:

-	Python (Windows: set PATH to Python and Script)

-	Sphinx: Open a console and type `pip install --upgrade sphinx`

-	The Sphinx "Read the Docs" theme: Open a console and type `pip install --upgrade sphinx_rtd_theme` 

To be able to bring your contribution to the official manual you finally need a KDE GitLab account: https://my.kde.org/login 

If you use an IDE you may want to install some additional tools for example with Visual Studio Code:

-	Open a console and type: pip install esbonio (Language Server for Sphinx projects. To see preview in VSCode)

-	Install on VSCode: https://code.visualstudio.com/

   - Install: Gitlab Workflow (To see the status on GitLab. Not mandatory)

   - Install: Gitlens (Microsoft git software)

   - Install: Python (for editing Python code. Not mandatory)

   - Install: reStructuredText (Code analyze, preview)

   - Install: reStructuredText Syntax highlighting 

   - .vscode/settings.json must contain:

.. code-block:: bash

   {
       "esbonio.sphinx.buildDir" : "${workspaceFolder}/_build/html",
       "esbonio.sphinx.confDir"  : "${workspaceFolder}",
       "esbonio.sphinx.srcDir"   : "${workspaceFolder}"
   }

-	git clone -> to clone from your fork (you have to clone it only once) 

VS-Code: When you now open a `*.rst` document and hit Ctrl + Shift + R it will build the entire Sphinx project and display the result in a new editor tab. Watch on the bottom right: it takes a while to do it the first time.


Build the Manual
================

Details see |kdenlive_doc| 

.. |kdenlive_doc| raw:: html

   <a href="https://invent.kde.org/documentation/docs-kdenlive-org" target="_blank">kdenlive_doc</a>

Fork the "Kdenlive.org Documentation Website" repository (https://invent.kde.org/documentation/docs-kdenlive-org) if you want to contribute to Kdenlive manual. A **fork** is a copy of a repository.

.. figure:: /images/kdenlive_fork.png
   :width: 450px 
   :alt: kdenlive fork
      
   Fork the Kdenlive documentation repository

**fork** is not a command in Git, but offered in GitLab.

.. figure:: /images/personal_projects.png
   :width: 450px 
   :alt: personal projects
      
   The Fork appears under your personal projects
   
Now we have our own copy of docs-kdenlive-org on: https://invent.kde.org/your-name/docs-kdenlive-org

Our own fork is only on GitLab. We also want a clone on our local Git to keep working on it on our PC.

A **clone** is a full copy of a repository on your local machine, including all logging and versions of files.

Start Visual Studio Code:

Hit F1 and type Git:clone, now copy your fork link into the field: https://invent.kde.org/your-name/docs-kdenlive-org.

Select a folder were you like to store the documentation on your PC.

git CLI:

Get the link to clone your repository (insert the screenshot here)

Go to the directory where the clone will be. Important: The git clone command will create a new directory and put the files there. So if you want the clone directory to be ~/Documents/repo/docs-kdenlive-org you must navigate to ~/Documents/repo, open a Terminal and start the git CLI commands.

git clone <clone_string_copied_from_github>

git remote -v

If this shows only origin <clone_string_copied_from_github> go to the kdenlive manual repository and get the clone link. Then enter

git remote add upstream <upstream_link>

This creates the link to the kdenlive manual repository needed for pulling changes from the master to your fork.

git status

At this stage this should report all good. If not take care of any issues git reports (in most cases there are suggestions or even instructions how to fix it).

Create a branch in your gitlab repository (see Editing the Manual below)

git checkout <branch_name>

This command starts tracking all changes to the branch. <branch_name> is case sensitive.


Editing the Manual
==================

Start Visual Studio Code

Go to source control

Create a branch from the master branch. The branch has to start with “work/new_branch-name”. Make this new branch your current branch. You see the branch name in the source control Message window.

Go to the explorer and choose a `*.rst` file you like to change.

File name: importing_and_assets_management.rst -> all lower case, use underscore, no space, maximum 40 characters.

More details about rst see here :ref:`rst_template.rst`
 
Do not change to much at once.

git CLI:

Use the editor of your choice to edit the *.rst files. 

Use this CLI command to create the full kdenlive documentation web site locally in order to check your editing:

sphinx-build -b html repo/docs-kdenlive-org/ test_docs/build/html

This example assumes the branch was cloned to the directory/folder ~/path/to/repo/docs-kdenlive-org/ and the local web site will be build in ~/path/to/test_docs/build/html/. Navigate to ~/path/to/ and open a Terminal and enter the sphinx-build command. Once sphinx has built the pages you can use the browser of your choice to open the site and check out your editing.

Commit
------

Once you are done you see all changed files in the source control. 

**Branch**: Make sure you have changed to the branch “work/new_branch-name”

**Stage**: Select the files you want to commit and click on Stage.

**Commit & Push**: Select on the blue banner on the down arrow Commit & Push. The new branch with the changed files is pushed to your repository on Gitlab

Login to your Gitlab repository and you see the question “create merge request to Kdenlive-Doc”? Click yes and your merge request get created in the Kdenlive Doc.

Important: Wait with new changes and commits until your merge request is merged otherwise you get merge conflict as your local files are newer than the files in Kdenlive Doc.

**Git:pull**: Once the merge request is accepted: in VScode hit F1 and type “git:pull”. This pulls the latest version from Kdenlive Doc to your local PC.

Now you can start with new changes.

git CLI:

Check the status of your changes:

git status

It will list all the files that have been changed, added or deleted in red indicating that they are not (yet) part of a commit. If the list shows files in green they are already part of a commit.

To add individual files to a commit use

git add <filename_or_folder>

To add everything git status listed in red:

git add .

Once all files you want to include in the commit have been added and are listed in green in git status you can bundle up the commit:

git commit -m "<commit_message>"

You tell git where the commit goes to with

git push origin master

Remember that git remote -v shows the name of the 'origin'. 'master' is the main "branch" from where you created your branch <branch_name>.

You finalize the commit and send it to your fork with

git push

When you do this for the first time you may need to config git with your gitlab user name and email to pass the git audit:

git config --global user.name <gitlab_user_name>
git config --global user.email <gitlab_user_email>
git commit --amend --reset-author

If something goes wrong during the push due to other commits:

git fetch
git pull

... and then try the git push again.

Once the commit has been accepted and successfully merged with the kdenlive documentation repository the branch <branch_name> is deleted. It is now a good idea to purge your local working directory:

Navigate to where the branch was cloned to. In our example ~/path/to/repo/docs-kdenlive-org. Remove everything either with the file manage of your choice or using

rm -rf <clone_name>.git
cd ..
rm -rf <clone_name>

We now need to bring the Kdenlive documentation repository with the latest and creates changes into our fork:

git checkout master /# this directs changes to the master branch of our fork

git fetch upstream /# this initiates the pulling of the Kdenlive doc repo

git pull upstream master /# this executes the pull

git push origin master /# this pushes the pulled Kdenlive doc repo into our fork

Now we need to purge the directory again just in case. Then we create a new branch in gitlab and copy the branch URL.

git clone <new_branch>

git checkout <new_branch>

Search
------

Set following exclusion: `*locale`, `*po`. This will avoid that VScode search in the translation files.

.. Hint::

   Folder delete: When you delete a folder delete in the top `*.rst` file the “toctree” entry as well. Otherwise, it generates links which doesn’t exist.


Translations
============

Will follow.