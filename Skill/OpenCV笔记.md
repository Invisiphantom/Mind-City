
[OpenCV中文教程](https://opencv-python-tutorials.readthedocs.io/)
[OpenCV-4.7.0说明文档](https://blog.csdn.net/qq_29659921/category_12251993_2)


## 使用pip安装OpenCV
```bash
sudo apt install libgtk2.0-dev pkg-config
pip uninstall opencv-python-headless
pip uninstall opencv-python
pip install opencv-python
```

RGB色彩空间(Red, Green, Blue)
HSV色彩空间(Hue, Saturation, Value)
HSI色彩空间(Hue, Saturation, Intensity)
HSL色彩空间(Hue, Saturation, Lightness)
HSB色彩空间(Hue, Saturation, Brightness)

<br>

## OpenCV图片读取与写入

### cv2.imread() 读图
(function) def imread(
    filename: str,
    flags: int = ...
) -> MatLike

| Flag                 | Function                |
| -------------------- | ----------------------- |
| cv2.IMREAD_COLOR     | 加载彩色图片            |
| cv2.IMREAD_GRAYSCALE | 加载灰度图片            |
| cv2.IMREAD_UNCHANGED | 加载原始图片(包括alpha) |

### cv2.imwrite() 写图
(function) def imwrite(
    filename: str,
    img: MatLike,
    params: Sequence[int] = ...
) -> bool

<br>

## OpenCV绘图

### cv2.line() 画线
(function) def line(
    img: MatLike,
    pt1: Point,
    pt2: Point,
    color: Scalar,
    thickness: int = ...,
    lineType: int = ...,
    shift: int = ...
) -> MatLike

| Para      | Function |
| --------- | -------- |
| pt1       | 起点坐标 |
| pt2       | 终点坐标 |
| color     | 颜色     |
| thickness | 线宽     |
| lineType  | 线型     |
| shift     | 偏移     |

| lineType    | Func   |
| ----------- | ------ |
| cv2.FILLED  | 填充   |
| cv2.LINE_4  | 4邻接  |
| cv2.LINE_8  | 8邻接  |
| cv2.LINE_AA | 抗锯齿 |



### cv2.rectangle() 画矩形
(function) def rectangle(
    img: MatLike,
    pt1: Point,
    pt2: Point,
    color: Scalar,
    thickness: int = ...,
    lineType: int = ...,
    shift: int = ...
) -> MatLike


### cv2.circle() 画圆
(function) def circle(
    img: MatLike,
    center: Point,
    radius: int,
    color: Scalar,
    thickness: int = ...,
    lineType: int = ...,
    shift: int = ...
) -> MatLike

### cv2.polylines() 画多边形
(function) def polylines(
    img: MatLike,
    pts: Sequence[MatLike],
    isClosed: bool,
    color: Scalar,
    thickness: int = ...,
    lineType: int = ...,
    shift: int = ...
) -> MatLike

### cv2.putText() 画文字
(function) def putText(
    img: MatLike,
    text: str,
    org: Point,
    fontFace: int,
    fontScale: float,
    color: Scalar,
    thickness: int = ...,
    lineType: int = ...,
    bottomLeftOrigin: bool = ...
) -> MatLike

<br>

## OpenCV色彩处理

### cv2.cvtColor() 色彩空间转换
(function) def cvtColor(
    src: MatLike,
    code: int,
    dst: MatLike | None = ...,
    dstCn: int = ...
) -> MatLike

| Code               | Function  |
| ------------------ | --------- |
| cv2.COLOR_BGR2GRAY | BGR转灰度 |
| cv2.COLOR_BGR2RGB  | BGR转RGB  |
| cv2.COLOR_BGR2HSV  | BGR转HSV  |


### cv2.inRange() 颜色区间提取
(function) def inRange(
    src: MatLike,
    lowerb: MatLike,
    upperb: MatLike,
    dst: MatLike | None = ...
) -> MatLike


### cv2.bitwise_and() 掩码按位与
(function) def bitwise_and(
    src1: MatLike,
    src2: MatLike,
    dst: MatLike | None = ...,
    mask: MatLike | None = ...
) -> MatLike

<br>



## OpenCV图像几何变换

### cv2.resize() 缩放
(function) def resize(
    src: MatLike,
    dsize: Size | None,
    dst: MatLike | None = ...,
    fx: float = ...,
    fy: float = ...,
    interpolation: int = ...
) -> MatLike: ...

| Para          | Func         |
| ------------- | ------------ |
| src           | 原图像       |
| dsize         | 输出图像大小 |
| dst           | 输出图像     |
| fx            | 水平缩放     |
| fy            | 垂直缩放     |
| interpolation | 插值方法     |


| Interpolation     | Func     |
| ----------------- | -------- |
| cv2.INTER_NEAREST | 最近邻   |
| cv2.INTER_LINEAR  | 双线性   |
| cv2.INTER_CUBIC   | 双三次   |
| cv2.INTER_AREA    | 区域像素 |


### cv2.getRotationMatrix2D() 获取旋转矩阵
(function) def getRotationMatrix2D(
    center: Point2f,
    angle: float,
    scale: float
) -> MatLike

### cv2.getAffineTransform() 获取仿射矩阵
(function) def getAffineTransform(
    src: MatLike,
    dst: MatLike
) -> MatLike: ...

### cv2.warpAffine() 仿射变换
(function) def warpAffine(
    src: MatLike,
    M: MatLike,
    dsize: Size,
    dst: MatLike | None = ...,
    flags: int = ...,
    borderMode: int = ...,
    borderValue: Scalar = ...
) -> MatLike: ...


### cv2.getPerspectiveTransform() 获取透视矩阵
(function) def getPerspectiveTransform(
    src: MatLike,
    dst: MatLike,
    solveMethod: int = ...
) -> MatLike: ...


### cv2.warpPerspective() 透视变换
(function)
def warpPerspective(
    src: MatLike,
    M: MatLike,
    dsize: Size,
    dst: MatLike | None = ...,
    flags: int = ...,
    borderMode: int = ...,
    borderValue: Scalar = ...
) -> MatLike: ...

<br>

## OpenCV图像阈值处理

### cv2.threshold() 阈值处理
(function)
def threshold(
    src: MatLike,
    thresh: float,
    maxval: float,
    type: int,
    dst: MatLike | None = ...
) -> tuple[float, MatLike]: ...

| Para   | Func     |
| ------ | -------- |
| src    | 输入图像 |
| thresh | 阈值     |
| maxval | 极大赋值 |
| type   | 阈值类型 |
| dst    | 输出图像 |


| type                  | Desc                          |
| --------------------- | ----------------------------- |
| cv2.THRESH_BINARY     | 大于阈值赋值maxval, 否则赋值0 |
| cv2.THRESH_BINARY_INV | 大于阈值赋值0, 否则赋值maxval |
| cv2.THRESH_TRUNC      | 大于阈值赋值阈值, 否则不变    |
| cv2.THRESH_TOZERO     | 大于阈值不变, 否则赋值0       |
| cv2.THRESH_TOZERO_INV | 大于阈值赋值0, 否则不变       |
| cv2.THRESH_OTSU       | Otsu自动阈值                  |

### cv2.adaptiveThreshold() 自适应阈值处理
(function) def adaptiveThreshold(
    src: MatLike,
    maxValue: float,
    adaptiveMethod: int,
    thresholdType: int,
    blockSize: int,
    C: float,
    dst: MatLike | None = ...
) -> MatLike: ...

| Para           | Func       |
| -------------- | ---------- |
| src            | 输入图像   |
| maxValue       | 极大赋值   |
| adaptiveMethod | 自适应方法 |
| thresholdType  | 阈值类型   |
| blockSize      | 邻域大小   |
| C              | 常数C      |
| dst            | 输出图像   |

| adaptiveMethod                 | Desc         |
| ------------------------------ | ------------ |
| cv2.ADAPTIVE_THRESH_MEAN_C     | 邻域均值     |
| cv2.ADAPTIVE_THRESH_GAUSSIAN_C | 高斯加权均值 |

<br>

## OpenCV图像滤波

### cv2.filter2D() 2D卷积
(function) def filter2D(
    src: MatLike,
    ddepth: int,
    kernel: MatLike,
    dst: MatLike | None = ...,
    anchor: Point = ...,
    delta: float = ...,
    borderType: int = ...
) -> MatLike: ...

### cv2.blur() 均值滤波
(function) def blur(
    src: MatLike,
    ksize: Size,
    dst: MatLike | None = ...,
    anchor: Point = ...,
    borderType: int = ...
) -> MatLike: ...

### cv2.GaussianBlur() 高斯滤波
(function) def GaussianBlur(
    src: MatLike,
    ksize: Size,
    sigmaX: float,
    dst: MatLike | None = ...,
    sigmaY: float = ...,
    borderType: int = ...
) -> MatLike: ...

### cv2.medianBlur() 中值滤波
(function) def medianBlur(
    src: MatLike,
    ksize: int,
    dst: MatLike | None = ...
) -> MatLike: ...

### cv2.bilateralFilter() 双边滤波
(function) def bilateralFilter(
    src: MatLike,
    d: int,
    sigmaColor: float,
    sigmaSpace: float,
    dst: MatLike | None = ...,
    borderType: int = ...
) -> MatLike: ...

<br>

## OpenCV图像形态变换

### cv2.erode() 腐蚀
(function) def erode(
    src: MatLike,
    kernel: MatLike,
    dst: MatLike | None = ...,
    anchor: Point = ...,
    iterations: int = ...,
    borderType: int = ...,
    borderValue: Scalar = ...
) -> MatLike: ...

### cv2.dilate() 膨胀
(function) def dilate(
    src: MatLike,
    kernel: MatLike,
    dst: MatLike | None = ...,
    anchor: Point = ...,
    iterations: int = ...,
    borderType: int = ...,
    borderValue: Scalar = ...
) -> MatLike: ...

### cv2.morphologyEx() 形态学变换
(function) def morphologyEx(
    src: MatLike,
    op: int,
    kernel: MatLike,
    dst: MatLike | None = ...,
    anchor: Point = ...,
    iterations: int = ...,
    borderType: int = ...,
    borderValue: Scalar = ...
) -> MatLike: ...

| op                 | Desc                   |
| ------------------ | ---------------------- |
| cv2.MORPH_OPEN     | 开运算(膨胀后腐蚀)     |
| cv2.MORPH_CLOSE    | 闭运算(腐蚀后膨胀)     |
| cv2.MORPH_GRADIENT | 形态梯度(膨胀减腐蚀)   |
| cv2.MORPH_TOPHAT   | 顶帽运算(原图减开运算) |
| cv2.MORPH_BLACKHAT | 黑帽运算(闭运算减原图) |


### cv2.getStructuringElement() 获取卷积核
(function) def getStructuringElement(
    shape: int,
    ksize: Size,
    anchor: Point = ...
) -> MatLike


## OpenCV图像梯度处理

### cv2.Sobel() Sobel算子
(function) def Sobel(
    src: MatLike,
    ddepth: int,
    dx: int,
    dy: int,
    dst: MatLike | None = ...,
    ksize: int = ...,
    scale: float = ...,
    delta: float = ...,
    borderType: int = ...
) -> MatLike: ...

### cv2.Scharr() Scharr算子
(function) def Scharr(
    src: MatLike,
    ddepth: int,
    dx: int,
    dy: int,
    dst: MatLike | None = ...,
    scale: float = ...,
    delta: float = ...,
    borderType: int = ...
) -> MatLike: ...

### cv2.Laplacian() Laplacian算子
(function) def Laplacian(
    src: MatLike,
    ddepth: int,
    dst: MatLike | None = ...,
    ksize: int = ...,
    scale: float = ...,
    delta: float = ...,
    borderType: int = ...
) -> MatLike: ...

<br>

## OpenCV边缘检测

(function) def Canny(
    image: MatLike,
    threshold1: float,
    threshold2: float,
    edges: MatLike | None = ...,
    apertureSize: int = ...,
    L2gradient: bool = ...
) -> MatLike: ...

1. 高斯滤波
2. Sobel梯度
3. 非极大值抑制
4. 滞后阈值

<br>

## OpenCV轮廓处理

### cv2.findContours() 查找轮廓
(function) def findContours(
    image: MatLike,
    mode: int,
    method: int,
    contours: Sequence[MatLike] | None = ...,
    hierarchy: MatLike | None = ...,
    offset: Point = ...
) -> tuple[Sequence[MatLike], MatLike]: ...

### cv2.drawContours() 绘制轮廓
(function) def drawContours(
    image: MatLike,
    contours: Sequence[MatLike],
    contourIdx: int,
    color: Scalar,
    thickness: int = ...,
    lineType: int = ...,
    hierarchy: MatLike | None = ...,
    maxLevel: int = ...,
    offset: Point = ...
) -> MatLike: ...

<br>

## OpenCV霍夫变换

### cv2.HoughLines() 直线检测
(function) def HoughLines(
    image: MatLike,
    rho: float,
    theta: float,
    threshold: int,
    lines: MatLike | None = ...,
    srn: float = ...,
    stn: float = ...,
    min_theta: float = ...,
    max_theta: float = ...
) -> MatLike: ...


### cv2.HoughLinesP() 概率直线检测
(function) def HoughLinesP(
    image: MatLike,
    rho: float,
    theta: float,
    threshold: int,
    lines: MatLike | None = ...,
    minLineLength: float = ...,
    maxLineGap: float = ...
) -> MatLike: ...


### cv2.HoughCircles() 圆检测
(function) def HoughCircles(
    image: MatLike,
    method: int,
    dp: float,
    minDist: float,
    circles: MatLike | None = ...,
    param1: float = ...,
    param2: float = ...,
    minRadius: int = ...,
    maxRadius: int = ...
) -> MatLike: ...