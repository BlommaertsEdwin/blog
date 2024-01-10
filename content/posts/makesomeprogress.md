+++ 
draft = false
date = 2024-01-06T15:53:04Z
title = "Installing Git plugin for Godot4 on Linux and animating a character"
description = ""
slug = ""
authors = ["me"]
tags = ["Game Dev", "godot"]
categories = ["Game Dev"]
externalLink = ""
series = []
+++
Right, time to crack on with this characters. I've loaded the sprite sheet into the Sprite2D node by dragging it over the Texture field. Now it's a matter of figuring out how many H- and Vframes are in the animation, additionally, I need to figure out the frame coordinates.

I set the Scale to x 1 and y 1 but to do this I had to unlink them, then set the values then relink them again.

So this sheet has 13 Hframes and 21 Vframes. Because there are a possible 13 animation frames on the longest row and there are 21 rows.

To put the frame in the centre I entered x -404 and y 130 in the Transform.

Setting it like this centers on the top left-most animation frame. By setting the Frame Coordinates Y variable to 10 it sets us to the 10th row which is the forward walking animation frame.

I ended up with something like the following.

![Godot4 Settings](../../images/settingsspritesheet.png)

That completed I need to now add some code versioning, looks like there's a plugin in the Godot editor for this let's try and get that working.

I found the [Wiki Guide](https://github.com/godotengine/godot-git-plugin/wiki) a bit confusing so I've written some additional steps.

I am installing this on a Linux system:
1. [Install Git](https://www.git-scm.com/)
2. Configure your username and email in Git  
    `$ git config --global user.name "your name"`  
    `$ git config --global user.email your@email.com`
3. [Generate](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) a private key and [add it to github](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. [Create a new Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) for your project.
4. Download your [Godot version plugin](https://github.com/godotengine/godot-git-plugin/wiki)
5. Create an 'addons' folder inside of your project folder. So something like the following. `projectname/addons`
6. Extract the content of the folder inside of the zipfile, into the addons folder. So it should look something like `addons/godot-git-plugin`. So we want the plugin in the folder not another folder.
7. Start your Godot 4 engine
8. Open up your project
9. Go to Editor > Editor Settings > Version Control > Version Control Settings 
9. Set your username which is found as the Account name of your github account
10. Set the paths to your private and public key Should look something like this. `/home/yourusername/.ssh/id_rsa.pub` for the public key and `/home/yourusername/.ssh/id_rsa` for the private one.
11. Go to Project > Version Control > Version Control Settings and make sure 'Connect to VCS' is enabled. (The other data should already be filled in for you.)
12. The above step will add a new tab next to the inspector, make this the active tab.
    ![New Commit Tab](../../images/NewCommitTab.png)
13. Near the bottom of the commit tab, you'll find a new window that looks like the following.
    ![Create New Remote](../../images/CreateNewRemote.png)
14. Here you need to add a new remote. Click on the three dots, and select "Create New Remote". In the 'Remote Name' field put the name of the repository you created earlier. In the Remote URL put the git@ url. Should look something like the following. `git@github.com:youraccountname/yourreponame.git`
15. That's it! You can now add changes, add a commit message, and Commit the changes, and then use the up arrow to push the changes. Or pull in changes someone else is working on by clicking the down arrow at the commit tab.