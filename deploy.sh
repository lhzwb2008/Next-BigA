#!/bin/bash

# 颜色设置
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}===============================================${NC}"
echo -e "${BLUE}    上证指数开盘预测系统 - 环境部署脚本    ${NC}"
echo -e "${BLUE}===============================================${NC}"

# 检查环境
echo -e "\n${GREEN}[1/3]${NC} 检查环境..."

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}未检测到 Python3，请安装 Python3.8 或更高版本${NC}"
    exit 1
fi

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}未检测到 Node.js，请安装 Node.js 14 或更高版本${NC}"
    exit 1
fi

# 检查 npm
if ! command -v npm &> /dev/null; then
    echo -e "${RED}未检测到 npm，请安装 npm${NC}"
    exit 1
fi

# 安装Python依赖
echo -e "\n${GREEN}[2/3]${NC} 安装Python依赖..."
python3 -m pip install flask==2.2.3 werkzeug==2.2.3 flask-cors==3.0.10 python-dotenv==1.0.0 --user
if [ $? -ne 0 ]; then
    echo -e "${RED}Python依赖安装失败。尝试使用--break-system-packages选项...${NC}"
    python3 -m pip install flask==2.2.3 werkzeug==2.2.3 flask-cors==3.0.10 python-dotenv==1.0.0 --user --break-system-packages
    if [ $? -ne 0 ]; then
        echo -e "${RED}Python依赖安装失败，请手动安装:${NC}"
        echo -e "${BLUE}python3 -m pip install flask==2.2.3 werkzeug==2.2.3 flask-cors==3.0.10 python-dotenv==1.0.0 --user${NC}"
        exit 1
    fi
fi

# 检查环境变量文件
if [ ! -f ".env" ]; then
    if [ -f "env.example" ]; then
        echo -e "\n${BLUE}环境变量文件 .env 不存在，将从 env.example 创建${NC}"
        cp env.example .env
        echo -e "${BLUE}请编辑 .env 文件，填入您的长桥 API 密钥，或者保持现状使用模拟数据${NC}"
    else
        echo -e "${RED}未找到环境变量文件模板 env.example${NC}"
        exit 1
    fi
fi

# 构建前端
echo -e "\n${GREEN}[3/3]${NC} 构建前端..."
cd frontend && npm install && npm run build
if [ $? -ne 0 ]; then
    echo -e "${RED}前端构建失败${NC}"
    exit 1
fi
cd ..

echo -e "\n${GREEN}环境部署完成!${NC}"
echo -e "${BLUE}请查看 README.md 了解如何启动服务${NC}"
echo -e "${BLUE}===============================================${NC}" 