# Markdown 简体中文与西文混排要点

**Version: 0.1**

李笑来 2019/03

---

这篇文档的标题中所使用的措辞是 “**要点**”，而非 “规范” —— 原因在于这些要点争议颇多。

然而，为了统一编辑，也为了读者阅读方便，selfteaching.com 仓库中的所有文档，应尽量遵守以下要点。

以下的要点是针对 Markdown 写作而整理的。Markdown 是纯文本文件，它们最终都需要被转换成 HTML 文档，而后再被浏览器渲染成格式文档。

## 常用标点符号

中英混排的文本中，除了完整的英文句子或段落之外，应全部使用全角标点符号。

|  名称  |       符号       |                               备注                                |
| ------ | ---------------- | ----------------------------------------------------------------- |
| 句号   | `。`             |                                                                   |
| 逗号   | `，`             |                                                                   |
| 顿号   | `、`             |                                                                   |
| 问号   | `？`             |                                                                   |
| 感叹号 | `！`             |                                                                   |
| 引号   | `“”` &nbsp; `‘’` | 弯引号                                                            |
| 冒号   | `：`             |                                                                   |
| 分号   | `；`             |                                                                   |
| 省略号 | `……`             | 共 6 个点，占据两个全角字符位置                                   |
| 破折号 | `——`             | 共 2 个 `—`，占据两个全角字符位置                                 |
| 圆括号 | `（） `          |                                                                   |
| 书名号 | `《》`           |                                                                   |
| 分隔号 | `・`             | [Katakana Middle Dot](<https://en.wikipedia.org/wiki/Interpunct>) |

**注意**

1. 分隔号统一使用占据一个全角位置的 [Katakana Middle Dot](<https://en.wikipedia.org/wiki/Interpunct>)，`&#12539;`，即，`・` ；而非键盘上可以直接打出的 `&sdot;`， `·`  —— 这个分隔号是半角符号。

2. 中英混排的文字中，单个英文单词需要用引号（单引号、双引号）括起来的时候，统一使用全角引号。英文句子中出现的引号，统一使用半角引号（单引号、双引号）。


## 空格

中英混排的文本中使用的空格是半角符号空格：` ` —— 这也更符合大多数中文输入法的习惯。

1. 中文与英文之间、中文与数字之间，都要有一个半角空格；如：`这是 1 个 variable 的例子`
2. 英文字符、数字字符，与全角标点符号之间，不应该有空格；如： `这是一个 variable，这是数字 100。`；再比如：`变量 a 的值是：8；a 的值大于变量 b。`
3. 全角引号（单引号、双引号）之外要有空格；如：`所谓的 “过早引用” 就是这样令人迷惑的。`
4. 中英文并存的句子里，英文单词若是需要用括号括起，必须使用全角引号；如：`这就是所谓的 “过早引用”（Forward References）` —— 注意，引号和括号之间没有空格。
5. 破折号（`——`）前后要各有一个半角空格。
6. 省略号（`……`）前后要各有一个半角空格。
7. 行内代码标示（Inline code）前后要有空格；如：```表达式 `a += 1` 的意思是说……```

## 倾斜

1. Markdown 中的倾斜标示，可用星号或者下划线，如， `*强调*` 或者 `_强调_`。然而，中文字符使用倾斜显示的话，在排版上会显得非常难看。
2. 在渲染（Render）时，Markdown 中的 `*强调*` 或者 `_强调_` 会被同样渲染成 `<em>强调</em>`。而 `<em>` 需由 css 设定为 `font-style: regular;`，而字体颜色则可以设置为不同的颜色以示强调。
3. 而在必须为英文单词设置强调（倾斜样式）之时，要在 Markdown 中使用 HTML 标签： `<i>` ，如：`<i>emphasis</i>`。如有必要，在 css 中再另外设置字体颜色。

## 标题

1. 标题一概使用 `#` 符号标示。

2. 由于在 GFM（Github Flavored Markdown）中，`#[0-9]+` 被自动渲染为 issue 的链接，所以，在标示标题的时候，`#`符号后应有且只有一个空格，例如：

   ```
    # 一级标题
    ## 二级标题
    ### 三级标题
   ```

3. 一个 Markdown 文件中有且只有一个一级标题。

4. 一个 Markdown 文件中最多使用到三级标题。如果层级过多，说明你可能需要将文本切分到多个文件。

## 段落

段落不使用行首缩进。

## 常用汉文数字

* 壹、贰、叁、肆、伍、陆、柒、捌、玖、拾

* 零、〇
* 廿（niàn）、卅（sà）

## 常用特殊字符

| HTML Identity | Displayed |
| ------------- | --------- |
| `&amp;`       | &amp;     |
| `&lt;`        | &lt;      |
| `&gt;`        | &gt;      |
| `&lbrack;`    | &lbrack;  |
| `&rbrack;`    | &rbrack;  |
| `&grave;`     | &grave;   |
| `&vert;`      | &vert;    |
| `&bsol;`      | &bsol;    |
| `&permil;`    | &permil;  |
| `&pertenk;`   | &pertenk; |
| `&trade;`     | &trade;   |
| `&copy;`      | &copy;    |
| `&reg;`       | &reg;     |

更多请查询：<https://www.toptal.com/designers/htmlarrows/>

## 版权声明的选择

selfteaching.com 上的所有文章，首选 [CC-BY-NC-ND](<https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh>) 版权协议，即：

> 署名-非商业性使用-禁止演绎 3.0 未本地化版本 (CC BY-NC-ND 3.0)

## 必读教程

1. [Github: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
2. [Microsoft Writing Style Guide](https://docs.microsoft.com/en-us/contribute/how-to-write-use-markdown)

## 推荐使用的 Markdown 编辑器

**Typora**: https://typora.io/

## 更多参考链接

> * https://golem.ph.utexas.edu/~distler/maruku/markdown_syntax.html
> * http://www.pinyin.info/tools/converter/chars2uninumbers.html
> * https://www.w3.org/html/ig/zh/wiki/Css4-text
> * https://www.toptal.com/designers/htmlarrows/
> * https://www.key-shortcut.com/en/writing-systems/%E6%96%87%E5%AD%97-chinese-cjk/cjk-characters-1/


