# 上证指数开盘预测系统

一个基于YINN.US和FXI.US股票数据预测上证指数开盘情况的网站应用。

## 功能特点

- 实时显示YINN.US和FXI.US的股票行情
- 基于这两只股票的涨跌幅预测上证指数开盘情况
- 自动刷新数据
- 美观简洁的用户界面

## 技术栈

- 后端: Flask (Python)
- 前端: React.js
- 数据来源: 长桥开放 API (LongPort OpenAPI)

## 部署与运行

### 前提条件

- Python 3.8+
- Node.js 14+
- npm 或 yarn
- 长桥开放 API 的账号与密钥（可选，没有密钥将使用模拟数据）

### 环境部署

使用部署脚本安装依赖并构建前端：

```bash
# 安装依赖并构建前端
bash deploy.sh
```

### 启动服务

部署完成后，您可以分别启动后端和前端服务：

#### 1. 启动后端服务 (API端口: 8080)

```bash
# 直接启动
python3 app.py

# 或使用nohup在后台运行
nohup python3 app.py > api.log 2>&1 &
```

#### 2. 启动前端服务 (Web端口: 80)

如果您希望在开发模式下运行前端（需要sudo权限运行在80端口）：

```bash
cd frontend
sudo npm start
```

#### 3. 使用构建好的生产版本

如果您已经运行了部署脚本，前端已经构建好并配置给Flask服务。
只需启动后端服务，然后访问 `http://localhost:8080` 即可。

#### 4. 使用其他静态服务器

您也可以使用其他静态服务器托管前端构建文件：

```bash
# 安装serve
npm install -g serve

# 启动服务在80端口
sudo serve -s frontend/build -l 80
```

## 开发模式

### 1. 后端开发（端口8080）

```bash
python3 app.py
```

### 2. 前端开发（端口80）

```bash
cd frontend
sudo npm start
```

前端开发服务器将在 `http://localhost:80` 启动，并自动代理API请求到后端的 `http://localhost:8080`。

## 额外说明

- 如果没有配置长桥API密钥，系统会使用模拟数据。
- 页面每分钟自动刷新一次数据。
- 开发模式下前端使用80端口可能需要管理员权限（sudo）。
