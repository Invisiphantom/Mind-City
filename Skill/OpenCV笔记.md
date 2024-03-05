### 使用pip安装OpenCV
`pip install opencv-python-headless`


### cv2.imread()
(function) def imread(
    filename: str,
    flags: int = ...
) -> MatLike


### cv2.cvtColor()
(function) def cvtColor(
    src: MatLike,
    code: int,
    dst: MatLike | None = ...,
    dstCn: int = ...
) -> MatLike


### cv2.Canny()
(function) def Canny(
    image: MatLike,
    threshold1: float,
    threshold2: float,
    edges: MatLike | None = ...,
    apertureSize: int = ...,
    L2gradient: bool = ...
) -> MatLike


### cv2.HoughLines()
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


### cv2.line()
(function) def line(
    img: MatLike,
    pt1: Point,
    pt2: Point,
    color: Scalar,
    thickness: int = ...,
    lineType: int = ...,
    shift: int = ...
) -> MatLike