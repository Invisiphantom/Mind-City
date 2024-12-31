## OpenGL资料

OpenGL教程: [LearnOpenGL](https://learnopengl.com/Getting-started/OpenGL)


[图解弄懂gl，glu，glut，glew，glfw之间关系-CSDN](https://blog.csdn.net/wangleizhenshuai/article/details/122960349)
[上帝视角看GPU：图形流水线基础_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1P44y1V7bu/?spm_id_from=333.1007.top_right_bar_window_history.content.click)
[最好的OpenGL教程之一_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1MJ411u7Bc/)
[Cherno OpenGL教程 | Fl0w3r (yousazoe.top)](https://www.yousazoe.top/archives/cbd8aac2.html)
[LearnOpenGL CN (learnopengl-cn.github.io)](https://learnopengl-cn.github.io/intro/)


[Lecture 01 Overview of Computer Graphics_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1X7411F744?p=1&vd_source=c03ebf3c70dde0f2b5c39bf1f5ee258e)
[GAMES101: 现代计算机图形学入门 (ucsb.edu)](https://sites.cs.ucsb.edu/~lingqi/teaching/games101.html)

[OpenGL ES 2.0 知识串讲（1）――OpenGL ES 2.0 概括 (geekfaner.com)](http://geekfaner.com/shineengine/blog2_OpenGLESv2_1.html)
[OpenGL矩阵变换的数学推导-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1389550)

[MIT6.837-2012 | Assignments](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/pages/assignments/)
[Curves-and-Surfaces | Solution](https://github.com/andrewmo2014/Curves-and-Surfaces)
[Curves-and-Surfaces | Solution](https://github.com/jul1u5/6.837)
[Curves-and-Surfaces | Solution](https://youtu.be/gm6CuvDbEDM)

| 图形库  | 介绍                                                 |
| ------- | ---------------------------------------------------- |
| OpenGL  | Open Graphics Library, 开放图形库                    |
| GLFW    | OpenGL FrameWork, OpenGL创建窗口和处理用户输入       |
| GLAD    | GL Loader Generator, OpenGL动态链接库加载器          |
| GLSL    | OpenGL Shading Language, OpenGL着色器语言            |
| GLM     | OpenGL Mathematics, OpenGL数学库                     |
| GLEW    | OpenGL Extension Wrangler Library, OpenGL扩展库      |
| SOIL2   | Simple OpenGL Image Library, 简单OpenGL图像库        |
| ------  | --------------------------------------------------   |
| GLUI    | OpenGL User Interface, OpenGL用户界面                |
| GLee    | OpenGL Easy Extension, OpenGL简单扩展                |
| GLUT    | OpenGL Utility Toolkit, OpenGL实用工具包             |
| SFML    | Simple and Fast Multimedia Library, 简单快速多媒体库 |
| SDL2    | Simple DirectMedia Layer, 简单直接媒体层             |
| DirectX | 微软图形库                                           |
| Metal   | 苹果图形库                                           |


## OpenGL配置

https://glad.dav1d.de/
选择最新版本gl, 勾选"Local Files", 然后生成并下载glad.zip
https://premake.github.io/download/
https://github.com/SpartanJ/SOIL2
```bash
sudo apt install build-essential g++ gdb cmake
sudo apt install libgl-dev libglfw3-dev libglm-dev libsoil-dev libglew-dev libsdl2-dev
sudo apt install glslang-tools

wget https://glad.dav1d.de/generated/tmpk57okme6glad/glad.zip 
unzip glad.zip -d glad
sudo mv glad /usr/local/include/

wget https://github.com/premake/premake-core/releases/download/v5.0.0-beta2/premake-5.0.0-beta2-linux.tar.gz
sudo tar -xvf premake-5.0.0-beta2-linux.tar.gz -C /usr/local/bin/

git clone https://github.com/SpartanJ/SOIL2.git
cd SOIL2 && premake5 gmake2
cd make/linux/ && make -j4
cd ../..
sudo mv src/SOIL2/ /usr/local/include
cd lib/linux/
sudo mv libsoil2-debug.* /usr/local/lib/

glxinfo | grep "OpenGL version"
```


VSCode插件
Shader languages support for VS Code
glsl-snippets
glsl-canvas
GLSL Lint

修改`.vscode/tasks.json`文件, 添加头文件和链接操作
```json
    "args": [
        "-fdiagnostics-color=always",
        "-g",
        "${file}",
        "/usr/include/glad/glad.c",
        "-o",
        "${workspaceFolder}/bin/${fileBasenameNoExtension}",
        "-lGL",
        "-lglfw",
    ],
```

修改`.vscode/settings.json`文件, 添加编译和运行操作
```json
"code-runner.executorMap": {
    "cpp": "cd $dir && g++ $fileName /usr/include/glad/glad.c -o $workspaceRoot/bin/$fileNameWithoutExt -lGL -lglfw && $workspaceRoot/bin/$fileNameWithoutExt",
},
```




## OpenGL管线



| glad Function                        | Desc           |
| ------------------------------------ | -------------- |
| `int gladLoadGLLoader(GLADloadproc)` | 加载OpenGL函数 |


| glfw Function                                                              | Desc                 |
| -------------------------------------------------------------------------- | -------------------- |
| `int glfwInit()`                                                           | 初始化glfw库         |
| `void glfwWindowHint(int hint, int value)`                                 | 配置glfw参数         |
| `void glfwTerminate()`                                                     | 终止glfw库           |
| ------------------------------------------------------------------------   | -----------------    |
| `GLFWwindow *glfwCreateWindow(int width, int height, const char *title)`   | 创建窗口             |
| `void glfwMakeContextCurrent(GLFWwindow *window)`                          | 指定窗口上下文       |
| `void glfwGetFramebufferSize(GLFWwindow *window, int *width, int *height)` | 获取窗口帧缓冲区大小 |
| `void glfwDestroyWindow(GLFWwindow *window)`                               | 销毁窗口             |
| ------------------------------------------------------------------------   | -----------------    |
| `GLFWglproc glfwGetProcAddress(const char *procname)`                      | 获取OpenGL函数指针   |
| ------------------------------------------------------------------------   | -----------------    |
| `void glfwSwapInterval(int interval)`                                      | 设置垂直同步         |
| `void glfwSwapBuffers(GLFWwindow *window)`                                 | 交换渲染缓冲区       |
| `void glfwPollEvents()`                                                    | 处理窗口事件         |



VBO: 向GPU传递顶点数据
VAO: 向GPU解释顶点数据

1. 编译program
2. 创建缓冲区并绑定
3. 构造PVMR矩阵
4. 绘制图元



| gl Function                                                                                         | Desc                           |
| --------------------------------------------------------------------------------------------------- | ------------------------------ |
| `GLenum glGetError(void)`                                                                           | 获取错误代码                   |
| `void glViewport(GLint x, GLint y, GLsizei width, GLsizei height)`                                  | 设置视窗位置与大小             |
| `void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)`                        | 设置清空颜色缓冲区             |
| `void glClear(GLbitfield mask)`                                                                     | 清空缓冲区                     |
| --------------------------------------------------------------------------------------------------- | ---------------------          |
| `GLuint glCreateShader(GLenum shaderType);`                                                         | 创建着色器                     |
| `void glShaderSource(GLuint shader, GLsizei count, GLchar **string, const GLint *length=NULL)`      | 设置着色器源码                 |
| `void glCompileShader(GLuint shader)`                                                               | 编译着色器源码                 |
| `void glGetShaderiv(GLuint shader, GLenum pname, GLint *params)`                                    | 查询着色器状态                 |
| `void glGetShaderInfoLog(GLuint shader, GLsizei maxLength, GLsizei *length, GLchar *infoLog)`       | 获取着色器错误日志             |
| `void glDeleteShader(GLuint shader)`                                                                | 删除着色器                     |
| --------------------------------------------------------------------------------------------------- | ---------------------          |
| `GLuint glCreateProgram()`                                                                          | 创建程序                       |
| `void glAttachShader(GLuint program, GLuint shader)`                                                | 绑定程序与着色器               |
| `void glLinkProgram(GLuint program)`                                                                | 链接生成可执行程序             |
| `void glGetProgramiv(GLuint program, GLenum pname, GLint *params)`                                  | 查询程序状态                   |
| `void glGetProgramInfoLog(GLuint program, GLsizei maxLength, GLsizei *length, GLchar *infoLog)`     | 获取程序错误日志               |
| `void glUseProgram(GLuint program)`                                                                 | 激活程序                       |
| `void glDeleteProgram(GLuint program)`                                                              | 删除程序                       |
| --------------------------------------------------------------------------------------------------- | ---------------------          |
| `void glGenVertexArrays(GLsizei n, GLuint *arrays)`                                                 | 创建VAO                        |
| `void glBindVertexArray(GLuint array)`                                                              | 激活VAO                        |
| `void glGenBuffers(GLsizei n, GLuint *buffers)`                                                     | 创建VBO                        |
| `void glBindBuffer(GLenum target, GLuint buffer)`                                                   | 激活VBO                        |
| `void glBufferData(GLenum target,	GLsizeiptr size, const void* data, GLenum usage);`                | 填充VBO数据                    |
| --------------------------------------------------------------------------------------------------- | ---------------------          |
| `GLint glGetUniformLocation(GLuint program, const GLchar *name)`                                    | 获取uniform变量位置            |
| `void glUniform1f(GLint location, GLfloat v0)`                                                      | 设置uniform变量值              |
| `void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)` | 设置uniform矩阵值              |
| `void glVertexAttribPointer(GLuint index, GLint size, GLenum type,                                  | 将缓冲区[stride*i+offset:size] |
| GLboolean normalized, GLsizei stride, const void *offset)`                                          | -关联到index属性               |
| `glEnableVertexAttribArray(GLuint index)`                                                           | 启用index属性                  |
| `glEnable(GL_DEPTH_TEST)  glDepthFunc(GL_LEQUAL)`                                                   | 设置深度测试                   |
| `void glDrawArrays(GLenum mode, GLint first, GLsizei count)`                                        | 绘制图元                       |
| `glDrawArraysInstanced(GLenum mode, GLint first, GLsizei count, GLsizei instancecount)`             | 绘制实例化图元                 |



| GLenum mode           | Description |
| --------------------- | ----------- |
| GL_TRIANGLES          | 三角形      |
| GL_TRIANGLE_STRIP     | 三角形带    |
| GL_TRIANGLE_FAN       | 三角形扇    |
| GL_TRIANGLE_ADJACENCY | 三角形邻接  |
| GL_LINES              | 线段        |
| GL_LINE_STRIP         | 线段带      |
| GL_LINE_LOOP          | 线段环      |
| GL_LINES_ADJACENCY    | 线段邻接    |
| GL_POINTS             | 点          |
| GL_PATCHES            | 曲面        |




| GLenum shaderType           | 文件名 | 着色器类型         |
| --------------------------- | ------ | ------------------ |
| `GL_VERTEX_SHADER`          | .vert  | 顶点着色器         |
| `GL_TESS_CONTROL_SHADER`    | .tesc  | 曲面细分控制着色器 |
| `GL_TESS_EVALUATION_SHADER` | .tese  | 曲面细分评估着色器 |
| `GL_GEOMETRY_SHADER`        | .geom  | 几何着色器         |
| `GL_FRAGMENT_SHADER`        | .frag  | 片段着色器         |
| `GL_COMPUTE_SHADER`         | .comp  | 计算着色器         |



## glm语法

| glm Function                     | Desc         |
| -------------------------------- | ------------ |
| value_ptr                        | 数据指针     |
| vec3                             | 三维向量     |
| normalize(vec3)                  | 单位向量     |
| dot(vec3,vec3)                   | 点乘         |
| cross(vec3,vec3)                 | 叉乘         |
| mat4                             | 四维矩阵     |
| transpose(mat4)                  | 矩阵转置     |
| translate(x,y,z)                 | 平移矩阵     |
| scale(x,y,z)                     | 缩放矩阵     |
| rotate(mat4,θ,x,y,z)             | 旋转矩阵     |
| perspective(fov,aspect,near,far) | 透视投影矩阵 |
| lookAt(eye,center,up)            | 观察矩阵     |

GLSL::mat4以列为单位读入值, 前4个参数为第1列


## GLSL语法

### 基本数据类型

| Type                   | Desc     |
| ---------------------- | -------- |
| void                   | 空类型   |
| bool/bvec2/bvec3/bvec4 | 布尔类型 |
| int/ivec2/ivec3/ivec4  | 整型     |
| float/vec2/vec3/vec4   | 浮点型   |
| mat2/mat3/mat4         | 矩阵     |


### Vertex Shader

| Name        | Type | Desc       |
| ----------- | ---- | ---------- |
| gl_Color    | vec4 | 顶点主颜色 |
| gl_Position | vec4 | 顶点位置   |
| gl_VertesID | int  | 顶点ID     |


## glfw语法

初始化并配置参数
`int glfwInit()`
`void glfwWindowHint(int hint, int value)`
```cpp
glfwInit(); // 初始化glfw库
// OpenGL版本号：4.1 (Compatibility Profile) Mesa 23.2.1-1ubuntu3.1~22.04.2
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4); // 指定主版本号
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1); // 指定次版本号
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE); // 启用核心模式
```


创建窗口
`GLFWwindow *glfwCreateWindow(int width, int height, const char *title, GLFWmonitor *monitor, GLFWwindow *share)`
指定该窗口为当前上下文
`void glfwMakeContextCurrent(GLFWwindow *window)` 
设置帧缓冲区大小发生变化时的回调函数
`GLFWframebuffersizefun glfwSetFramebufferSizeCallback(GLFWwindow *window, GLFWframebuffersizefun callback)`
```cpp
const unsigned int SCR_WIDTH = 800;  // 窗口宽度
const unsigned int SCR_HEIGHT = 600; // 窗口高度
GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL", NULL, NULL);
if (window == NULL)
{
    std::cout << "Failed to create GLFW window" << std::endl;
    glfwTerminate();
    return -1;
}
glfwMakeContextCurrent(window);
glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

void framebuffer_size_callback(GLFWwindow* window, int width, int height ){
    glViewport(0, 0, width, height);
}
```


获取OpenGL函数指针
`GLFWglproc glfwGetProcAddress(const char *procname)`
使用OpenGL函数来初始化GLAD
`int gladLoadGLLoader(GLADloadproc)`
```cpp
if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
{
    std::cout << "Failed to initialize GLAD" << std::endl;
    return -1;
}    
```


检测窗口是否关闭
`int glfwWindowShouldClose(GLFWwindow *window)`

设置清空颜色缓冲区
`void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)`
清空缓冲区
`void glClear(GLbitfield mask);`
GL_COLOR_BUFFER_BIT: 颜色缓冲区
GL_DEPTH_BUFFER_BIT: 深度缓冲区
GL_STENCIL_BUFFER_BIT: 模板缓冲区

交换窗口缓冲区来渲染图像
`void glfwSwapBuffers(GLFWwindow *window)`
处理窗口事件
`void glfwPollEvents()`
终止GLFW库运行
`void glfwTerminate()`
```cpp
while (!glfwWindowShouldClose(window))
{
    // input
    processInput(window);

    // render
    glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
    glfwSwapBuffers(window);
    glfwPollEvents();
}

glfwTerminate();
return 0;
```


获取窗口关键字
`int glfwGetKey(GLFWwindow *window, int key)`
设置窗口是否关闭
`void glfwSetWindowShouldClose(GLFWwindow *window, int value)`
```cpp
void processInput(GLFWwindow *window)
{
    if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}
```


1. 初始化GLFW
2. 配置GLFW
3. 创建窗口对象
4. 指定窗口上下文
5. 加载OpenGL函数指针
6. 渲染循环
7. 释放资源

```vert
#version 410
void main(void)
{
    if(gl_VertexID==0)gl_Position=vec4(.25,-.25,0.,1.);
    else if(gl_VertexID==1)gl_Position=vec4(-.25,-.25,0.,1.);
    else gl_Position=vec4(.25,.25,0.,1.);
}
```

```frag
#version 410
out vec4 color;
void main(void)
{
    color=vec4(.1804,.7059,.4431,1.);
}
```

```cpp
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <string>
#include <fstream>

using namespace std;

void u_framebuffer_size_callback(GLFWwindow *window, int width, int height)
{
    glViewport(0, 0, width, height);
}

string u_readShaderCode(const char *filePath)
{
    string sourceCode;
    ifstream fileStream(filePath, ios::in);
    while (!fileStream.eof())
    {
        string line = "";
        getline(fileStream, line);
        sourceCode.append(line + "\n");
    }
    fileStream.close();
    return sourceCode;
}

GLuint u_createShaderProgram()
{
    string vShaderStr = u_readShaderCode("demo.vert");
    string fShaderStr = u_readShaderCode("demo.frag");

    const char *vShaderCode = vShaderStr.c_str();
    const char *fShaderCode = fShaderStr.c_str();

    GLuint vShader = glCreateShader(GL_VERTEX_SHADER);
    GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);

    glShaderSource(vShader, 1, &vShaderCode, nullptr);
    glShaderSource(fShader, 1, &fShaderCode, nullptr);
    glCompileShader(vShader);
    glCompileShader(fShader);

    GLuint program = glCreateProgram();
    glAttachShader(program, vShader);
    glAttachShader(program, fShader);
    glLinkProgram(program);

    glDeleteShader(vShader);
    glDeleteShader(fShader);
    return program;
}

void u_processInput(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
    {
        glfwSetWindowShouldClose(window, true);
    }
}

int main()
{
    glfwInit();
    glfwInitHint(GLFW_VERSION_MAJOR, 4);
    glfwInitHint(GLFW_VERSION_MINOR, 1);
    glfwInitHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow *window = glfwCreateWindow(800, 600, "Demo", nullptr, nullptr);
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, u_framebuffer_size_callback);

    gladLoadGLLoader((GLADloadproc)glfwGetProcAddress);

    glfwSwapInterval(1);

    const int numVAOs = 1;
    GLuint vao[numVAOs];
    glBindVertexArray(vao[0]);
    GLuint program = u_createShaderProgram();

    while (!glfwWindowShouldClose(window))
    {
        u_processInput(window);

        glClear(GL_DEPTH_BUFFER_BIT);
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(program);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteProgram(program);
    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;
}
```