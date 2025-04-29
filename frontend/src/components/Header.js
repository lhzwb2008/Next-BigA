import React from 'react';
import './Header.css';

const Header = ({ onRefresh, lastUpdated }) => {
  return (
    <header className="header">
      <div className="header-container">
        <h1 className="header-title">上证指数开盘预测</h1>
        <div className="header-actions">
          {lastUpdated && (
            <div className="last-updated">
              最后更新: {lastUpdated.toLocaleString('zh-CN')}
            </div>
          )}
          <button className="refresh-button" onClick={onRefresh}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M23 4v6h-6"></path>
              <path d="M1 20v-6h6"></path>
              <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10"></path>
              <path d="M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
            </svg>
            刷新
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header; 