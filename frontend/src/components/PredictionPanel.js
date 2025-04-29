import React from 'react';
import './PredictionPanel.css';

const PredictionPanel = ({ predictionData, timestamp }) => {
  if (!predictionData) {
    return (
      <div className="prediction-panel prediction-panel-loading">
        <h2>预测数据加载中...</h2>
      </div>
    );
  }

  if (predictionData.error) {
    return (
      <div className="prediction-panel prediction-panel-error">
        <h2>预测错误</h2>
        <p>{predictionData.error}</p>
      </div>
    );
  }

  // 根据预测状态设置样式
  const getPredictionStatusClass = () => {
    if (predictionData.prediction_status === '上涨') return 'prediction-up';
    if (predictionData.prediction_status === '下跌') return 'prediction-down';
    return 'prediction-flat';
  };

  // 根据预测状态设置图标
  const getPredictionIcon = () => {
    if (predictionData.prediction_status === '上涨') {
      return (
        <svg className="prediction-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M7 17L17 7M17 7H7M17 7V17" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      );
    } else if (predictionData.prediction_status === '下跌') {
      return (
        <svg className="prediction-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M7 7L17 17M17 17H7M17 17V7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      );
    } else {
      return (
        <svg className="prediction-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M5 12H19" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      );
    }
  };

  return (
    <div className={`prediction-panel ${getPredictionStatusClass()}`}>
      <h2 className="prediction-title">上证指数开盘预测</h2>
      
      <div className="prediction-result">
        {getPredictionIcon()}
        <div className="prediction-status">{predictionData.prediction_status}</div>
        <div className="prediction-value">{predictionData.predicted_change.toFixed(2)}%</div>
      </div>
      
      <div className="prediction-factors">
        <div className="prediction-factor">
          <div className="factor-label">YINN.US 涨跌幅</div>
          <div className={`factor-value ${predictionData.yinn_change > 0 ? 'positive' : predictionData.yinn_change < 0 ? 'negative' : ''}`}>
            {predictionData.yinn_change.toFixed(2)}%
          </div>
        </div>
        
        <div className="prediction-factor">
          <div className="factor-label">FXI.US 涨跌幅</div>
          <div className={`factor-value ${predictionData.fxi_change > 0 ? 'positive' : predictionData.fxi_change < 0 ? 'negative' : ''}`}>
            {predictionData.fxi_change.toFixed(2)}%
          </div>
        </div>
      </div>
    </div>
  );
};

export default PredictionPanel; 