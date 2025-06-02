# ML Traffic Light Optimization

A demo project using SVM (for density classification) and Random Forest (for green time prediction) to optimize traffic signal green times and minimize travel delay.

## Features
- SVM-based traffic density classification
- Random Forest-based green time prediction
- MongoDB for data storage and analytics
- Flask API and basic dashboard

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Start MongoDB locally.
3. Train the ML models: `python train_models.py`
4. Simulate traffic: `python simulate_traffic.py`
5. Start the dashboard: `python app.py`
6. Visit [http://localhost:5000](http://localhost:5000)

## References
- [Machine Learning-Enhanced Traffic Light Optimization System](https://dergipark.org.tr/en/download/article-file/4347610)
- [A Novel Approach to Proactively Optimize Urban Traffic Systems through Machine Learning](https://nhsjs.com/wp-content/uploads/2024/02/A-Novel-Approach-to-Proactively-Optimize-Urban-Traffic-Systems-through-Machine-Learning-2.pdf)
