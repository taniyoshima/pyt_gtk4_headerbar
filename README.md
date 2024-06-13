# pyt_gtk4_headerbar

<br>

## 内容 

Gtk.MenuButtonやGtk.Buttonを使用してGtk.HeaderBarにボタンを追加します。  
uiの作成には、cambalacheを使用します。



<br>

### [01_headerbar](./01_headerbar/README.md)

Gtk.HeaderBarにメニューをつけます。

![pic](./data/pyt_gtk4_headerbar.webp)

<br>

### [02_add_shortcut](./02_add_shortcut/README.md)

メニューにショートカットキーを設定したり、メニューにチェックボタンやトグルボタンを指定します。

![pic](./data/pyt_gtk4_headerbar02.webp)

<br>

## 履歴

2024/6/8 プログラム作成  

cambalacheにより、Gtk.MenuButton内にPopoverやmodelを定義することができますが、それを使用して作成したのではエラーが生じて、正常に動作しませんでした。このため、Gtk.PopoverMenuをPython側で定義して、それにmodelを指定して、Gtk.MenuButtonのpopoverにセットしています。

<br>

2024/6/13 02_add_shortcutを追加  

menuにショートカットキーを追加したり、menuにチェックボタンやトグルボタンにしたitemを追加する方法についてのプログラムを追加。

<br>

## 参考にしたHP
