# Load data (replace with actual file path or database connection)
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Data transformation function
def transform_data(data):
    # Assume the data has 'date' and 'demand' columns for demand forecasting
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    # Additional transformations, e.g., handling missing values
    data.fillna(method='ffill', inplace=True)
    return data
