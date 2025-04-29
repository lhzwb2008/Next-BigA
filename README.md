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

## 快速部署

### 前提条件

- Python 3.8+
- Node.js 14+
- npm 或 yarn
- 长桥开放 API 的账号与密钥

### 一键部署

1. 克隆仓库:

```bash
git clone [仓库地址]
cd 上证指数开盘预测系统
```

2. 设置环境变量:

```bash
cp env.example .env
```

编辑 `.env` 文件，填入您的长桥 API 密钥:

```
LONGPORT_APP_KEY=您的APP_KEY
LONGPORT_APP_SECRET=您的APP_SECRET
LONGPORT_ACCESS_TOKEN=您的ACCESS_TOKEN
```

3. 一键部署命令:

```bash
# 安装依赖并启动应用
bash deploy.sh
```

### 手动部署

1. 安装后端依赖:

```bash
pip install -r requirements.txt
```

2. 安装前端依赖:

```bash
cd frontend
npm install
npm run build
cd ..
```

3. 启动服务:

```bash
python app.py
```

4. 访问网站:

打开浏览器访问 `http://localhost:5000`

## 开发模式

### 后端开发

```bash
python app.py
```

### 前端开发

```bash
cd frontend
npm start
```

前端开发服务器将在 `http://localhost:3000` 启动，并自动代理API请求到后端。
