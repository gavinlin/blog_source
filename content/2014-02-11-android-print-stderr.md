Title: android 打印 stderr
Date: 2014-02-11
Category: android
Tags: jni

>mark

android 默认的 stderr 没有重定向到 logcat ，如果想在 logcat 上打印本地程序的错误信息，可以输入下列命令。

    adb shell stop
    adb shell setprop log.redirect-stdio true
    adb shell start
