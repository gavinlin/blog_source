Android 持久化数据 system properties
####################################################

:date: 2014-03-12
:tags: properties
:category: android
:author: Gavin 

我用 android 的键值对保存系统状态，好处是 java 和 native code 都可以调用到。但需要系统权限。

键值需要是 persist 开头的以 . 隔开的关键字。例如 persist.audio.analog 。其保存形式是文件。 我们可以在 /data/property 看到以关键字命名的文件。里面的内容便是其值。

对于 java 的接口

.. code-block:: java

    import android.os.SystemProperties;
    SystemProperties.get(String key);
    SystemProperties.set(String key, String value);

对于 c 的接口

.. code-block:: c++

    // system/core/include/cutils/properties.h
    #include <cutils/properties.h>
    int property_get(const char *key, char *value, const char *default_value);
    int property_set(const char *key, const char *value);

