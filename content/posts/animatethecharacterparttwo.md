+++ 
draft = false
date = 2024-01-07T00:04:17Z
title = "Using Sprite Sheets and the wonderful combo of State Charts and movement."
description = ""
slug = ""
authors = ["me"]
tags = ["Game Dev", "godot"]
categories = ["Game Dev"]
externalLink = ""
series = []
+++

Cracking on with the game. Looks like the pre-generated code for a CharacterBody2d is actually for a side scroller. I think I'll use a state machine for the player character so we can control animations or other game functions by looking at what state the character is in.

I've done some research since my last post. I've come across this [StateChart](https://github.com/derkork/godot-statecharts/tree/main) plugin for Godot. I thought it might be handy for my players and enemies. Additionally, it allows you to hook in the animations to the states. This is ideal for what I'm looking for right now and hopefully, this will help manage some of the code.

My initial thought was to use an enum type variable and tie my states to this I know from previous experience that this bloats to a massive if else section in your code. But I've decided to now try and give this state chart a chance.

I've attached the  AnimationTreeState to the HeroStateChart and slotted in an AnimationTree.

Keying in the frames was easy as I could simply use the AnimationPlayer and manipulate the Frame Coords at 0.1-second intervals to switch to a new frame. Need to make sure not to pick the x : 0 coord as that's the idle state.

I managed to hook in the state machine to the movements and input. Whereby the input changes the state and the change in states dictates the movement.

Excited about the next iteration.
