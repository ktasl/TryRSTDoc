其他 Beacon 元件控制函式
========================

此章節介紹其他的一些 Beacon 元件的控制函式

--------------

Stop Beacon SDK
~~~~~~~~~~~~~~~

此函式將會停止 Beacon SDK 於背景的服務，若要重新啟動請重新 Init

    目前已知會有 Leak Warring 出現

.. code:: java

    sBeaconNotifyLib.stop();

--------------

Show Event Bubble
~~~~~~~~~~~~~~~~~

此函式將會將浮動泡泡顯示於螢幕上

    請注意顯示模式必須要為 MODE\_BUBBLE\_CARD 才可使用此函式

.. code:: java

    sBeaconNotifyLib.showEventBubble(mContext);

--------------

Close Event Bubble
~~~~~~~~~~~~~~~~~~

此函式將會將目前顯示的浮動泡泡關閉

    請注意顯示模式必須要為 MODE\_BUBBLE\_CARD 才可使用此函式

.. code:: java

    sBeaconNotifyLib.closeEventBubble();

--------------

Show Event List
~~~~~~~~~~~~~~~

此函式將會將廣告訊息列表顯示於螢幕上

    請注意顯示模式必須不為 MODE\_NO\_UI 才可使用此函式

.. code:: java

    sBeaconNotifyLib.showEventList();

--------------

Close Event List
~~~~~~~~~~~~~~~~

此函式將會將目前顯示的廣告訊息列表關閉

    請注意顯示模式必須不為 MODE\_NO\_UI 才可使用此函式

.. code:: java

    sBeaconNotifyLib.closeEventList();

--------------
