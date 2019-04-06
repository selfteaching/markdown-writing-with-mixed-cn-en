# cnenlinter：中英混排格式命令行清理工具

这是我自己用的一个简陋的 Python 程序，用来检查文本文件中（例如 markdown 文件）的中英混排的句子不符合要求的地方。

理论上它可以用来检查任何基于纯文本的文档（如 markdown、html、json、ipynb 等等），只不过是需要更换 `rules.yml` 文件中的正则表达式而已。

程序很简单：

> 1. 针对文本文件中**非纯 ascii 字符**构成的每一行逐一进行操作；
> 1. 读取 `rules.yml` 文件中的规则（正则表达式），逐一应用到该行；
> 1. 检查过程中允许使用 verbose 模式决定是否进行修正。

## 安装方法

```bash
git clone https://github.com/selfteaching/markdown-writing-with-mixed-cn-en
cd markdown-writing-with-mixed-cn-en
pip install -e .
```

## 使用帮助

```bash
cnenlinter --help

Usage: cnenlinter [OPTIONS] [FILES]...

Options:
  -c, --config-path PATH      Specify directory that contains rules file.
  -l, --log-file TEXT         Specify file name for log, default: "log.txt".
  -f, --fix-directly BOOLEAN  Fix file(s) directly, rather than save to
                              "/linted" directory. Default: True.
  -v, --verbose BOOLEAN       Ask permission before fix. Default: True.
  --help                      Show this message and exit.
```

## 最基本命令
```bash
cnenlinter *.md

也可以通过添加参数关闭 `verbose` 和 `fix-directly` 模式

```bash
cnenlinter -v False *.md
cnenlinter -f False *.md
```

此程序只在 Mac OSX 环境下测试运行过。
