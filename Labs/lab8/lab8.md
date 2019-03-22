# Lab 8

## Checkpoint 1
![VTK Repository Cloned](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/repo%20clone.png)

![Initial Configuration](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/initial%20config.png)

![Disabling VTK_GROUP values](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/group%20disable.png)

![Enabling VTK_MODULE values](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/module%20enable.png)

![Final Configuration and Generation](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/final%20config:gener.png)

![Build Complete](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/build%20complete.png)

Observations: This was a very simple step, although I was stuck on it for about an hour. VTK modules are only shown if the "Advanced" checkbox in CMake is enabled. Besides that, everything was relatively straightforward and the build only took about 2 minutes when using multithreading with the -j4 flag.

## Checkpoint 2

![Nightly and Experimental Tests](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/vtk%20nightly:experimental.png)

You may see the tests run for a particular submission by viewing the "test" column on the VTK dashboard under the nightly and experimental sections. 

![Failed Test](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/testfail.png)

You can see the runtime, output, and reason for failure for all tests that failed under a particular submission. This helps debug by giving developers all of the data they need to debug.

![Similar Build](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/similar%20build.png)

The dashboard is clean and error-free.

![ctest Experimental](https://github.com/amitra1997/CSCI-49XX-OpenSource/blob/master/Labs/lab8/lab8pics/ctest%20Experimental.png)