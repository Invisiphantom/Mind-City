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


| 图形库  | 介绍                                                 |
| ------- | ---------------------------------------------------- |
| OpenGL  | Open Graphics Library, 开放图形库                    |
| GLAD    | GL Loader Generator, OpenGL加载器生成器              |
| GLSL    | OpenGL Shading Language, OpenGL着色器语言            |
| GLM     | OpenGL Mathematics, OpenGL数学库                     |
| GLEW    | OpenGL Extension Wrangler Library, OpenGL扩展库      |
| GLFW    | OpenGL FrameWork, OpenGL框架                         |
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

```bash
sudo apt install build-essential g++ gdb
sudo apt install libgl-dev libglfw3-dev
```

https://glad.dav1d.de/
选择4.1版本gl, 勾选"Local Files", 然后生成并下载glad.zip
`sudo mv glad /usr/include/`


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

| 图形管线       | 英文名                      | 功能     |
| -------------- | --------------------------- | -------- |
| 顶点着色器     | Vertex Shader               | 顶点处理 |
| 曲面细分着色器 | Tessellation Control Shader | 图元处理 |
| 几何着色器     | Geometry Shader             | 图元处理 |
| 光栅化着色器   | Rasterization Shader        | 片段处理 |
| 片段着色器     | Fragment Shader             | 片段处理 |
| 像素操作       | Pixel Shader                | 片段处理 |


| glad函数                             | 功能           |
| ------------------------------------ | -------------- |
| `int gladLoadGLLoader(GLADloadproc)` | 加载OpenGL函数 |


| glfw函数                                                                                                          | 功能                         |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `int glfwInit()`                                                                                                  | 初始化glfw库                 |
| `void glfwWindowHint(int hint, int value)`                                                                        | 配置glfw参数                 |
| `void glfwTerminate()`                                                                                            | 终止glfw库                   |
| `GLFWwindow *glfwCreateWindow(int width, int height, const char *title, GLFWmonitor *monitor, GLFWwindow *share)` | 创建窗口                     |
| `void glfwMakeContextCurrent(GLFWwindow *window)`                                                                 | 指定窗口上下文               |
| `void glfwDestroyWindow(GLFWwindow *window)`                                                                      | 销毁窗口                     |
| `GLFWframebuffersizefun glfwSetFramebufferSizeCallback(GLFWwindow *window, GLFWframebuffersizefun callback)`      | 设置帧缓冲区大小变化回调函数 |
| `GLFWglproc glfwGetProcAddress(const char *procname)`                                                             | 获取OpenGL函数指针           |
| `void glfwSwapInterval(int interval)`                                                                             | 设置垂直同步                 |
| `int glfwWindowShouldClose(GLFWwindow *window)`                                                                   | 检测窗口是否应该关闭         |
| `void glfwSetWindowShouldClose(GLFWwindow *window, int value)`                                                    | 设置窗口是否应该关闭         |
| `void glfwSwapBuffers(GLFWwindow *window)`                                                                        | 交换渲染缓冲区               |
| `void glfwPollEvents()`                                                                                           | 处理窗口事件                 |
| `int glfwGetKey(GLFWwindow *window, int key)`                                                                     | 获取窗口关键字               |


void glGetAttachedShaders(	GLuint program,
 	GLsizei maxCount,
 	GLsizei *count,
 	GLuint *shaders);

| gl函数                                                                                         | 功能               |
| ---------------------------------------------------------------------------------------------- | ------------------ |
| `void glViewport(GLint x, GLint y, GLsizei width, GLsizei height)`                             | 设置视窗位置与大小 |
| `void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)`                   | 设置清空颜色缓冲区 |
| `void glClear(GLbitfield mask)`                                                                | 清空缓冲区         |
| `GLuint glCreateShader(GLenum shaderType);`                                                    | 创建着色器         |
| `void glShaderSource(GLuint shader, GLsizei count, GLchar **string, const GLint *length)`      | 设置着色器源码     |
| `void glCompileShader(GLuint shader)`                                                          | 编译着色器源码     |
| `GLuint glCreateProgram()`                                                                     | 创建着色器程序     |
| `void glGetAttachedShaders(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders)` | 绑定程序与着色器   |
| `void glLinkProgram(GLuint program)`                                                           | 链接生成可执行程序 |
| `void glDeleteShader(GLuint shader)`                                                           | 删除着色器         |

| GLenum shaderType           | 着色器类型         |
| --------------------------- | ------------------ |
| `GL_VERTEX_SHADER`          | 顶点着色器         |
| `GL_TESS_CONTROL_SHADER`    | 曲面细分控制着色器 |
| `GL_TESS_EVALUATION_SHADER` | 曲面细分评估着色器 |
| `GL_GEOMETRY_SHADER`        | 几何着色器         |
| `GL_FRAGMENT_SHADER`        | 片段着色器         |
| `GL_COMPUTE_SHADER`         | 计算着色器         |


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


```cpp
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <iostream>

void framebuffer_size_callback(GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

// settings
const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

int main()
{
    // glfw: initialize and configure
    // ------------------------------
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // glfw window creation
    // --------------------
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    // glad: load all OpenGL function pointers
    // ---------------------------------------
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }    

    // render loop
    // -----------
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

    // glfw: terminate, clearing all previously allocated GLFW resources.
    // ------------------------------------------------------------------
    glfwTerminate();
    return 0;
}

// process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly
// ---------------------------------------------------------------------------------------------------------
void processInput(GLFWwindow *window)
{
    if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}

// glfw: whenever the window size changed (by OS or user resize) this callback function executes
// ---------------------------------------------------------------------------------------------
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    // make sure the viewport matches the new window dimensions; note that width and 
    // height will be significantly larger than specified on retina displays.
    glViewport(0, 0, width, height);
}
```