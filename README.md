# 文件说明
myMainWindow.py     主程序窗体业务逻辑文件

myKeyDialog.py      按键对话框业务逻辑文件

ui_mainwindow.py    主程序窗体文件

ui_keyDialog.py     案件对话框窗体文件

KEY.py  按键映射文件                 

# 软件说明
如果使用了头文件没有定义的按钮 将会由我的软件定义一个常量 他的前缀会是小写的key 

# 未实现功能
## 现在

### 代码优化
两个lineEdit 可能可以用一个槽函数来做主输入 目前是 传过来 keylist和keystatus
#### 先看一下
DigiKeyboard.sendKeyStroke(KEY_ENTER, MOD_CONTROL_LEFT | MOD_SHIFT_LEFT);

DigiKeyboard.sendKeyStroke(0, MOD_CONTROL_LEFT | MOD_SHIFT_LEFT);

DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);

DigiKeyboard.sendKeyStroke(0, MOD_GUI_LEFT);

DigiKeyboard.sendKeyPress(KEY_R);

DigiKeyboard.delay(3000);

DigiKeyboard.sendKeyPress(0);       # 按3秒的r键

DigiKeyboard.sendKeyPress(KEY_E, MOD_GUI_LEFT);

DigiKeyboard.delay(2000);

DigiKeyboard.sendKeyPress(0);   # 开两秒的资源管理器

##### 对话框
就是 我们主动的限制 用户的代码输入 目前的一些思路
用户在按键对话框中 当文本编辑框中 已经有了一个key或者 modifiers
1. 那么 当用户再次点击key值 将会直接替换掉 lineEdit中的key值
2. 然后 我们的modifiers 并不能这样做 它是那种 点一下显示 再点一下就消失
3. 最后 我们有 8个modifiers 右边那四个就放到全部按键中  只是它们已经被头文件定义了 对吧 
4. 记得左边的四个颜色标记一下
5. 我们已经明白了 key和modifiers是两个不同的东西 那么我们将会考虑恢复 modifiers所代表的key值 比较麻烦 因为还要再查那个表 按顺序生成 可能还要适配他的tooltip
6. 按键不松我们还要考虑如何接收用户指定的时间


## 未来
### 代码规范
你整个仓库都没有进行pylint检测吧
### 预览代码
就是把这个badusb的代码 转成python的键盘操作 来进行一个预览；aotogui扩展库可以做到
### 截获快捷键
我们现在是抓不到这个 被windows全局绑定的快捷键的 所以需要pyhook一下 例如 win+e我们的lineEdit是接受不到的
### 主题
打算做一个Material Design的主题
### 语法高亮
我们主窗体的textEdit是可以做一个badusb语法高亮 这样更好看 那么qt也提供了QSyntaxHighlighter类供我们使用
### 界面小优化
智能的花里胡哨 对话框的生成位置可以生成到主窗口的边缘 哪边距屏幕边缘远就靠在主窗口的哪边
### 鼠标操作
看到还有操作