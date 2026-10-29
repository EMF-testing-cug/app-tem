import pytest
from src.core_logic import am_to_microtesla, calculate_tem_field

def test_am_to_microtesla_normal():
    # 正常值换算测试
    result = am_to_microtesla(10.0)
    assert result == 12.566

def test_am_to_microtesla_negative():
    # 异常输入报错测试
    with pytest.raises(ValueError):
        am_to_microtesla(-5.0)

def test_calculate_tem_field():
    # 10V 电压，0.5m 间距，场强应为 20.0 V/m
    assert calculate_tem_field(10.0, 0.5) == 20.0
