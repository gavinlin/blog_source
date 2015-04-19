#######################
在osx上配置android-make
#######################

:date: 2014-09-19
:category: android
:author: Gavin 

android-cmake 的网址是这个 `android cmake <https://code.google.com/p/android-cmake/>`_

-----

下载源码需要用到 hg 如果有brew 就好办了

.. code-block:: java

    brew install hg

可能装好还是用不了，这是需要连接，本来是可以自动连接的，但是出现了某些错误连接不了，例如没有某个目录的写权限，所以设置一下权限

.. code-block:: java

    sudo chown -R $USER:admin /usr/local
    brew link hg
    
------

下载源码很简单，复制下面就可以了

.. code-block:: java

   hg clone https://code.google.com/p/android-cmake/

-----

还没完，接着是下载ndk，去android官方网址下，解压下来我们需要提取交叉工具链

.. code-block:: java


   sh $NDK_ROOT/build/tools/make-standalone-toolchain.sh --platform=android-8 --ndk-dir=$HOME/android-ndk --install-dir=$HOME/arm-linux-android/arm-linux-androideabi-4.4.3 --toolchain=arm-linux-androideabi-4.4.3 --system=darwin-x86_64
   
.. IMPORTANT::
    
    需要注意我们用得交叉工具链是4.4.3，听说使用4.6有错误，待验证。
    
接着在shell配置文件中填入配置参数

.. code-block:: java

    export PATH=$PATH:$HOME/adt-bundle/sdk/tools
    
    export ANDROID_NDK_TOOLCHAIN_ROOT=$HOME/arm-linux-android/arm-linux-androideabi-4.4.3
    export ANDTOOLCHAIN=$HOME/workspace/android-cmake/toolchain/android.toolchain.cmake
    alias android-cmake='cmake -DCMAKE_TOOLCHAIN_FILE=$ANDTOOLCHAIN '

    
------

配置完成了，只要使用 android-cmake 就可以完成交叉cmake的功能了。

可以在sample中的hello-cmake试验一下。

.. code-block:: java

   android-cmake
   make
   

如果可以编译出libs/armeabi-v7a/libhello-cmake.so 就表示成了。

