# 使用 GitHub Actions 自动化构建安卓 APK

由于在沙盒环境中直接构建安卓 APK 耗时较长且可能受资源限制，我们为您提供了一个 GitHub Actions 工作流，您可以利用它在自己的 GitHub 仓库中自动化构建 APK 文件。

## 什么是 GitHub Actions？

GitHub Actions 是 GitHub 提供的持续集成/持续部署 (CI/CD) 服务。它允许您自动化软件开发工作流，例如代码构建、测试和部署。通过配置 `.github/workflows` 目录下的 YAML 文件，您可以定义在特定事件（如代码推送）发生时自动执行的任务。

## 如何使用此工作流？

请按照以下步骤，在您的 GitHub 仓库中设置并运行 APK 构建工作流：

1.  **创建 GitHub 仓库**：
    如果您还没有 GitHub 仓库，请在 GitHub 上创建一个新的空仓库。例如，您可以命名为 `AI-Translator-App`。

2.  **上传项目代码**：
    将您之前下载的 `translator_app.zip` 解压后的所有文件（包括 `main.py`, `core.py`, `translator.kv`, `requirements.txt`, `buildozer.spec` 以及 `.github/workflows/build_apk.yml` 目录和文件）上传到您的 GitHub 仓库的根目录。
    
    确保 `.github/workflows/build_apk.yml` 文件位于正确的位置。

3.  **触发工作流**：
    *   **推送代码**：一旦您将项目代码推送到 `main` 分支，GitHub Actions 将自动触发构建工作流。
    *   **手动触发**：您也可以在 GitHub 仓库页面导航到 `Actions` 选项卡，选择 `Build Android APK` 工作流，然后点击 `Run workflow` 按钮手动触发。

4.  **监控构建进度**：
    在 `Actions` 选项卡中，您可以实时查看工作流的运行状态和日志。构建过程可能需要 10-20 分钟，具体取决于 GitHub Actions 的负载和您的项目大小。

5.  **下载 APK 文件**：
    工作流成功运行后，您会在 `Actions` 页面看到一个名为 `android-apk` 的 `Artifacts`（构件）。点击下载此构件，解压后即可获得 `aitranslator-0.1-debug.apk` 文件。

6.  **安装 APK 到您的安卓设备**：
    将下载的 APK 文件传输到您的安卓手机，然后点击安装。请确保您的手机允许安装来自未知来源的应用（通常在“设置”->“安全”或“应用”中）。

## `build_apk.yml` 文件内容

```yaml
name: Build Android APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.9'

    - name: Install Buildozer
      run: |
        pip install buildozer
        buildozer android debug --bootstrap-buildozer

    - name: Build Android APK
      run: buildozer android debug

    - name: Upload APK artifact
      uses: actions/upload-artifact@v4
      with:
        name: android-apk
        path: bin/*.apk
```

## 注意事项

*   **Python 版本**：工作流中指定使用 Python 3.9。如果您的项目对 Python 版本有特定要求，请相应修改 `python-version`。
*   **Buildozer 配置**：`buildozer android debug --bootstrap-buildozer` 命令会在首次运行时下载并配置 Android SDK、NDK 等必要工具。这可能需要一些时间。
*   **权限**：请确保 `buildozer.spec` 文件中包含了 `RECORD_AUDIO` 和 `INTERNET` 等必要的安卓权限。
*   **调试版本**：此工作流构建的是调试 (debug) 版本的 APK。如果您需要发布 (release) 版本，需要额外的配置，包括签名密钥等。

希望这份指南能帮助您顺利构建并安装您的 AI 同声传译应用！
