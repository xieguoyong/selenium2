;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("打开", "","Edit1")


; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)


; Set the File name text on the Edit field

  ControlSetText("打开", "", "Edit1", "C:\Users\xie.guoyong\Desktop\111.xls")

  Sleep(5000)

; Click on the Open button

  ControlClick("打开", "","Button1");