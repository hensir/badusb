# 文件说明
document包
ui_document.py      # 主窗口UI
myFromDoc.py        # MDI需要使用的文本框  考虑放到一个文件里
myDocument.py       # 主窗口 MDI

function包
ui_function.py      # 功能区组件UI
ui_selectdialog.py  # 功能区组件点击选择对话框UI
Enmu_Key.py         # 功能区组件点击选择对话框需要用到的各种"枚举"变量
DialogKeyPushButton   # 用来创建对话框中的按钮的字典 同时存储了对应的十六进制数值 用于后期define
mySelectDialog.py   # 功能区组件点击选择对话框业务逻辑文件
DuckToDigi.py       # 功能区组件点击选择对话框中Ducky脚本转换成Digi语法的一个函数文件
CodeList.py         # 功能区组件点击选择对话框中 存储第二个层叠窗口中ListWidget中的项的data
myFunction.py       # 功能区组件业务逻辑文件

主窗口文件    
myFunDoc.py         # Function加上Document 就是最终的窗口啦

# 软件说明
如果使用了头文件没有定义的按钮 将会由我的软件定义一个常量 他的前缀会是小写的key 

# 未实现功能
## document
### 主题
打算做一个Material Design的主题
### 语法高亮
我们主窗体的textEdit是可以做一个badusb语法高亮 这样更好看 那么qt也提供了QSyntaxHighlighter类供我们使用
### DOCK区域
新加入的这个功能区域 可以随便将文本编辑框放在主窗口的上下左右以及悬浮
### 文本编辑框
新窗口 页面设置 打印 使用bing搜索 转到 查找等功能都没做
### 鼠标操作
看到还有这个光标的移动操作
### 键盘录制
就像脚本精灵那样

## function
### 预览代码
就是把这个badusb的代码 转成python的键盘操作 来进行一个预览；aotogui扩展库可以做到
### 截获快捷键(HOOk)
我们现在是抓不到这个 被windows全局绑定的快捷键的 所以需要pyhook一下 例如 win+e我们的lineEdit是接受不到的
### 通写
ducky脚本和digi脚本都支持


