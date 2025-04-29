import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import Header from './components/Header';
import PredictionPanel from './components/PredictionPanel';
import StocksList from './components/StocksList';
import LoadingSpinner from './components/LoadingSpinner';

function App() {
  const [marketData, setMarketData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [lastUpdated, setLastUpdated] = useState(null);

  const fetchMarketData = async () => {
    try {
      setLoading(true);
      const response = await axios.get('/api/market-data');
      setMarketData(response.data);
      setLastUpdated(new Date());
      setLoading(false);
    } catch (err) {
      console.error('获取市场数据失败:', err);
      setError('获取市场数据失败，请刷新页面重试');
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMarketData();
    
    // 设置每分钟自动刷新
    const interval = setInterval(() => {
      fetchMarketData();
    }, 60000);
    
    return () => clearInterval(interval);
  }, []);

  const handleRefresh = () => {
    fetchMarketData();
  };

  return (
    <div className="app">
      <Header onRefresh={handleRefresh} lastUpdated={lastUpdated} />
      
      {loading && !marketData ? (
        <div className="loading-container">
          <LoadingSpinner />
          <p>加载中，请稍候...</p>
        </div>
      ) : error ? (
        <div className="error-container">
          <p className="error-message">{error}</p>
          <button onClick={handleRefresh} className="refresh-button">
            重试
          </button>
        </div>
      ) : marketData && (
        <>
          <main className="main-content">
            <PredictionPanel predictionData={marketData.prediction} timestamp={marketData.timestamp} />
            <StocksList stocks={marketData.stocks} />
          </main>
        </>
      )}
    </div>
  );
}

export default App; 