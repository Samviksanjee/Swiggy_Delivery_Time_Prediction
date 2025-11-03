# Swiggy Delivery Time Prediction

A machine learning-powered web application that predicts delivery time for Swiggy orders based on various real-world factors like rider characteristics, weather conditions, traffic, and delivery parameters.

## Overview

This project implements a **Streamlit-based predictive system** that estimates the time required to deliver food orders by analyzing multiple features including rider details, environmental conditions, vehicle information, and delivery logistics. The model uses a **Random Forest Regressor** trained on historical delivery data to make accurate predictions.

## Features

The application predicts delivery time by taking the following inputs:

- **Rider Information**: Age (20-50 years) and rating (0-5 stars)
- **Environmental Conditions**: Weather type and traffic status
- **Vehicle Details**: Vehicle condition and type of vehicle
- **Delivery Parameters**: Multiple deliveries, festival flag, city name, and weekend status
- **Time & Distance**: Pickup time (in minutes), order hour (0-24), and distance between restaurant and delivery location

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **Frontend Framework** | Streamlit |
| **Data Processing** | Pandas |
| **Machine Learning** | scikit-learn (Random Forest Regressor) |
| **Data Preprocessing** | OneHotEncoder, OrdinalEncoder, StandardScaler |
| **Model Serialization** | pickle |

## Project Structure

```
Swiggy-Delivery-Time-Prediction/
├── app.py                    # Main Streamlit application
├── swiggy.csv               # Training dataset
├── Deployment.pkl           # Serialized trained model
└── README.md                # Project documentation
```

## Installation

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Samviksanjee/swiggy-delivery-time-prediction.git
   cd swiggy-delivery-time-prediction
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**
   ```bash
   pip install streamlit pandas scikit-learn or pip install -r requirements.txt 
   ```

## Usage

1. **Prepare your data**
   - Ensure `swiggy_cleaned.csv` is in the project root directory
   - Ensure `Deployment.pkl` (trained model) is in the project root directory

2. **Run the application**
   ```bash
   streamlit run app.py
   ```

3. **Access the web interface**
   - The application will open at `http://localhost:8501` in your default browser

4. **Make predictions**
   - Fill in the form fields with delivery details
   - Click the **"Predict"** button to get the estimated delivery time in minutes
   - A celebratory snow animation appears after prediction

## How It Works

The application follows this workflow:

1. **Data Loading**: Reads the `swiggy_cleaned.csv` dataset and removes missing values
2. **User Input**: Collects delivery parameters through interactive Streamlit widgets
3. **Model Loading**: Deserializes the pre-trained Random Forest model from `Deployment.pkl`
4. **Prediction**: Uses the model to predict delivery time based on input features
5. **Output**: Displays the predicted delivery time in minutes with visual feedback

## Model Details

- **Algorithm**: Random Forest Regressor
- **Training Data**: Historical Swiggy delivery records
- **Input Features**: 12+ delivery and environmental parameters
- **Output**: Estimated delivery time (in minutes)
- **Preprocessing**: Categorical features encoded and numerical features scaled using scikit-learn transformers

## Requirements File

Create a `requirements.txt` for easy installation:

```txt
streamlit>=1.28.0
pandas>=1.5.0
scikit-learn>=1.3.0
```

Install all dependencies at once:
```bash
pip install -r requirements.txt
```

## Example Input Scenario

| Parameter | Example Value |
|-----------|--------------|
| Rider Age | 28 |
| Rider Rating | 4.5 |
| Weather | Rainy |
| Traffic | Heavy |
| Vehicle Condition | Good |
| Type of Vehicle | Bike |
| Multiple Deliveries | 2 |
| Festival | No |
| City Name | Bangalore |
| Is Weekend | Yes |
| Pickup Time | 5 minutes |
| Order Hour | 19 |
| Distance | 8 km |

**Predicted Output**: The Delivery Time is approximately 25-35 minutes

## Dataset Requirements

The `swiggy.csv` file should contain the following columns:

- `age`: Rider age
- `ratings`: Rider rating
- `weather`: Weather conditions
- `traffic`: Traffic conditions
- `vehicle_condition`: Condition of the delivery vehicle
- `type_of_vehicle`: Type of vehicle used
- `multiple_deliveries`: Number of multiple deliveries
- `festival`: Whether it's a festival day
- `city_name`: Delivery city
- `is_weekend`: Whether it's a weekend
- `pickup_time_minutes`: Time to pick up order
- `order_time_hour`: Hour when order was placed
- `distance`: Distance in kilometers
- `time_taken`: Target variable (delivery time in minutes)

## Limitations & Future Improvements

### Current Limitations
- Requires pre-trained model (`Deployment.pkl`) to be available
- Model performance depends on dataset quality and representativeness
- No real-time data updates; uses static historical data

### Suggested Improvements
- Implement model retraining pipeline for continuous learning
- Add data visualization for feature importance
- Include confidence intervals with predictions
- Integrate real-time traffic and weather APIs
- Add user authentication and delivery history tracking
- Deploy on cloud platforms (Heroku, AWS, Azure)
- Create mobile-friendly interface

## File Descriptions

### `app.py`
Main application file containing the Streamlit interface, user input handling, and prediction logic.

### `swiggy_cleaned.csv`
Dataset containing historical delivery information used for model training and feature extraction.

### `Deployment.pkl`
Serialized Random Forest model trained on delivery data, loaded during runtime for predictions.

### `Swiggy_Delivery_Time_Prediction.ipynb`
Jupyter notebook containing the complete model development process, including:
- Data loading and exploration
- Feature engineering and preprocessing
- Model training and evaluation
- Model serialization for deployment

#### Using Google Colab
1. **Open the Notebook in Google Colab**:
   - Visit [Google Colab](https://colab.research.google.com)
   - Go to File → Upload Notebook
   - Upload the `Swiggy_Delivery_Time_Prediction.ipynb` file

2. **Upload the Dataset**:
   ```python
   from google.colab import files
   uploaded = files.upload()  # Select swiggy_cleaned.csv when prompted
   ```
   Or mount your Google Drive if the dataset is stored there:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. **Install Required Dependencies**:
   ```python
   !pip install pandas numpy scikit-learn seaborn matplotlib
   ```

4. **Runtime Configuration**:
   - Go to Runtime → Change runtime type
   - Select "Python 3" and "GPU" or "CPU" as needed
   - Click "Save"

5. **Run the Notebook**:
   - Use Runtime → Run all to execute all cells
   - Or run cells individually using Shift+Enter
   - Monitor the execution status in the top-right corner

6. **Download Generated Files**:
   ```python
   from google.colab import files
   files.download('Deployment.pkl')  
   ```

#### Using Jupyter Notebook/Lab Locally
1. Place the notebook and `swiggy_cleaned.csv` in the same directory
2. Launch Jupyter: `jupyter notebook` or `jupyter lab`
3. Open `Swiggy_Delivery_Time_Prediction.ipynb`
4. Run the cells sequentially to understand the model development process

The notebook will generate the `Deployment.pkl` file used by the Streamlit app.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError: swiggy.csv` | Ensure `swiggy.csv` is in the same directory as `app.py` |
| `FileNotFoundError: Deployment.pkl` | Ensure the trained model file is in the project root |
| Import errors | Run `pip install -r requirements.txt` to install all dependencies |
| Streamlit not found | Install Streamlit using `pip install streamlit` |

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Samyak S Sanjee / https://github.com/Samviksanjee?tab=overview&from=2025-10-01&to=2025-10-23

## Contact

For questions or suggestions, please reach out through:
- GitHub Issues
- Email: Samyak.s1264@gmail.com

## Acknowledgments

- Dataset inspired by Swiggy food delivery service
- Built with Streamlit for rapid prototyping
- Machine learning powered by scikit-learn

---

**Note**: This application is for educational and demonstration purposes. Actual delivery time predictions depend on many real-time factors not captured in this model.