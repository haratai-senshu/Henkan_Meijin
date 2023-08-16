import os
import wx
import time
import ffmpy
import ffmpeg
j1 = os.path.dirname(os.path.abspath(__file__))

class FileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window #ファイルをドロップする対象

    def OnDropFiles(self, x, y, filenames):
        for file in filenames:
            self.window.box.SetValue(file)
            dnd = self.window.box.SetValue(file)

class FileDropTarget2(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window #ファイルをドロップする対象

    def OnDropFiles(self, x, y, filenames):
        for file2 in filenames:
            self.window.box2.SetValue(file2)
            dnd2 = self.window.box2.SetValue(file2)

class FileDropTarget3(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window#ファイルをドロップする対象

    def OnDropFiles(self, x, y, filenames):
        for file3 in filenames:
            self.window.box2.SetValue(file3)
            dnd3 = self.window.box2.SetValue(file3)



class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        frame = wx.Frame(None, wx.ID_ANY, "ファイル形式変換の達人", size=(400, 550) , style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.MINIMIZE_BOX)
        panel_ui = wx.Panel(frame, -1)
        frame.Show(True)



        array = ("選択" , ".mp3", ".wav", ".gif" , ".jpeg" , ".jpg" , ".png" , ".aac", ".aif" , ".flac" , ".tta" , ".tak" , ".ape" , ".wma" , ".bmp" , ".avi" , ".mov" , ".wmv" , ".flv" , ".mpg" , ".mp4")
        # コンボボックスの設置
        #self.combo = wx.ComboBox(panel_ui, -1, u'選択', choices=array , pos=(220,271))
        self.combo = wx.ComboBox(panel_ui, -1, u'選択', choices=array , pos=(220,278) , size=(50,70) , style=wx.CB_READONLY)
        combochoi = self.combo.SetStringSelection('選択')
        combo_text=self.combo.GetValue()




        self.label= wx.StaticText(panel_ui, -1, 'ここにドロップしろ(変換するファイル)', pos=(10, 10))
        #日本語なら、一文字８必要になる

        bobo=wx.StaticText(panel_ui, -1, '______________________________________________________________________', pos=(15, 35))
        bobo2=wx.StaticText(panel_ui, -1, '______________________________________________________________________', pos=(15,210))

        self.bobo3 = wx.StaticText(panel_ui, -1, ' ', pos=(15, 49), size=(350, 170))

        bobo3 = wx.StaticText(panel_ui, -1 , '______________________________________________________' , pos=( 108,386 ))

        self.bobo44 = wx.StaticText(panel_ui, -1 , ' ' , pos=(110,400) , size=(264.9999999999999999999999999999999999999999999999999999999999999999999999,40))
        self.bobo55 = wx.StaticText(panel_ui, -1 , ' ' , pos=(5,435) , size=(390,55))


        btn = wx.Button(panel_ui, -1, '参照', pos=(20, 270) , size=(65,40))
        btn.Bind(wx.EVT_BUTTON, self.clicked)


        self.box = wx.TextCtrl(panel_ui, -1, pos=(6, 235) , size=(370,25))#ここに絶対パスが入る
        sbtext = self.box.GetValue()

        rabelfile = wx.StaticText(panel_ui, -1 , 'ファイルの拡張子' , pos=(116,284.5))
        font2 = wx.Font(9.5, wx.FONTFAMILY_DEFAULT , wx.FONTSTYLE_NORMAL , wx.FONTWEIGHT_NORMAL)
        rabelfile.SetFont(font2)

        rabelyajirusi = wx.StaticText(panel_ui, -1 , '⇒' , pos=(205,282))
        font = wx.Font(11.5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        rabelyajirusi.SetFont(font)



        btn2 = wx.Button(panel_ui, -1, '変換開始', pos=(280,270), size=(90,40))
        btn2.Bind(wx.EVT_BUTTON, self.clicked444)

        self.bobo5 = wx.StaticText(panel_ui, -1, '___________________________________________________________________________',pos=(4,310))
        self.bobo6 = wx.StaticText(panel_ui, -1, '___________________________________________________________________________',pos=(4,485))

        self.bobo4 = wx.StaticText(panel_ui, -1, '出力先のファイル', pos=(15,335))

        self.box2 = wx.TextCtrl(panel_ui, -1, pos=(6,360) , size=(370,25))
        sbtext2=self.box2.GetValue()


        btn3 = wx.Button(panel_ui, -1, '参照', pos=(20,395) , size=(85,36))#出力の参照
        btn3.Bind(wx.EVT_BUTTON, self.clicked333)


        dt = FileDropTarget(self)
        self.bobo3.SetDropTarget(dt)


        dt2 = FileDropTarget2(self)
        self.bobo44.SetDropTarget(dt2)

        dt3 = FileDropTarget3(self)
        self.bobo55.SetDropTarget(dt3)


    def clicked333(self, event):
        folder = wx.DirDialog(self , style=wx.DD_CHANGE_DIR , message="保存先フォルダ")

        if folder.ShowModal() == wx.ID_OK:
            self.folder = folder.GetPath()
            sefo=self.folder#sefoにファイルパスの情報を入れる
        folder.Destroy()
        self.box2.SetValue(sefo)

    def clicked444(self, event):

        sbtext = self.box.GetValue() #ファイルのフルパスが入る
        sbtext2=self.box2.GetValue() #ディレクトリのパスが入る

        combo_text=self.combo.GetValue() #拡張子が入る

        filepath=sbtext
        basename_without_ext = os.path.splitext(os.path.basename(filepath))[0]
        basename=basename_without_ext
        basename2 = os.path.basename(filepath)#ファイル名だけを抽出している。
        #dirname = os.path.dirname(filepath)
        #huhu33=("sdihihhfgisirehqiwjeiphapodjfapjdifhawejfoiahw")
        #huhu22=("あsdkljfaklhiajdklfhadjcnbzkf2-09820911i939381923dkjaeij992849201491194jidijghwuhahalkjaoijaejaidhfakbfouahwe" + huhu33 )
        #dircopy = (dirname + '/' + huhu22 + basename2)

        path22 = (sbtext2 + '/' + basename + combo_text)#出力ファイルのフルパス
        kaku = os.path.exists(path22)


        if os.path.isfile(sbtext):
            print("jk0")
            jk5="tyo3"
        else :
            print("0.2")
            jk5="jojo2"

        if os.path.isdir(sbtext2):
            print("jk1")
            jk4="tyo2"

        else :
            jk4="jojo"
            print("jk2")

        if combo_text=="選択" :
            jk2="jojo"
            print("jk3")
            False

        else :
            print("jk4")
            jk2="tyotyo"


        t98="e"
        if "gu"==t98 :
            print("ok")

        elif jk5=="jojo2":
            print("jk7.3")
            failshuturyoku = wx.MessageDialog(None , u'変換するファイルを選んでください。' , 'エラー' , style=wx.ICON_ERROR | wx.OK)
            failshuturyoku.ShowModal()

        elif jk4=="jojo" :
            print("jk7")
            shuturyokusaki = wx.MessageDialog(None , u'出力先のフォルダを選択してください。' , 'エラー' , style=wx.ICON_ERROR | wx.OK)
            shuturyokusaki.ShowModal()


        elif jk2=="tyotyo" :
            print("jk8")
            True

        elif combo_text=="選択" :
            print("jk9")
            dialog2 = wx.MessageDialog(None, u'変換するファイル形式を選んでください。', u'エラー', style=wx.ICON_ERROR |  wx.OK)
            # メッセージダイアログを表示
            dialog2.ShowModal()


        thi="thi"

        if thi=="tho" :
            True

        elif jk4=="jojo" :
            False

        elif kaku == False and "tyotyo"==jk2:


            time.sleep(2)
            pathall = os.path.dirname(__file__)
            ffmpegdir = pathall + "ffmpeg/bin/ffmpeg.exe"
            stream = ffmpeg.input(sbtext)
            # 出力
            stream = ffmpeg.output(stream, path22)
            # 実行
            ffmpeg.run(stream)




            message2=wx.MessageBox(u'ファイル形式の変換が終わりました。', u'完了', wx.OK)
            message2.ShowModal()
            message2.Destroy()

        elif combo_text=="選択" :
            False
        elif "jojo"==jk4 :
            False
        elif "jojo2"==jk5 :
            False

        else:
            message232 = """
            ファイルが重複してしまうため、
                作業を続行できません。
            重複するファイルを削除すると、
                作業を続行できます。
                         """
            # メッセージダイアログを作成

            dialog = wx.MessageDialog(None, message232, u'エラー', style=wx.ICON_ERROR |  wx.OK)
            # メッセージダイアログを表示
            dialog.ShowModal()




    def clicked(self, event):
        dialog = wx.FileDialog(None, u'ファイルを選択してください')
        # ファイル選択ダイアログを表示

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()  #pathにファイルの情報を入れる
            self.box.SetValue(path)# メンバ変数tcにセット


if __name__ == '__main__':
    app = wx.App(False)
    MyApp(None)

    app.MainLoop()
