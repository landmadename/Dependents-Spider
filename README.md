# Dependents Spider

> 看看用这个Library的最好的项目

当你学一个库的时候，可能总想看看其他人在用这个库做什么

当你在用一种技术的时候，可能总想看看别人能玩出什么花样

只要你给出地址，我就帮你找到



## 先聊聊

当你在Github上看到一个库，你可能会在这里看到一个 Used by，这里就可以看到使用这个库的其他项目

![1582360119429](C:\Users\LMN\AppData\Roaming\Typora\typora-user-images\1582360119429.png)

当然，你也可以在网址后面加上 ```/network/dependents```查看

但是你在页面里是按时间排序的，而且只有 “上一页”，“下一页” 来控制前后。而且，这个是没法按 Star 和 Fork 来排序的。而且，还没法搜索。

简单来说，这个乐色没法用。

那解决方法就是用爬虫把他整下来，把它变成一个表格。

## 预览

![1582361854949](C:\Users\LMN\AppData\Roaming\Typora\typora-user-images\1582361854949.png)

## 用法

在 ```main.py``` 里的path 填入dependents的网址

```
python main.py
```

在该目录下会生成一个```index.html```，打开就好了



## 感谢

表格控件用的是[DataTables](https://datatables.net/)