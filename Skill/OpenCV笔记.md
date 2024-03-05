### 使用pip安装OpenCV
`pip install opencv-python-headless`

RGB色彩空间(Red, Green, Blue)
HSV色彩空间(Hue, Saturation, Value)
HSI色彩空间(Hue, Saturation, Intensity)
HSL色彩空间(Hue, Saturation, Lightness)
HSB色彩空间(Hue, Saturation, Brightness)

### cv2.imread()
读取图像, 保存为numpy数组
(function) def imread(
    filename: str,
    flags: int = ...
) -> MatLike

| Flag                 | Function                |
| -------------------- | ----------------------- |
| cv2.IMREAD_COLOR     | 加载彩色图片            |
| cv2.IMREAD_GRAYSCALE | 加载灰度图片            |
| cv2.IMREAD_UNCHANGED | 加载原始图片(包括alpha) |


### cv2.cvtColor()
转换图像所在的色彩空间
(function) def cvtColor(
    src: MatLike,
    code: int,
    dst: MatLike | None = ...,
    dstCn: int = ...
) -> MatLike

| Code               | Function  |
| ------------------ | --------- |
| cv2.COLOR_BGR2GRAY | BGR转灰度 |
| cv2.COLOR_BGR2HSV  | BGR转HSV  |



### cv2.GaussianBlur



### cv2.Canny()
边缘检测算法
(function) def Canny(
    image: MatLike,
    threshold1: float,
    threshold2: float,
    edges: MatLike | None = ...,
    apertureSize: int = ...,
    L2gradient: bool = ...
) -> MatLike

| Para         | Function       |
| ------------ | -------------- |
| threshold1   | 阈值下限       |
| threshold2   | 阈值上限       |
| apertureSize | Sobel算子大小  |
| L2gradient   | 是否使用L2范数 |

### cv2.HoughLines()
霍夫变换的直线检测算法
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
) -> MatLike

| Para      | Function                 |
| --------- | ------------------------ |
| rho       | 线段以像素为单位的分辨率 |
| theta     | 线段以弧度为单位的分辨率 |
| threshold | 线段检测的最小投票数     |



### cv2.line()
绘制直线
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