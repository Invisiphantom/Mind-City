
<Python数据科学手册>

## 导入库
`import numpy as np`


## NumPy数据类型

| Type       | Desc                   |
| ---------- | ---------------------- |
| bool_      | 布尔型                 |
| int_       | 整型                   |
| intc       | C语言int类型           |
| intp       | 用于索引               |
| ---------  | ---------------------- |
| int8       | 8位整型                |
| int16      | 16位整型               |
| int32      | 32位整型               |
| int64      | 64位整型               |
| ---------  | ---------------------- |
| uint8      | 8位无符号整型          |
| uint16     | 16位无符号整型         |
| uint32     | 32位无符号整型         |
| uint64     | 64位无符号整型         |
| ---------  | ---------------------- |
| float_     | float64的简写          |
| float16    | 16位浮点型             |
| float32    | 32位浮点型             |
| float64    | 64位浮点型             |
| ---------  | --------------------   |
| complex_   | complex128的简写       |
| complex64  | 64位复数(2个32位浮点)  |
| complex128 | 128位复数(2个64位浮点) |







## NumPy函数

### np.array()
(function) def array(
    object: _ArrayType@array,
    dtype: None = ...,
    *,
    copy: bool | _CopyMode = ...,
    order: _OrderKACF = ...,
    subok: Literal[True],
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...
) -> _ArrayType@array: ...




### np.zeros()
(function) def zeros(
    shape: _ShapeLike,
    dtype: _DTypeLike[_SCT@zeros],
    order: _OrderCF = ...,
    *,
    like: _SupportsArrayFunc | None = ...
) -> NDArray[_SCT@zeros]

