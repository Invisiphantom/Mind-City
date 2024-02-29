Ubuntu22.04配置OpenGL环境

```bash
sudo apt install build-essential g++
sudo apt install libgl-dev libglfw3-dev
```

https://glad.dav1d.de/
选择最新版本gl, 勾选"Local Files", 然后生成并下载


修改`.vscode/tasks.json`文件, 添加头文件和链接操作
```json
    "args": [
        "-fdiagnostics-color=always",
        "-g",
        "${file}",
        "${workspaceFolder}/glad/glad.c",
        "-o",
        "${fileDirname}/${fileBasenameNoExtension}",
        "-lGL",
        "-lglfw",
    ],
```

<br>


OpenGL教程: [LearnOpenGL](https://learnopengl.com/Getting-started/OpenGL)


