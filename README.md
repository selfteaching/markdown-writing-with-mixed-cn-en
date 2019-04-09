# Markdown 简体中文与西文混排要点

**Version: 0.3**

李笑来 2019/04

---

这篇文档的标题中所使用的措辞是 “**要点**”，而非 “规范” —— 原因在于这些要点争议颇多。

然而，为了统一编辑，也为了读者阅读方便，《成长时代》（selfteaching.com）仓库中的所有文档，应尽量遵守以下要点。

以下的要点是针对 Markdown 写作而整理的。Markdown 是纯文本文件，它们最终都需要被转换成 HTML 文档或者其他文件格式，比如 PDF 等等 —— 即，为方便阅读而被渲染成的格式文档。

另外，本文不涉及 “文字风格建议”，只涉及**格式排版要求**。如，“表达数值变化程度时，不能使用 ‘降低了 n 倍’ 的说法，因为 ‘降低 1 倍’ 的意思是说，‘原来是 `100`，现在是 `0`’。应该用的表达方式是 “降低了百分之多少。” —— 这是文字风格（Writing Style）；而 “数值与单位之间、货币符号之间不能有空格。如 `75kg`、`$85`、`25%`。” —— 这是格式排版要求。

## 常用标点符号

中英混排的文本中，除了完整的英文句子或段落之外，应全部使用全角标点符号。

以下是常用中文全角标点符号：

|  名称  |         符号         |                               备注                                |
| ------ | -------------------- | ----------------------------------------------------------------- |
| 句号   | `。`                 |                                                                   |
| 逗号   | `，`                 |                                                                   |
| 顿号   | `、`                 |                                                                   |
| 问号   | `？`                 |                                                                   |
| 感叹号 | `！`                 |                                                                   |
| 引号   | ` “” ` &nbsp; ` ‘’ ` | 弯引号                                                            |
| 冒号   | `：`                 |                                                                   |
| 分号   | `；`                 |                                                                   |
| 省略号 | `……`                 | 共 6 个点，占据两个全角字符位置                                   |
| 破折号 | `——`                 | 共 2 个 `—`，占据两个全角字符位置                                 |
| 圆括号 | `（）`               |                                                                   |
| 书名号 | `《》`               |                                                                   |
| 分隔号 | `・`                 | [Katakana Middle Dot](<https://en.wikipedia.org/wiki/Interpunct>) |

**注意**

1. 分隔号统一使用占据一个全角位置的 [Katakana Middle Dot](<https://en.wikipedia.org/wiki/Interpunct>)，`&#12539;`，即，`・`；而非键盘上可以直接打出的 `&sdot;`，`・` —— 这个分隔号是半角符号。
2. 中英混排的文字中，单个英文单词需要用引号（单引号、双引号）括起来的时候，统一使用全角引号。英文句子中出现的引号，统一使用半角引号（单引号、双引号）。
3. 句子末尾用括号加注时，句号应该在括号之外。如：`……（参见第三章）。`
4. 句子内部的并列词汇，使用顿号（`、`）分割，即便并列词为英文，也要如此。如：`经常使用的等宽字体包括 Menlo、Monaco、Courier New、monospace 等等`。而纯英文句子中的并列词，则要用半角逗号（`,`）分割。

## 空格

中英混排的文本中使用的空格是半角符号空格：` ` —— 这也更符合大多数中文输入法的习惯。

1. 中文与英文之间、中文与数字之间，都要有一个半角空格；如：`这是 1 个 variable 的例子`
2. 英文字符、数字字符，与全角标点符号之间，不应该有空格；如：`这是一个 variable，这是数字 100。`；再比如：`变量 a 的值是：8；a 的值大于变量 b。`
3. 全角引号（单引号、双引号）之外要有空格；如：`所谓的 “过早引用” 就是这样令人迷惑的。`
4. 中英文并存的句子里，英文单词若是需要用括号括起，必须使用全角引号；如：`这就是所谓的 “过早引用”（Forward References）` —— 注意，引号和括号之间没有空格。
5. 破折号（`——`）前后要各有一个半角空格。
6. 省略号（`……`）后要各有一个半角空格。如：`他们总是这么说…… 可实际上呢？`
7. 引号、破折号、省略号之外的全角标点符号前后不能有空格。如，`…… 就是这个元素（“decorators”）—— 即，所谓的装饰器。` 注意，`”`、`）`、`——` 之间都没有空格。
8. 行内代码标示（Inline code）前后要有空格；如：```表达式 `a += 1` 的意思是说……```

## 倾斜

1. Markdown 中的倾斜标示，可用星号或者下划线，如，`*强调*` 或者 `_强调_`。然而，中文字符使用倾斜显示的话，在排版上会显得非常难看。
2. 在渲染（Render）时，Markdown 中的 `*强调*` 或者 `_强调_` 会被同样渲染成 `<em>强调</em>`。而 `<em>` 需由 css 设定为 `font-style: regular;`，而字体颜色则可以设置为不同的颜色以示强调。
3. 而在必须为英文单词设置强调（倾斜样式）之时，要在 Markdown 中使用 HTML 标签：`<i>`，如：`<i>emphasis</i>`。如有必要，在 css 中再另外设置字体颜色。

## 标题

1. 标题一概使用 `#` 符号标示。

2. 由于在 GFM（Github Flavored Markdown）中，`/#[0-9]+/` 被自动渲染为 issue 的链接，所以，在标示标题的时候，`#` 符号后应有且只有一个空格，例如：

   ```markdown
    # 一级标题
    ## 二级标题
    ### 三级标题
   ```

3. 一个 Markdown 文件中有且只有一个一级标题。

4. 一个 Markdown 文件中最多使用到三级标题。如果层级过多，说明你可能需要将文本切分到多个文件。

## 段落

1. 段落不使用行首缩进。
2. 段落之间用一个空行隔开。

## 数字

1. 阿拉伯数字一律使用半角字符。
2. 使用半角逗号标记千分位；4 ～ 6 位的的数值，千分位的逗号是可选的，但，7 位或者 7 位以上的数值，必须有千分位的逗号。如：`2000`，`21,000,000`。针对多位小数可从小数点后从左至右添加千分位的逗号，如，`3.141,59`。
3. 表示数值范围，使用 ` ~ `（`~`前后各有一个半角空格字符），如：`25 ～ 29`。
4. 数值带有单位或者百分号的时候，前后两个数值都要有单位或者百分号，如：`25% ~ 29%`、` 72kg ~ 75kg`；不能是：`25 ~ 29%`、` 72 ~ 75kg`
5. 数值与单位之间、货币符号之间不能有空格。如 `75kg`、`$85`、`25%`。

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

1. Github 的 Markdown 教程：[Github: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
2. 微软的写作风格指导：[Microsoft Writing Style Guide](https://docs.microsoft.com/en-us/contribute/how-to-write-use-markdown)
3. Markdown 格式检查工具：[MarkdownLint](https://github.com/DavidAnson/markdownlint) —— 虽然它本身是 lint 工具，但它的文档中包含很多 Markdown 格式上的优化要求。

## 推荐使用的 Markdown 编辑器

- [VSCode](<https://code.visualstudio.com/>) + [Docs Authoring Pack](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-authoring-pack)
- [Typora](https://typora.io/)

## 更多参考链接

> * https://golem.ph.utexas.edu/~distler/maruku/markdown_syntax.html
> * http://www.pinyin.info/tools/converter/chars2uninumbers.html
> * https://www.w3.org/html/ig/zh/wiki/Css4-text
> * https://www.toptal.com/designers/htmlarrows/
> * https://www.key-shortcut.com/en/writing-systems/%E6%96%87%E5%AD%97-chinese-cjk/cjk-characters-1/
