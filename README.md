# AI 同声传译 App

这是一个基于 Python 和 KivyMD 开发的安卓同声传译应用程序。它能够实时识别语音、进行翻译，并将翻译结果通过语音合成播放出来。

## 功能特性

*   **实时语音识别 (STT)**：利用 `SpeechRecognition` 库，支持多种语言的语音输入。
*   **多语言翻译**：通过 `googletrans` 库实现源语言到目标语言的即时翻译。
*   **语音合成 (TTS)**：使用 `pyttsx3` 和 `plyer` 库将翻译结果朗读出来，支持安卓原生 TTS。
*   **KivyMD 界面**：简洁美观的用户界面，提供良好的用户体验。
*   **语言选择**：用户可以方便地选择源语言和目标语言。

## 技术栈

*   **Python**：主要开发语言。
*   **KivyMD**：用于构建安卓应用的用户界面。
*   **SpeechRecognition**：处理语音识别。
*   **googletrans**：提供翻译功能。
*   **pyttsx3 / plyer**：实现语音合成。
*   **Buildozer**：用于将 Kivy 应用打包成安卓 APK。

## 项目结构

```
translator_app/
├── main.py             # KivyMD 应用主文件，处理 UI 逻辑和事件
├── core.py             # 核心翻译逻辑，包含 STT、翻译和 TTS 功能
├── translator.kv       # KivyMD 界面布局文件
├── requirements.txt    # Python 依赖列表
└── buildozer.spec      # Buildozer 配置文件，用于安卓打包
```

## 安装与运行 (开发环境)

1.  **克隆仓库**：
    ```bash
    git clone <仓库地址>
    cd translator_app
    ```

2.  **创建虚拟环境并安装依赖**：
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **运行应用**：
    ```bash
    python main.py
    ```

## 打包为安卓 APK

1.  **安装 Buildozer**：
    ```bash
    pip install buildozer
    ```

2.  **初始化 Buildozer (如果 `buildozer.spec` 不存在)**：
    ```bash
    buildozer init
    ```
    *注意：本项目已提供 `buildozer.spec` 文件，无需再次初始化。*

3.  **配置 `buildozer.spec`**：
    请确保 `buildozer.spec` 文件中的 `requirements`、`android.permissions` 等配置正确。本项目已为您配置好。

4.  **构建 APK**：
    ```bash
    buildozer android debug
    ```
    首次构建可能需要下载 Android SDK、NDK 等工具，耗时较长。请确保网络连接稳定。

5.  **安装到设备**：
    构建成功后，APK 文件位于 `bin/` 目录下。您可以通过 `adb install` 命令将其安装到安卓设备上：
    ```bash
    adb install bin/aitranslator-0.1-debug.apk
    ```

## 注意事项

*   **网络连接**：语音识别和翻译功能需要稳定的互联网连接。
*   **权限**：应用需要麦克风和互联网权限。
*   **pyttsx3 在安卓上的兼容性**：`pyttsx3` 在安卓上可能无法直接工作，因此本项目优先使用 `plyer` 提供的安卓原生 TTS 功能作为替代方案。

## 许可证

本项目采用 MIT 许可证。
