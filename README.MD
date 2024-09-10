# RAM Filler

## About app + how to use

This code will be very useful for PC technicans, benchmarks, etc. Let's say you want to fill 2GB of RAM, with a turned ON safe mode, and with a live update of usage. You clone this repository, and then enter:

	python main.py 2048 1 0 (or instead of 0 set any amount of seconds, if you want to refresh app with delay)

It will fill 2GB of RAM of your laptop. Instead of 2048 you can enter even 1MB, or 128GB, if you actually need it. That's a very useful tool for programmers/coders, because you can check how fast your app will work with a small amount of available RAM without running a lot of different apps just to fill it. And it's even more important for game developers, try it!

Inside this repository you can also find a second variant of this app (main_second.py), but he is less powerful. His usage is also for a little different.

This app is terminal-based forever, because code runned only inside terminal will be never freezed. Also it's better to get a true results, becaue GUI can consume significant amount of RAM.

## Attention!

I'm not sure about how safe this app is. As I know, fully filled RAM will not affect any parts of you computer, but probably it will just fully freeze him. Use this app without filling 1TB of RAM on your 1GB Raspberry PI! Add in one time +512MB-1GB, to find this point of affected performance in a bad way.

Or use:

	python main.py <RAM> 1 (to turn on safe mode, or 0 to run app without him) 0

With a turned ON safe mode, it will automatically shutdown application if usage of RAM will be more than 90%

## To-Do

I think it will be a good idea to create a full benchmark instead of RAM filler only. I'm not sure about how good is Python for this purpose it, but probably we have to try to do it. We can create an app which will fill CPU, GPU, RAM, but I think not HDD/SSD (it will destroy them very fast, do it will maximum run it for 5-10 seconds to check his speed)
