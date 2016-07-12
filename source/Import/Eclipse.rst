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