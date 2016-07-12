匯入專案
========

此章節將介紹如何匯入 範例專案及 SDK \* \* \*

本元件使用 Android Studio 作為開發工具(IDE)，因此建議使用 Android Studio
作為開發工具最為快速。

以下範例皆為使用 Android Studio 作為環境使用

    如果你是第一次開發 Android 應用程式，建議你先了解如何開發 Android
    應用程式後再來使用元件，關於Android開發教學，官方網站上有許多資源，請自行參考(\ `Link <http://developer.android.com/intl/zh-tw/sdk/index.html>`__)

Import Sample Project
~~~~~~~~~~~~~~~~~~~~~

    [注意!!] 本章節只注重於 **匯入範例專案**
    ，不保證SDK為最新版本，因此一定要繼續 **`Update
    SDK <#update-sdk>`__**

1. 請至
   **`Downloads <https://bitbucket.org/beacondemoteam/as-beaconnotifydemo/downloads>`__**
   頁面，點選
   ``Download repository``\ ，下載後解壓縮為一個資料夾(\ *名稱自訂*)至你習慣的工作環境(\ *work
   space*)中。
2. 請下載
   **`fabric.zip <https://bitbucket.org/beacondemoteam/as-beaconnotifydemo/downloads/fabric.zip>`__**
   檔案，將壓縮檔中的 ``fabric.properties`` 複製到
   ``BeaconNotifyApp\build.gradle`` 同目錄下
3. 打開 Android Studio IDE
4. 點選 "Open an existing Android Studio Project"
5. IDE 會詢問 "Select Modules to Include in Project Subset"，點選 ``ok``
   即可。
6. IDE 開始載入專案並且自動 Build 第一次
7. 請記得要參考 API文件中的 Initial Beacon SDK 章節,
   寫入屬於你自己專案的 License Key

--------------

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

Update SDK
~~~~~~~~~~

此小節主要是說明如何更新 Beacon Notify SDK > BeaconNotifyLite.aar
將會持續更新並且保持於最新的版本

1. 請下載
   **`BeaconNotifyLite.aar <https://bitbucket.org/beacondemoteam/as-beaconnotifydemo/downloads/BeaconNotifyLite.aar>`__**
   檔案，並覆蓋 ``BeaconNotifyLite`` 專案中的 ``BeaconNotifyLite.aar``
   檔
2. 點選 ``Build`` → ``Clean Build``\ ，讓系統重新產生一份元件參考資源
3. 完成

--------------

Eclipse環境 (#Discard)
~~~~~~~~~~~~~~~~~~~~~~

    本說明依據
    Mars版本說明，而不同的Eclipse版本設定上會有所不同，請自行參考網路資料
    由於眾多套件已不支援於Eclipse上使用，因此Eclipse版本元件已不再更新

1. Eclipse
   開發專案請參考\ `這裡 <https://bitbucket.org/beacondemoteam/ec-beaconnotifydemo>`__
2. 請至 **Eclipse 專案中的[Downloads][id-download-ec]** 頁面，點選
   ``Download repository``\ ，下載後解壓縮為一個資料夾(\ *名稱自訂*)至你習慣的工作環境(\ *work
   space*)中。
3. 開啟 Eclipse IDE
4. 選擇 ``File`` → ``Import`` → ``Android`` →
   ``Existing Android Code Into Workspace`` → ``Next``
5. 選擇 剛剛資料夾中的 **(Eclipse)BeaconNotifyLite** 資料夾 → ``Finish``
6. 本元件有用到 **android.support.v7**\ 中的 **appcompat** ,
   **cardview** , **recyclerview** , 請自行上網查詢如何匯入資源
7. 重複步驟2. 將 **(Eclipse)BeaconNotifyApp** 專案資料夾也匯入到 Eclipse
   中
8. 檢查 **(Eclipse)BeaconNotifyApp** 的專案設定，看是否有成功與
   **(Eclipse)BeaconNotifyLite** 專案相依, 若無則請將彼此相依
9. Eclipse 尚須安裝 fabric套件及更改註冊檔，容我後續再做文件更新
