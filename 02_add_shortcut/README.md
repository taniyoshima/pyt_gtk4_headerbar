# 02_add_shortcut

[戻る](../README.md)

<br>

## 内容

メニューボタン付きのGtk.HeaderBarを作成します。メニューの項目にはショートカットを指定したり、メニューをチェックボタンやトグルボタンにしたりします。

![pic](../data/pyt_gtk4_headerbar02.webp)


### メニューの記入について

メニューの作成では、①actionで選択時に実行する関数を指定、②labelで選択肢に表示するラベルを指定、③targetで関数に送る変数を指定、④accelでショートカットキーを指定する。ショートカットキーの指定は、labelでも行える。

```
  <menu id="menu">
    <section>
      <attribute name="label">Section 1</attribute>
      <item>
        <attribute name="action">win.button1</attribute>
        <attribute name="label">Button1</attribute>
        <attribute name="target">Button1</attribute>
        <attribute name="accel">&lt;ctl&gt;a</attribute>
      </item>
      <item>
        <attribute name="action">win.button1</attribute>
        <attribute name="label">Button2</attribute>
        <attribute name="target">Button2</attribute>
        <attribute name="accel">&lt;ctl&gt;b</attribute>
      </item>
    </section>
    <section>
      <attribute name="label">Section 2</attribute>
      <item>
        <attribute name="action">win.button3</attribute>
        <attribute name="label">Button3</attribute>
        <attribute name="accel">&lt;ctl&gt;c</attribute>
      </item>
    </section>
  </menu>
```

<br>

### メニューにチェックボタンを追加する。


```
        lbl_variant = GLib.Variant.new_string("Button1")
        action = Gio.SimpleAction.new_stateful(
            "button1", lbl_variant.get_type(), lbl_variant)
        action.connect("change-state", self.on_button1_clicked)
        self.add_action(action)

    def on_button1_clicked(self, action, param):
        action.set_state(param)
        print(param.get_string())


```

<br>

### メニューにトグルボタンを追加する。

```
        action = Gio.SimpleAction.new_stateful(
            "button3", None, GLib.Variant.new_boolean(False))
        action.connect("change-state", self.on_button3_clicked)
        self.add_action(action)


    def on_button3_clicked(self, action, param):
        action.set_state(param)
        if param.get_boolean():
            print('hello')
        else:
            print('hi')
```

<br>

## 参考にしたHP

[GtkShortcutsShortcut:accelerator](https://docs.gtk.org/gtk4/property.ShortcutsShortcut.accelerator.html)

### ショートカットの記入方法

単一のショートカット: <ctl><alt>delete
2 つの代替ショートカット: <shift>a Home
ショートカットの範囲: <alt>1...<alt>9
複数のキーを同時に押す: Control_L&Control_R
ショートカットまたはキーのシーケンス: <ctl>c+<ctl>x

キーを連続して押す必要がある場合 (または押す必要がある場合) は、「&」ではなく「+」を使用します (たとえば、「t キーを 2 回押す」には「t+t」を使用します)。

.ui ファイルで使用する場合は、<、>、および & を &lt;、&gt;、および &amp; としてエスケープする必要があることに注意してください。cambalaceでは、そのまま<ctl>のように記入すれば良い。

[戻る](../README.md)


[24. Application 24.4. Example](https://python-gtk-3-tutorial.readthedocs.io/en/latest/application.html#menus)