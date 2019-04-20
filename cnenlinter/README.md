# cnenlinter：中英混排格式命令行清理工具

这是我自己用的一个简陋的 Python 程序，用来检查文本文件中（例如 markdown 文件）的中英混排的句子不符合要求的地方 —— 其实，它只不过是一个批处理工具。

理论上它可以用来检查任何基于纯文本的文档（如 markdown、html、json、ipynb 等等），只不过是需要更换 `rules.yml` 文件中的正则表达式而已。匹配全角字符的正则表达式是：`[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD]`。

程序很简单：

> 1. 针对文本文件中**非纯 ascii 字符**构成的每一行逐一进行操作；
> 1. 读取 `rules.yml` 文件中的规则（正则表达式），逐一应用到该行；
> 1. 检查过程中允许使用 verbose 模式决定是否进行修正。

## 安装方法

```bash
git clone https://github.com/selfteaching/markdown-writing-with-mixed-cn-en
cd markdown-writing-with-mixed-cn-en/cnenlinter
pip install virtualenv
virtualenv venv
. venv/bin/activate

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
  -r, --rules-file-name TEXT  Specify rules file name. Default: rules.yml
  -v, --verbose BOOLEAN       Ask permission before fix. Default: True.
  --help                      Show this message and exit.
```

## 基本命令

```bash
cnenlinter *.md
```

也可以通过添加参数关闭 `verbose` 和 `fix-directly` 模式

```bash
cnenlinter -v False *.md
cnenlinter -f False *.md
```

还可以指定规则文件及其存放的目录：

```bash
cnenlinter -c <path-of-rules-file> -r <rules-file-name> -v False -f False *.md
# 随后可以打开 log.txt 文件查看可修订记录
```

在处理单个文件的时候，我通常会使用 `cnenlinter <file>`，因为即便是总监不小心操作出错（比如，在不应该的地方顺手敲了 `y`），也可以通过 `log.txt` 文件查找哪里出了问题。

但是，在处理多个文件的时候，我会使用 `cnenlinter -f False *.md`，即，修改过的文件将另存在 `linted` 目录中。

## 关于规则，以及 rules.yml

`rules.yml` 文件里保存着搜索（`pattern`）和替换（`expected`）的正则表达式。

每个规则由 `---` 作为起始，而后一个 `expected` 再加上一个 `pattern`，比如：

```yaml
---
# conver half-width puntuations in Chinese sentences to full-width ones.
# 中文前后的半角标点符号字符更换为全角标点符号
'expected': /\1，/
'pattern': /([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD”’])\,/
---
'expected': /\1。/
'pattern': /([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD”’])\./
---
'expected': /\1：/
'pattern': /([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD”’])\:/
---
'expected': /\1；/
'pattern': /([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD”’])\;/
---
'expected': /\1？/
'pattern': /([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD”’])\?/
---
'expected': /\1！/
'pattern': /([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD”’])\!/
---
'expected': /\1）/
'pattern': /([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD”’])\s*[\)）]/
---
'expected': /（\1/
'pattern': /[（\(]\s*([\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD‘“])/
```

正则表达式前后，使用 `/` 标记。

在 `pattern` 中允许使用三个 `flag`：`a`、`i` 和 `l` —— 分别对应着 `re.A`、`re.I` 和 `re.L`：

```
/<regex>/<flag>
```

在 `expected` 中，使用 `\1` `\2`... 来替换 `pattern` 中的捕获。

## 注意

此程序只在 Mac OSX 环境下测试运行过。
