import os
from datetime import datetime
from longport.openapi import Config, QuoteContext
import decimal  # 添加decimal模块

def main():
    # 从环境变量加载配置
    # 如果没有设置环境变量，请替换以下代码为：
    # config = Config(app_key="YOUR_APP_KEY", app_secret="YOUR_APP_SECRET", access_token="YOUR_ACCESS_TOKEN")
    try:
        config = Config.from_env()
        print("成功从环境变量加载配置")
    except Exception as e:
        print(f"从环境变量加载配置失败: {e}")
        print("请确保已设置以下环境变量:")
        print("LONGPORT_APP_KEY, LONGPORT_APP_SECRET, LONGPORT_ACCESS_TOKEN")
        return

    try:
        # 创建行情上下文
        quote_ctx = QuoteContext(config)
        
        # 股票代码列表
        symbols = ["YINN.US", "FXI.US"]
        
        # 获取股票基本行情
        quote_results = quote_ctx.quote(symbols)
        if not quote_results:
            print("未获取到行情数据")
            return
        
        # 存储涨跌幅数据
        percentage_changes = {}
        
        # 处理每个股票的信息
        for quote_info in quote_results:
            symbol = quote_info.symbol
            
            # 获取当前价格和开盘价 - 确保转换为float类型
            current_price = float(quote_info.last_done)
            open_price = float(quote_info.open)
            
            # 计算涨跌幅
            price_change = current_price - open_price
            price_change_percentage = (price_change / open_price) * 100
            
            # 存储涨跌幅数据用于后续预测
            percentage_changes[symbol] = price_change_percentage
            
            # 输出结果
            print(f"\n股票代码: {symbol}")
            print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"当前价格: {current_price}")
            print(f"开盘价格: {open_price}")
            print(f"涨跌额: {price_change:.4f}")
            print(f"涨跌幅: {price_change_percentage:.2f}%")
            
            # 输出更多股票信息
            print("\n更多股票信息:")
            print(f"最高价: {float(quote_info.high)}")
            print(f"最低价: {float(quote_info.low)}")
            print(f"成交量: {quote_info.volume}")
            print(f"成交额: {quote_info.turnover}")
            print("-" * 50)
        
        # 预测上证指数开盘情况
        print("\n预测上证指数开盘情况:")
        
        # 确保我们有所需的数据
        if "YINN.US" in percentage_changes and "FXI.US" in percentage_changes:
            x = float(percentage_changes["YINN.US"])
            y = float(percentage_changes["FXI.US"])
            
            # 计算预测值 z = 0.4*x + 0.6*y
            z = 0.4 * x + 0.6 * y
            
            print(f"YINN.US 涨跌幅(x): {x:.2f}%")
            print(f"FXI.US 涨跌幅(y): {y:.2f}%")
            print(f"预测上证指数涨跌幅(z = 0.4*x + 0.6*y): {z:.2f}%")
            
            # 判断上证指数预测开盘情况
            if z > 0.5:
                prediction = "预测上涨"
            elif z < -0.5:
                prediction = "预测下跌"
            else:
                prediction = "预测平开"
                
            print(f"上证指数开盘预测: {prediction}")
        else:
            print("缺少必要的数据来进行预测")
        
    except Exception as e:
        print(f"查询过程中发生错误: {e}")
        import traceback
        traceback.print_exc()  # 打印详细错误信息

if __name__ == "__main__":
    main()
