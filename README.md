# README
## 使用指南
### 所需环境
python3
```
python3 -m pip install -r requirements.txt
```
### 命令参数
```
python3 main.py -h

usage: main.py [-h] [-f FILE] [-u URL] [-p POC] [-t THREAD]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  url文件路径
  -u URL, --url URL     主机地址
  -p POC, --poc POC     poc名,多个以逗号隔开,支持*号模糊匹配
  -t THREAD, --thread THREAD
                        线程数量(默认1500,数量越低，准确率越高)
```
注：
1、-u或-f为必填参数，二者二选一，即为单个扫描或者批量扫描
2、-p为可选参数，不加默认全扫poc。支持单个、多个、模糊poc扫描。分别如：
    -p poc-yaml-74cms-sqli
    -p poc-yaml-74cms-sqli,poc-yaml-74cms-sqli-1
    -p \*74cms\*
3、-t为可选参数，不加默认线程数为1500。可根据实际情况自定义
### 结果打印
终端结果就打印三种回显：
1、[+]开头即为存在漏洞的url，和对应poc
2、[-]开头即为不存在漏洞的url,和对应poc
3、[!]开头即为url连接失败或程序报错，可作不存在漏洞处理
程序运行时，会实时将存在漏洞的url和poc名称保存至当前目录的vuln.txt中，漏洞验证可向pocs目录中找到对应的python文件，查看代码分析。
## 自定义poc编写
### 较其他扫描器优势
1、自定义poc比较灵活，没有具体模板要求。只需要自定义一个py文件，编写函数，函数名为scan,代码逻辑随意，无其他硬性要求，若存在漏洞，scan函数返回True,不存在漏洞，scan函数返回False即可完成一个自定义poc编写。
2、也可自行调用其他库，如socks库等编写端口未授权漏洞等，不局限于web端漏洞。此功能的poc也在计划开发中，预计v2版本更新。
## poc更新
此工具为个人编写，暂无商用计划，所以poc的后续增加，只能等我慢慢去撸，有兴趣交poc的大佬也可私聊我，微信号：eval_POST ,经济困难，暂无奖励哈，全凭自愿，实现共赢！！
近期更新频率为每周一或周五更新，数量不等，有多少更新多少哦！！
