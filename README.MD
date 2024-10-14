<p align="center">
  <img src="EasyBench_Logo.png" alt="App Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-green"/>
</p>

# EasyBench

With this app you can benchmark any computer which you have. You can create a artificial usage of any of your PC parts, and notice how your PC will behave with it. This app is a manual benchmark, so you can set usage of your PC part (RAM, CPU) in percents or in defined value.  It's useful or if you have a very low-end PC (which can be overloaded just with one page in browser), or if you use a very powerful PC (which can't be overloaded even with 1 million of opened apps).

This app will be very useful for PC technicans, developers, gamers, benchmarks, etc. This app is terminal-based forever, because code runned only inside terminal will be never freezed. Also it's better to get a true results, because GUI can consume significant amount of resources.


## RAM BENCHMARK

Let's say you want to fill 2GB of RAM, with a turned ON safe mode and with a live refresh. You clone this repository, and then run this app. In first menu you have to enter 1 (RAM benchmark). Then you will have to set some settings, as amount of MB which app will take from your RAM, safe mode ON/OFF, and refresh time.

I recommend to not to set, let's say **4096MB** if you at all have **1024MB** (it can cause some errors)

## CPU BENCHMARK (beta version, use it on your own risk)

Currently this benchmark on the earliest stage of development, so he can only fill your CPU usage to this percent, to whose you prescribed it. At all still very useful if you have a PC with Intel Core i9 999 Gen which just can't bu turned to use maximum of his power with any heavy app.

## Attention!

**I'm not sure about how safe this app is!!!** It will better to control a temperature of your PC also with another app (as HWiNFO or Aida64).

If you know how to use benchmarks and control resources of your pc - it will NEVER damage him, because YOU set usage of your resources in it, it's a manual benchmark.

(SOON) **With a turned ON safe mode, it will automatically shutdown application if usage of your resources will be more than 90% or if one of them will achieve critical temperature**

## CPU BENCHMARK

## To-Do

1. Add benchmarks for GPU + HDD/SSD (it will destroy them very fast, so will maximum run it for 5-10 seconds to check his speed)
2. Safe mode in CPU benchmark
