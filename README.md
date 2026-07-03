### **Time Series Forecasting for Portfolio Management Optimization**



An end-to-end financial analytics project that applies time series forecasting and Modern Portfolio Theory (MPT) to optimize investment portfolios. Using historical market data from Yahoo Finance, the project compares statistical and deep learning forecasting models, constructs an optimal portfolio, and validates the strategy through historical backtesting.



#### **Overview**



Guide Me in Finance (GMF) Investments aims to improve portfolio management by combining historical financial data with predictive analytics. This project demonstrates how machine learning, statistical modeling, and portfolio optimization techniques can be integrated into a complete investment decision-making pipeline.



Rather than attempting to perfectly predict future stock prices, the project follows industry best practices by using forecasts as one input for portfolio optimization while accounting for uncertainty and risk.

##### 

#### **Business Objective**



The primary goals of this project are to:



* Forecast future market movements using historical financial data.
* Compare classical statistical models with deep learning approaches.
* Optimize a multi-asset investment portfolio using Modern Portfolio Theory.
* Evaluate portfolio performance through historical backtesting.
* Generate actionable investment recommendations supported by quantitative analysis.



Assets Used

Asset	Ticker	              Description	                        Risk Level

Tesla	TSLA	High-growth automobile manufacturer	                  High

Vanguard Total Bond Market ETF	BND	Investment-grade U.S. bond ETF	   Low

SPDR S\&P 500 ETF	SPY	Tracks the S\&P 500 Index	          Medium



Historical data covers:



Start Date: January 1, 2015

End Date: June 30, 2026



Data is collected using the Yahoo Finance (yfinance) Python library.



#### **Project Workflow**



The project consists of five major stages:



**Task 1 — Data Collection \& Exploratory Data Analysis**

* Download historical market data
* Clean and preprocess datasets
* Handle missing values
* Compute daily returns
* Calculate rolling volatility
* Perform stationarity tests (ADF)
* Calculate risk metrics
* Visualize trends and market behavior



**Deliverables**



* Clean datasets
* Exploratory visualizations
* Risk analysis
* Stationarity analysis



**Task 2 — Time Series Forecasting**



Two forecasting approaches are implemented and compared.



Statistical Model

ARIMA / SARIMA



**Model tuning includes:**



1. ACF/PACF analysis
2. Auto ARIMA
3. Hyperparameter optimization
4. Deep Learning Model
5. Long Short-Term Memory (LSTM)



**The LSTM model includes:**



1. Sequence generation
2. Feature scaling
3. Model training
4. Prediction
5. Hyperparameter tuning



**Models are evaluated using:**



1. MAE
2. RMSE
3. MAPE



**Task 3 — Future Market Forecasting**



Using the best-performing forecasting model:



* Generate future stock price forecasts
* Forecast 6–12 months ahead
* Plot confidence intervals
* Analyze long-term market trends
* Assess uncertainty
* Identify investment opportunities and risks





**Task 4 — Portfolio Optimization**



Portfolio optimization is performed using Modern Portfolio Theory (MPT).



**Key steps include:**



1. Expected return estimation
2. Covariance matrix calculation
3. Efficient Frontier generation
4. Maximum Sharpe Ratio portfolio
5. Minimum Volatility portfolio
6. Portfolio recommendation



**Performance metrics include:**



* Expected Return
* Portfolio Volatility
* Sharpe Ratio
* Asset Allocation



**Task 5 — Portfolio Backtesting**



The optimized portfolio is validated using historical data.



**Backtesting includes:**



* Benchmark comparison (60% SPY / 40% BND)
* Strategy simulation
* Monthly portfolio evaluation
* Cumulative return analysis
* Performance comparison



**Metrics include:**



* Total Return
* Annualized Return
* Sharpe Ratio
* Maximum Drawdown

#### 

#### **Project Structure**



portfolio-optimization/

│

├── .github/

│   └── workflows/

│       └── unittests.yml

│

├── .vscode/

│   └── settings.json

│

├── data/

│   └── processed/

│

├── notebooks/

│   ├── README.md

│   └── \_\_init\_\_.py

│

├── scripts/

│   └── \_\_init\_\_.py

│

├── src/

│   └── \_\_init\_\_.py

│

├── tests/

│   └── \_\_init\_\_.py

│

├── requirements.txt

├── README.md

└── .gitignore



#### **Technologies Used**



Programming Language:  Python

Data Collection: yfinance

Data Processing: pandas, numpy

Visualization: matplotlib, seaborn

Statistical Modeling: statsmodels, pmdarima

Deep Learning: TensorFlow, Keras

Portfolio Optimization: PyPortfolioOpt, scipy

Model Evaluation: scikit-learn

Development Tools: Jupyter Notebook, Git, GitHub



#### **Installation**



Clone the repository: git clone https://github.com/yourusername/portfolio-optimization.git



Navigate into the project: cd portfolio-optimization



Create a virtual environment:



Windows

python -m venv venv

venv\\Scripts\\activate

Linux / macOS

python -m venv venv

source venv/bin/activate



Install dependencies:



pip install -r requirements.txt

Running the Project



Step 1

Download financial data

python scripts/download\_data.py



Step 2

Run exploratory analysis

jupyter notebook

Execute the Task 1 notebook.



Step 3

Train forecasting models

python scripts/train\_models.py



Step 4

Generate forecasts

python scripts/forecast.py



Step 5

Optimize portfolio

python scripts/portfolio\_optimization.py



Step 6

Run strategy backtest

python scripts/backtest.py



#### **Expected Outputs**



The project generates:



* Cleaned financial datasets
* Closing price visualizations
* Daily return analysis
* Volatility plots
* Stationarity test results
* ARIMA/SARIMA forecasts
* LSTM forecasts
* Forecast comparison charts
* Efficient Frontier visualization
* Covariance heatmap
* Portfolio allocation results
* Backtesting performance plots
* Investment recommendations
* Performance Metrics
* Forecasting Models
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Percentage Error (MAPE)
* Portfolio
* Expected Return
* Portfolio Volatility
* Sharpe Ratio
* Backtesting
* Total Return
* Annualized Return
* Sharpe Ratio
* Maximum Drawdown



#### **Key Learning Outcomes**



This project demonstrates practical experience in:



* Financial data acquisition using APIs
* Time series preprocessing
* Exploratory financial data analysis
* Stationarity testing
* ARIMA/SARIMA forecasting
* LSTM neural networks
* Model evaluation
* Modern Portfolio Theory
* Efficient Frontier optimization
* Investment risk analysis
* Portfolio backtesting
* Financial data visualization



#### **Future Improvements**



Potential enhancements include:



* Incorporating macroeconomic indicators
* Adding additional financial assets
* Integrating sentiment analysis from financial news
* Implementing Transformer-based forecasting models
* Automating the pipeline with workflow orchestration tools
* Deploying the forecasting system as a web application
* Enabling real-time market data updates



