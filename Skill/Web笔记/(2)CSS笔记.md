https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference


```css
a {}            /* 标签选择器 */
a[href=""] {}   /* 属性选择器 */
a:hover {}      /* 伪类选择器 */
a::after {}     /* 伪元素选择器 */
div > p {}      /* 子元素选择器 */

.box {}         /* class选择器 */
#unique {}      /* ID选择器 */
```


| 属性    | 描述   |
| ------- | ------ |
| width   | 宽度   |
| height  | 高度   |
| margin  | 外边距 |
| border  | 边框   |
| padding | 内边距 |

`margin: 10px;`: 上下左右都是10px
`margin: 10px 20px;`: 上下是10px，左右是20px
`margin: 10px 20px 30px;`: 上是10px，左右是20px，下是30px
`margin: 10px 20px 30px 40px;`: 上是10px，右是20px，下是30px，左是40px
`box-shadow: 10px 5px 8px skyblue;`: 水平偏移10px，垂直偏移5px，模糊半径8px，阴影颜色skyblue



| 字体属性     | 可选参数                           | 描述     |
| ------------ | ---------------------------------- | -------- |
| font         |                                    | 字体     |
| font-style   | normal italic oblique              | 字体样式 |
| font-variant | normal small-caps                  | 字体变体 |
| font-weight  | normal bold bolder lighter 100-900 | 字体粗细 |
| font-size    | 10px 1em 100%                      | 字体大小 |
| line-height  | normal 1.5 1em 100%                | 字体行高 |
| font-family  | sans-serif                         | 字体系列 |


| 边框属性      | 描述     |
| ------------- | -------- |
| border        | 边框     |
| border-width  | 边框宽度 |
| border-style  | 边框样式 |
| border-color  | 边框颜色 |
| border-radius | 边框圆角 |

| 背景属性         | 描述     |
| ---------------- | -------- |
| background       | 背景     |
| background-color | 背景颜色 |