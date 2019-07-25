我们需要两个软件：Pycharm和Anaconda。其中Pycharm作为Python编辑器，Anaconda作为编译器，同时Anaconda可以提供许多第三方Python库的安装。下载网址如下：

Anaconda：https://www.anaconda.com/distribution/

Pycharm：https://www.jetbrains.com/pycharm/download/#section=windows

Anaconda选择Python3.7的64-Bit Graphical Installer下载，注意您所用的电脑系统版本不要选错

如果为在校学生，可以免费使用专业版Pycharm，其他情况只能自行百度搜索破解方法了（手动滑稽），但其实用Community版也无妨

下载完毕后先安装Anaconda，记住你的安装路径，勾选选项Add Anaconda to my PATH environment variable 一路确认即可
Anaconda安装完毕后，运行命令行（搜索中输入cmd回车），输入python，看看是不是Anaconda版本，输入exit（）退出。
![命令行中运行python](https://github.com/FabregasZhou/Python-class/blob/master/class_0/class_0_pics/1.PNG)
若无法打开python或python不是Anaconda版本，则需要修改系统变量，在系统变量中的PATH中加入Anaconda安装目录 xxx\Anaconda和其子目录xxx\Anaconda\Scripts
![修改系统变量](https://github.com/FabregasZhou/Python-class/blob/master/class_0/class_0_pics/2.PNG)

然后安装Pycharm，根据提示一步步安装即可。安装完后打开Pycharm，选择create new project，勾选Existing interpreter，选择Anaconda目录下的python.exe，勾选Make available to all projects，然后点击create即可。
![勾选Existing interpreter](https://github.com/FabregasZhou/Python-class/blob/master/class_0/class_0_pics/3.PNG)
![勾选Make available to all projects](https://github.com/FabregasZhou/Python-class/blob/master/class_0/class_0_pics/4.PNG)

Anaconda安装完后在开始菜单会有一个Anaconda文件夹，打开Anaconda Prompt，输入conda list查看目前安装的所有第三方库，再输入conda update --all更新所有库。
