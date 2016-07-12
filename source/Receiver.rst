事件監聽器
==========

本章節主要市介紹如何透過 Broadcast Receiver 監聽特殊事件的回傳

--------------

Custom Event Content
~~~~~~~~~~~~~~~~~~~~

    此監聽器主要為客製化事件條件成立所觸發

-  Register a Broadcast Receiver on AndroidManifest.xml

   ::

       <receiver
       android:name="yourAppID.Receiver.CustomEventReceiver"
       android:permission="yourAppID.permission.GET_ALL_TYPE_BEACONS">
       <intent-filter>
           <action android:name="receiver_custom_event" />
       </intent-filter>
       </receiver>

-  Get the Broadcast Receiver bundle content

   ::

       public class CustomEventReceiver extends BroadcastReceiver {
       long beaconId;
       int beaconPositionX;
       int beaconPositionY;
       String eventContent;
       String userDefineData;

       @Override
       public void onReceive(Context context, Intent intent) {
           if (intent.getExtras() != null) {
               //=== 這個事件感測的 Beacon 的ID @ ===//
               beaconId = intent.getExtras().getLong("BeaconId");
               //=== 這個事件感測的 Beacon 所在地圖中的位置 @ ===//
               beaconPositionX = intent.getExtras().getInt("BeaconX");
               beaconPositionY = intent.getExtras().getInt("BeaconY");
               //=== 這個事件的資訊 @ ===//
               eventContent = intent.getExtras().getString("EventContent");
               userDefineData = intent.getExtras().getString("UserDefineData");
           }
       }

       public long getBeaconId() {
           return beaconId;
       }

       public int getBeaconPositionX() {
           return beaconPositionX;
       }

       public int getBeaconPositionY() {
           return beaconPositionY;
       }

       public String getEventContent() {
           return eventContent;
       }

       public String getUserDefineData() {
           return userDefineData;
       }
       }

--------------

Custom Advertise Event Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    此監聽器主要為客製化廣告事件中，[詳細] 按鈕被點選觸碰時所觸發

-  Register a Broadcast Receiver on AndroidManifest.xml

   ::

       <receiver
       android:name="yourAppID.Receiver.CustomAdvertiseEventReceiver"
       android:permission="yourAppID.permission.GET_ALL_TYPE_BEACONS">
       <intent-filter>
           <action android:name="receiver_custom_advertise_event" />
       </intent-filter>
       </receiver>

-  Get the Broadcast Receiver bundle content

   ::

       public class CustomAdvertiseEventReceiver extends BroadcastReceiver {
       int mBeaconPositionX;
       int mBeaconPositionY;
       String mCardTitle;
       String mCardContent1;
       String mCardContent2;
       String mCardActionContent;

       @Override
       public void onReceive(Context context, Intent intent) {
           if (intent.getExtras() != null) {
               //=== 這個事件感測的 Beacon 所在微地圖中的位置 @ ===//
               mBeaconPositionX = intent.getExtras().getInt("BeaconX");
               mBeaconPositionY = intent.getExtras().getInt("BeaconY");
               //=== 這個事件的資訊 @ ===//
               mCardTitle = intent.getExtras().getString("CardTitle");
               mCardContent1 = intent.getExtras().getString("CardContent1");
               mCardContent2 = intent.getExtras().getString("CardContent2");
               mCardActionContent = intent.getExtras().getString("CardActionContent");
           }
       }

       public int getBeaconPositionX() {
           return mBeaconPositionX;
       }

       public int getBeaconPositionY() {
           return mBeaconPositionY;
       }

       public String getCardTitle() {
           return mCardTitle;
       }

       public String getCardContent1() {
           return mCardContent1;
       }

       public String getCardContent2() {
           return mCardContent2;
       }

       public String getCardActionContent() {
           return mCardActionContent;
       }
       }

--------------

Add Favorite Event Content
~~~~~~~~~~~~~~~~~~~~~~~~~~

    此監聽器主要為廣告事件中，[加最愛] 按鈕被點選觸碰時所觸發

-  Register a Broadcast Receiver on AndroidManifest.xml

   ::

       <receiver
       android:name="yourAppID.Receiver.AddFavoriteReceiver"
       android:permission="yourAppID.permission.GET_ALL_TYPE_BEACONS">
       <intent-filter>
           <action android:name="receiver_add_favorite" />
       </intent-filter>
       </receiver>

-  Get the Broadcast Receiver bundle content

   ::

       public class AddFavoriteReceiver extends BroadcastReceiver {
       @Override
       public void onReceive(Context context, Intent intent) {
           if (intent.getExtras() != null) {
               long eventID = intent.getExtras().getLong("EventID");
               String endDate = intent.getExtras().getString("EndDate");
               String mainIconURL = intent.getExtras().getString("MainIconURL");
               String backgroundImgURL = intent.getExtras().getString("BackgroundImgURL");
               String cardTitle = intent.getExtras().getString("CardTitle");
               String cardContent1 = intent.getExtras().getString("CardContent1");
               String cardContent2 = intent.getExtras().getString("CardContent2");
               int cardAction = intent.getExtras().getInt("CardAction");
               String cardActionContent = intent.getExtras().getString("CardActionContent");
           }
       }
       }

--------------

Notification Event Content
~~~~~~~~~~~~~~~~~~~~~~~~~~

    此監聽器主要為當簡訊事件被點選觸碰時所觸發

-  Register a Broadcast Receiver on AndroidManifest.xml

   ::

       <receiver 
       android:name="com.cht.beacon.notify.App.Receiver.NotificationReceiver"
       android:permission="com.cht.beacon.notify.App.permission.GET_ALL_TYPE_BEACONS">
       <intent-filter>
           <action android:name="receiver_notification" />
       </intent-filter>
       </receiver>

-  Get the Broadcast Receiver bundle content

   ::

       public class NotificationReceiver extends BroadcastReceiver {
       @Override
       public void onReceive(Context context, Intent intent) {
           Intent intent1 = new Intent(context, SplashActivity.class);
           intent1.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
           context.startActivity(intent1);
       }
       }

--------------

Position Beacon Event Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    此監聽器主要為當定位事件條件成立所觸發

-  Register a Broadcast Receiver on AndroidManifest.xml

   ::

       <receiver
       android:name="com.cht.beacon.notify.App.Receiver.PositionBeaconReceiver"
       android:permission="com.cht.beacon.notify.App.permission.GET_ALL_TYPE_BEACONS">
       <intent-filter>
           <action android:name="receiver_position_beacon" />
       </intent-filter>
       </receiver>

-  Get the Broadcast Receiver bundle content

   ::

       public class PositionBeaconReceiver extends BroadcastReceiver {
       @Override
       public void onReceive(Context context, Intent intent) {
           if (intent.getExtras() != null) {
               //=== 這個事件感測的 Beacon 的ID @ ===//
               long beaconId = intent.getExtras().getLong("BeaconId");
               //=== 這個事件感測的 Beacon 所在地圖中的位置 @ ===//
               double beaconPositionGpsX = intent.getExtras().getDouble("BeaconGpsX");
               double beaconPositionGpsY = intent.getExtras().getDouble("BeaconGpsY");
               //=== 這個事件的資訊 @ ===//
               long sBeaconId = intent.getExtras().getLong("SBeaconID");
               int RDistance = intent.getExtras().getInt("RDistance");
               int RSSI = intent.getExtras().getInt("RSSI");
               //===
               String userDefinedData = intent.getExtras().getString("UserDefineData");
           }
       }
       }

--------------
