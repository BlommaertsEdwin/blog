+++ 
draft = false
date = 2024-01-17T21:48:00Z
title = "Adding the attacking animation"
description = ""
slug = ""
authors = ["me"]
tags = ["Game Dev", "godot"]
categories = ["Game Dev"]
externalLink = ""
series = []
+++
While listening to [Sir Patrick Steward](https://open.spotify.com/show/15S53WYXA32y7TkiOLBipy?si=fbbdc8d067d34323) divulge his memoir on Spotify. I hack away at my silly game. 

Firstly I need to key in the attacking animation for each direction. This was fairly easy as it just meant adjusting hr Frame Coords.
Next, I'm going to hook these animations in the Left Mouse button click. which again was fairly easy as I captured the input and gave a signal to the State Machine to travel to the attack state.
While entering the attack state I fired off the accompanying animation.
I got a bit stuck with what to do at the end of the animation. So as I pressed the left mouse button to attack, it would trigger the correct animation, but then it would get stuck at the end of the animation. I researched and I found the best way would be to call a function at the end of the animation where I would revert to the Idle state.

Behold LittleDeath
{{< youtube id="eTsit7vkFyQ" >}}