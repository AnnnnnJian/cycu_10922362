from datetime import datetime

def analyze_date_time(date_time_str):
    """
    分析輸入的時間字串，完成以下任務：
    1. 回傳該日期為星期幾
    2. 回傳該日期是當年的第幾天
    3. 計算從該時刻至現在時間，共經過了幾個太陽日（以浮點表示）

    :param date_time_str: 時間字串，格式為 'YYYY-MM-DD HH:MM'
    :return: 包含結果的字典
    """
    # 將字串轉換為 datetime 對象
    input_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    
    # 1. 回傳該日期為星期幾
    weekday = input_time.strftime('%A')  # 英文星期幾，例如 'Monday'
    
    # 2. 回傳該日期是當年的第幾天
    day_of_year = input_time.timetuple().tm_yday
    
    # 3. 計算從該時刻至現在時間，共經過了幾個太陽日
    now = datetime.now()
    delta = now - input_time
    days_elapsed = delta.total_seconds() / (24 * 3600)  # 將秒數轉換為天數（浮點數）
    
    # 回傳結果
    return {
        'weekday': weekday,
        'day_of_year': day_of_year,
        'days_elapsed': days_elapsed
    }

# 接受使用者輸入
date_time_str = input("請輸入日期和時間 (格式為 'YYYY-MM-DD HH:MM'): ")
result = analyze_date_time(date_time_str)

# 輸出結果
print(f"星期幾: {result['weekday']}")
print(f"當年的第幾天: {result['day_of_year']}")
print(f"經過的太陽日: {result['days_elapsed']:.2f}")