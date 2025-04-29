from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
from datetime import datetime
from dotenv import load_dotenv
import decimal
import random
import traceback

# 尝试加载环境变量
load_dotenv()

app = Flask(__name__, 
            static_folder='frontend/build/static',
            template_folder='frontend/build')
CORS(app)

def get_market_data():
    # 首先检查是否有API密钥
    api_key = os.environ.get('LONGPORT_APP_KEY')
    api_secret = os.environ.get('LONGPORT_APP_SECRET')
    access_token = os.environ.get('LONGPORT_ACCESS_TOKEN')
    
    # 如果API密钥未设置，使用模拟数据
    if not (api_key and api_secret and access_token):
        print("未检测到长桥API密钥，使用模拟数据...")
        return get_mock_data()
    
    try:
        # 从环境变量加载配置
        from longport.openapi import Config, QuoteContext
        config = Config.from_env()
        # 创建行情上下文
        quote_ctx = QuoteContext(config)
        
        # 股票代码列表
        symbols = ["YINN.US", "FXI.US"]
        
        # 获取股票基本行情
        quote_results = quote_ctx.quote(symbols)
        if not quote_results:
            return {"error": "未获取到行情数据"}
        
        # 存储涨跌幅数据和股票信息
        percentage_changes = {}
        stocks_data = []
        
        # 处理每个股票的信息
        for quote_info in quote_results:
            symbol = quote_info.symbol
            
            # 获取当前价格和开盘价
            current_price = float(quote_info.last_done)
            open_price = float(quote_info.open)
            
            # 计算涨跌幅
            price_change = current_price - open_price
            price_change_percentage = (price_change / open_price) * 100
            
            # 存储涨跌幅数据用于后续预测
            percentage_changes[symbol] = price_change_percentage
            
            # 添加股票数据
            stocks_data.append({
                "symbol": symbol,
                "current_price": current_price,
                "open_price": open_price,
                "price_change": price_change,
                "price_change_percentage": price_change_percentage,
                "high": float(quote_info.high),
                "low": float(quote_info.low),
                "volume": quote_info.volume,
                "turnover": quote_info.turnover
            })
        
        # 预测上证指数开盘情况
        prediction_data = {}
        
        # 确保我们有所需的数据
        if "YINN.US" in percentage_changes and "FXI.US" in percentage_changes:
            x = float(percentage_changes["YINN.US"])
            y = float(percentage_changes["FXI.US"])
            
            # 计算预测值 z = 0.4*x + 0.6*y
            z = 0.4 * x + 0.6 * y
            
            # 判断上证指数预测开盘情况
            if z > 0.5:
                prediction_status = "上涨"
            elif z < -0.5:
                prediction_status = "下跌"
            else:
                prediction_status = "平开"
            
            prediction_data = {
                "yinn_change": x,
                "fxi_change": y,
                "predicted_change": z,
                "prediction_status": prediction_status
            }
        else:
            prediction_data = {"error": "缺少必要的数据来进行预测"}
        
        return {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "stocks": stocks_data,
            "prediction": prediction_data
        }
        
    except Exception as e:
        error_msg = str(e)
        error_trace = traceback.format_exc()
        print(f"获取数据时出错: {error_msg}")
        print(error_trace)
        return get_mock_data()

def get_mock_data():
    """生成模拟数据，用于演示目的"""
    # 为YINN生成一个-3%到3%的随机涨跌幅
    yinn_change = random.uniform(-3, 3)
    # 为FXI生成一个-2%到2%的随机涨跌幅
    fxi_change = random.uniform(-2, 2)
    
    # 生成模拟股票数据
    stocks_data = []
    
    # YINN数据
    yinn_open = round(random.uniform(20, 30), 2)
    yinn_current = round(yinn_open * (1 + yinn_change/100), 2)
    yinn_price_change = yinn_current - yinn_open
    stocks_data.append({
        "symbol": "YINN.US",
        "current_price": yinn_current,
        "open_price": yinn_open,
        "price_change": yinn_price_change,
        "price_change_percentage": yinn_change,
        "high": round(max(yinn_current, yinn_open) * 1.01, 2),
        "low": round(min(yinn_current, yinn_open) * 0.99, 2),
        "volume": random.randint(100000, 1000000),
        "turnover": random.randint(3000000, 30000000)
    })
    
    # FXI数据
    fxi_open = round(random.uniform(30, 40), 2)
    fxi_current = round(fxi_open * (1 + fxi_change/100), 2)
    fxi_price_change = fxi_current - fxi_open
    stocks_data.append({
        "symbol": "FXI.US",
        "current_price": fxi_current,
        "open_price": fxi_open,
        "price_change": fxi_price_change,
        "price_change_percentage": fxi_change,
        "high": round(max(fxi_current, fxi_open) * 1.01, 2),
        "low": round(min(fxi_current, fxi_open) * 0.99, 2),
        "volume": random.randint(2000000, 8000000),
        "turnover": random.randint(60000000, 320000000)
    })
    
    # 计算预测值 z = 0.4*x + 0.6*y
    z = 0.4 * yinn_change + 0.6 * fxi_change
    
    # 判断上证指数预测开盘情况
    if z > 0.5:
        prediction_status = "上涨"
    elif z < -0.5:
        prediction_status = "下跌"
    else:
        prediction_status = "平开"
    
    prediction_data = {
        "yinn_change": yinn_change,
        "fxi_change": fxi_change,
        "predicted_change": z,
        "prediction_status": prediction_status
    }
    
    return {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "stocks": stocks_data,
        "prediction": prediction_data,
        "is_mock": True
    }

@app.route('/api/market-data')
def market_data():
    data = get_market_data()
    return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080) 