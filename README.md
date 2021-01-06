# 食用方法
- 安装python3
- python srcs/xxx.py

脚本       | 作用
:------------------| :------------------
ccolor | 将56 82 73转换为16进制颜色0x385249
datecalc| 计算2020-12-3的前25天
unzip | 解压一个文件
zip | 压缩一个文件
wxdb | 一个算法，用于解开mac微信的本地加密，注释里有用法
zhai| 计算可转债的转股溢价率

# Mac OSX优化

- 打开环境变量配置<BR>
```open ~/.bash_profile```

- 加入一个function，路径换成你本地的py路径<BR>
```
function ccolor {
    Python3  /Users/xirtam/Documents/tools/py/ccolor.py $1 $2 $3
}
```

- source一下<BR>
```source ~/.bash_profile```

- 命令行直接可以使用ccolor 12 12 12了