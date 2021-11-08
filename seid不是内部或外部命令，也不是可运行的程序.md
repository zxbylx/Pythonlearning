# seid不是内部或外部命令，也不是可运行的程序

使用you-get下载b站视频时进度100%后会出现上面的报错，

解决方案：

将url中的&seid=替换为3D即可。

before

```
you-get https://www.bilibili.com/video/BV11x41117FL?from=search&seid=7624727307478602068
```

after

```
you-get https://www.bilibili.com/video/BV11x41117FL?from=search3D76247273074786020682068
```

