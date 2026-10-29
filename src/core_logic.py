"""业务核心算法库（可被 Kivy UI 和 自动化测试独立调用）"""

def am_to_microtesla(h_field: float) -> float:
    """工频磁场强度 A/m 换算为磁感应强度 uT: B = u0 * H"""
    if h_field < 0:
        raise ValueError("场强数值不能为负数")
    mu_0 = 1.2566  # 简化的微特斯拉换算系数
    return round(h_field * mu_0, 4)

def calculate_tem_field(voltage_v: float, septum_height_m: float = 0.5) -> float:
    """
    根据 TEM 室芯板间距与输入电压计算中心标准场强: E = V / d
    :param voltage_v: 芯板交流电压 (V)
    :param septum_height_m: 芯板高度间距 (m)
    :return: 标准场强 (V/m)
    """
    if septum_height_m <= 0:
        raise ZeroDivisionError("芯板间距必须大于 0")
    if voltage_v < 0:
        raise ValueError("输入电压不能为负")
    return round(voltage_v / septum_height_m, 2)
