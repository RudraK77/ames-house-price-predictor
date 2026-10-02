# House Price Prediction

Predicts historical Ames, Iowa house sale prices in USD.

## Inputs
- Above-ground living area in square feet
- Bedrooms above ground
- Construction year
- Overall material and finish quality, rated 1–10

## Model
Random Forest with 100 trees and min_samples_leaf=5.

## Evaluation
- Baseline test MAE: $59,568
- Final model test MAE: $23,233
- 1,168 training houses and 292 test houses
- Model selection used 934 learning and 234 validation houses
- Initial model test results were viewed before final model selection

## Run locally
Requires Python 3.12.

Activate the environment:
source .venv312/bin/activate

Launch the app:
python -m streamlit run app.py

## Limitations
Uses four features and historical data from one city.
Not intended to estimate current Indian property prices.
MAE is an average error, not a guaranteed prediction range.

## Live Demo
https://ames-house-price-predictor-vawptf5opue3hekqvbavwq.streamlit.app/
