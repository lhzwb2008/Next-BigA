import React from 'react';
import './StocksList.css';

const StocksList = ({ stocks }) => {
  if (!stocks || stocks.length === 0) {
    return (
      <div className="stocks-list empty">
        <p>没有可用的股票数据</p>
      </div>
    );
  }

  return (
    <div className="stocks-list">
      <h2 className="stocks-title">相关标的实时行情</h2>
      
      <div className="stocks-grid">
        {stocks.map((stock, index) => (
          <div key={index} className="stock-card">
            <div className="stock-header">
              <div className="stock-symbol">{stock.symbol}</div>
              <div 
                className={`stock-change ${
                  stock.price_change_percentage > 0 
                    ? 'positive' 
                    : stock.price_change_percentage < 0 
                      ? 'negative' 
                      : ''
                }`}
              >
                {stock.price_change_percentage > 0 ? '+' : ''}
                {stock.price_change_percentage.toFixed(2)}%
              </div>
            </div>
            
            <div className="stock-price">
              {stock.current_price.toFixed(2)}
              <span className="price-change">
                {stock.price_change > 0 ? '+' : ''}
                {stock.price_change.toFixed(2)}
              </span>
            </div>
            
            <div className="stock-details">
              <div className="detail-row">
                <div className="detail-label">开盘价</div>
                <div className="detail-value">{stock.open_price.toFixed(2)}</div>
              </div>
              <div className="detail-row">
                <div className="detail-label">最高价</div>
                <div className="detail-value">{stock.high.toFixed(2)}</div>
              </div>
              <div className="detail-row">
                <div className="detail-label">最低价</div>
                <div className="detail-value">{stock.low.toFixed(2)}</div>
              </div>
              <div className="detail-row">
                <div className="detail-label">成交量</div>
                <div className="detail-value">{formatNumber(stock.volume)}</div>
              </div>
              <div className="detail-row">
                <div className="detail-label">成交额</div>
                <div className="detail-value">{formatCurrency(stock.turnover)}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// 格式化数字为更易读的格式（添加千位分隔符）
const formatNumber = (num) => {
  return new Intl.NumberFormat('zh-CN').format(num);
};

// 格式化货币（假设是美元）
const formatCurrency = (amount) => {
  return new Intl.NumberFormat('zh-CN', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(amount);
};

export default StocksList; 