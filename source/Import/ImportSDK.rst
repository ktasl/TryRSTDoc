Import SDK
~~~~~~~~~~

此小節不同於\ `Import Sample
Project <#import-sample-project>`__\ 而是介紹如何只將 SDK 匯入到
**你的應用程式專案** 中 > [注意!!] 本章節只注重於 **匯入SDK**
，不保證SDK為最新版本，因此一定要繼續 **`Update
SDK <#markdown-header-update-sdk>`__**

1. 請下載
   **`BeaconNotifyLite.zip <https://bitbucket.org/beacondemoteam/as-beaconnotifydemo/downloads/BeaconNotifyLite.zip>`__**
   檔案，，下載後解壓縮為 **BeaconNotifyLite** 資料夾
2. 將此資料夾複製到 **你的project** 目錄下
3. 請下載
   **`fabric.zip <https://bitbucket.org/beacondemoteam/as-beaconnotifydemo/downloads/fabric.zip>`__**
   檔案，將壓縮檔中的 ``fabric.properties`` 複製到 ``app\build.gradle``
   同目錄下
4. 打開 *project:raw-latex:`\setting`.gradle*\ 檔案，於最下方新增：

   ::

        include ':BeaconNotifyLite'

5. 於 *app:raw-latex:`\build`.gradle* 中，新增如下代碼：

   ::

        buildscript {
            repositories {
                maven { url 'https://maven.fabric.io/public' }
            }
            dependencies {
                classpath 'io.fabric.tools:gradle:1.21.5'
            }
        }
        apply plugin: 'com.android.application'
        apply plugin: 'io.fabric'
        ...
        ...
        ...
        defaultConfig {
            applicationId "Your Application ID"
            manifestPlaceholders = [ LibApplicationId:applicationId]
        }
        ...
        ...
        ...
        dependencies {
            // Support lib
            compile 'com.android.support:support-v4:23.0.1'
            compile 'com.android.support:appcompat-v7:23.0.1'
            compile 'com.android.support:cardview-v7:23.0.1'
            //Glide, Image loader
            compile 'com.github.bumptech.glide:glide:3.7.0'
            //OkHttp
            compile 'com.squareup.okhttp3:okhttp:3.2.0'
            //EventBus
            compile 'org.greenrobot:eventbus:3.0.0'
            //Gson
            compile 'com.google.code.gson:gson:2.6.2'
            //BeaconNotifyLite
            compile project(':BeaconNotifyLite')
        }

6. 並於你的 ``Activity`` 中 `初始化 Beacon
   SDK <http://-dc-beaconnotifydemo.readthedocs.io/3.%20Init/>`__
7. 完成後執行 ``Make Project``

    [注意!!] 請記得將 ``Your Application ID`` 改成您的專案 ID

--------------