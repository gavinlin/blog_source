######################
源码编译OpenCV4Android
######################

:date: 2014-09-22
:category: android
:author: Gavin 

准备工作
""""""""

+ git client
+ android cmake
+ Android NDK
+ OpenCV master:git://github.com/itseez/opencv.git.
  
使用以下命令下载源码

.. code-block:: java

    git clone http://github.com/itseez/opencv.git

.. IMPORTANT::
    
    如果看过这篇文章 http://lingavin.com/zai-osxshang-pei-zhi-android-make.html android cmake 配置不是问题。
    
------

构建opencv
""""""""""

首先确认已经配置了NDK路径

.. code-block:: java

    export ANDROID_NDK=~/android-ndk-r8e

相对地如果你想用独立的交叉工具链来编译，可以配置工具链的路径

.. code-block:: java

    export ANDROID_STANDALONE_TOOLCHAIN=~/android-toolchain

如果你没有配置上面其中一个路径，编译脚本会在 /opt 文件夹下面寻找 NDK。

.. IMPORTANT:: 
    
    例如如果你得NDK放在 /opt/android-ndk-r8e，脚本会找到的。

接下来运用以下脚本来生成cmake构建文件夹。

.. code-block:: java

    cd opencv/platforms
    sh ./scripts/cmake_android_arm.sh

现在应该会找到编译目录，然后就可以进去编译了。

.. code-block:: java

    cd build_android_arm
    make -j8
    
这样就会编译 opencv 模块，除了 Android 没有用到得 gpu，ocl，python wrapper等。

使用opencv建立控制台的Hello World
"""""""""""""""""""""""""""""""""

这个不是普通的android程序。这是一个unix控制台程序。用控制台程序可以更方便编程，调试和优化程序。如果你完成了你的cv算法，你可以切换到java+ndk实现android程序。

预备条件
========

你需要使用虚拟机或者已经root了的设备，因为我们将使用控制台运行可执行程序。

编译
========

之前编译没有问题的话，可执行程序应该是编译好了得。如果不放心，可以在 build_android_arm 里运行 make android-hello

暂时先到这里，看opencv主要是提取camera部分的。
