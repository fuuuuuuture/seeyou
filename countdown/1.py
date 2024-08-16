from datetime import datetime

# 定义目标日期
target_date = datetime(2024, 9, 1)

# 获取当前时间
current_time = datetime.now()

# 计算时间差
time_difference = target_date - current_time

# 提取天、小时、分钟和秒
days = time_difference.days
total_seconds = time_difference.seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# 打印结果
print(f"距离2024年9月1日还有 {days} 天 {hours} 小时 {minutes} 分钟 {seconds} 秒")