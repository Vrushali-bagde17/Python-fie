# Simple optimization function to recommend safety stock and reorder points
def inventory_optimization(forecast, lead_time, service_level=0.95):
    demand_std = forecast.std()  # Standard deviation of demand forecast
    safety_stock = demand_std * lead_time * service_level
    reorder_point = forecast.mean() * lead_time + safety_stock
    return safety_stock, reorder_point
