import numpy as np
from sklearn.metrics import mean_absolute_error

# 计算均方根误差
def Rmse(predictions, targets):
    return np.sqrt(np.mean((predictions - targets) ** 2))

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true))

# ==================================================================
# Faults：输入原始故障数据，一维，放大后的数据
# FitValue：输入拟合值，每个省一组，即共三组
# Len_One=6：每组数组的长度，可改为12  Zoom_factor=100：缩小倍数
#
# Mean_Rmse：返回每个省的RMSE值
# ==================================================================
def RMSE(Faults, FitValue, Len_One=6, Zoom_factor=1):
    Len_Faults = np.shape(Faults)
    Len_Fault = round(Len_Faults[0] / Len_One)  # round取整数，Len_Fault = 126/6 = 21

    Faults = Faults / Zoom_factor  # 还原数据
    FitValue = np.array(FitValue)
    FitValue = FitValue / Zoom_factor  # 还原数据

    Faults_Col = np.array([Faults[i * Len_One:(i + 1) * Len_One] for i in np.arange(Len_Fault)])  # 将输入数据排列好

    Mean_Rmse = {}
    Mean_MAE = {}
    Mean_MAPE = {}
    for i in np.arange(3):
        Rmse_Value = []
        MAE_Value = []
        MAPE_Value = []
        if i==0:
            for ip in np.arange(7):
                A = Rmse(Faults_Col[ip], FitValue[i])
                Rmse_Value = np.append(Rmse_Value, A)  # 计算每组的均方根误差
                B = mean_absolute_error(Faults_Col[ip], FitValue[i])
                MAE_Value = np.append(MAE_Value, B)  # 计算每组的均方根误差
                C = mean_absolute_percentage_error(Faults_Col[ip], FitValue[i])
                MAPE_Value = np.append(MAPE_Value, C)  # 计算每组的均方根误差
        if i==1:
            for ip in np.arange(11):
                A = Rmse(Faults_Col[ip+i*7], FitValue[i])
                Rmse_Value = np.append(Rmse_Value, A)  # 计算每组的均方根误差
                B = mean_absolute_error(Faults_Col[ip+i*7], FitValue[i])
                MAE_Value = np.append(MAE_Value, B)  # 计算每组的均方根误差
                C = mean_absolute_percentage_error(Faults_Col[ip+i*7], FitValue[i])
                MAPE_Value = np.append(MAPE_Value, C)  # 计算每组的均方根误差
        if i==2:
            for ip in range(7):
                A = Rmse(Faults_Col[ip + 18], FitValue[i])
                Rmse_Value = np.append(Rmse_Value, A)
                B = mean_absolute_error(Faults_Col[ip + 18], FitValue[i])
                MAE_Value = np.append(MAE_Value, B)  # 计算每组的均方根误差
                C = mean_absolute_percentage_error(Faults_Col[ip + 18], FitValue[i])
                MAPE_Value = np.append(MAPE_Value, C) # 计算每组的均方根误差
        Mean_Rmse[i] = Rmse_Value.mean(axis=0)  # 计算每省的均方根误差
        Mean_MAE[i] = MAE_Value.mean(axis=0)  # 计算每省的均方根误差
        Mean_MAPE[i] = MAPE_Value.mean(axis=0)  # 计算每省的均方根误差
    # print(Mean_Rmse)
    print('Rmse Mean is A、B、C :')
    return Mean_Rmse, Mean_MAE, Mean_MAPE


# Rmse_all = RMSE_computer(elec_faults, Mean_output, Len_One=6, Zoom_factor=100)
# print(Rmse_all)





# ==================================================================
# Faults：输入第7年原始故障数据，一维3*7=21个，放大后的数据
# FitValue：输入拟合值，每个省1个，即共3个
# Len_One=7：每省数组的长度， Zoom_factor=100：缩小倍数
#
# Mean_Rmse：返回每个省的RMSE值
# ==================================================================
def RMSEfor_Pred(Faults, FitValue, Len_One=7, Zoom_factor=100):
    Len_Faults = np.shape(Faults)
    Len_Fault = round(Len_Faults[0] / Len_One)  # round取整数，Len_Fault = 21/7 = 3

    Faults = Faults / Zoom_factor  # 还原数据
    FitValue = np.array(FitValue)
    FitValue = FitValue / Zoom_factor  # 还原数据

    Faults_Col = np.array([Faults[i * Len_One:(i + 1) * Len_One] for i in np.arange(Len_Fault)])  # 将输入数据排列好

    Mean_Rmse = {}
    for i in np.arange(3):
        A = Rmse(Faults_Col[i], FitValue[i])  # 计算每组的均方根误差
        # print(Rmse_Value)
        Mean_Rmse[i] = A   # 计算每省的均方根误差
    # print(Mean_Rmse)
    print('Rmse Mean is A、B、C :')
    return Mean_Rmse










# 计算均方误差
def Mse(predictions, targets):
    return np.mean((predictions - targets) ** 2)


# ==================================================================
# Faults：输入原始故障数据，一维，放大后的数据
# FitValue：输入拟合值，每个省一组，即共三组
# Len_One=6：每组数组的长度，可改为12  Zoom_factor=100：缩小倍数
#
# Mean_Mse：返回每个省的RMSE值
# ==================================================================
def MSE(Faults, FitValue, Len_One=6, Zoom_factor=1):
    Len_Faults = np.shape(Faults)
    Len_Fault = round(Len_Faults[0] / Len_One)  # round取整数，Len_Fault = 126/6 = 21

    Faults = Faults / Zoom_factor  # 还原数据
    FitValue = np.array(FitValue)
    FitValue = FitValue / Zoom_factor  # 还原数据

    Faults_Col = np.array([Faults[i * Len_One:(i + 1) * Len_One] for i in np.arange(Len_Fault)])  # 将输入数据排列好

    Rmse_Value = []
    Mean_Mse = {}
    for i in np.arange(3):
        Rmse_Value = []
        for ip in np.arange(7):
            A = Mse(Faults_Col[ip], FitValue[i])
            Rmse_Value = np.append(Rmse_Value, A)  # 计算每组的均方根误差
        # print(Rmse_Value)
        Mean_Mse[i] = Rmse_Value.mean(axis=0)  # 计算每省的均方根误差
    # print(Mean_Rmse)
    print('Mse Mean is A、B、C :')
    return Mean_Mse