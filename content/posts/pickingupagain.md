+++ 
draft = false
date = 2024-01-06T01:32:13Z
title = "Picking up Godot4 again"
description = "Picking up development of my game"
slug = ""
authors = ["me"]
tags = ["Game Dev"]
categories = ["Game Dev"]
externalLink = ""
series = []
+++

# Starting over
## New beginings
With the help of my previously written code, I'm starting over. I'm not going to just take my old project and build on that. I think it's better to pick the good bits out of what I've written already. I'd like to make it more modular so I can share this with other communities.

### Character
Let's start with the main character and since the main character is called Little Death let's make it a skeleton. I went to [Universal LPC Spritesheet Generator](https://sanderfrenken.github.io/) and pulled down the skeleton character spritesheet. There's a scythe too which will be handy for our little death character.

I added a CharacterBody2D node to the scene and attached a Sprit2D. I'll create an Art folder in the project to store the Character and maybe other art. Surprisingly from previous versions, this CharacterBody2D when I attached a script had already some code generated. I recognise the _physics_process method and there seem to be some direction vectors and a velocity indicator. 

But that's for tomorrow it's late enough.