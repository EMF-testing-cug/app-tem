from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from core_logic import am_to_microtesla, calculate_tem_field

class CalibDemoUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        self.add_widget(Label(text="[ 电磁校准简易控制面板 Demo ]", font_size='20sp', size_hint_y=0.2))
        
        # 输入行
        input_box = BoxLayout(orientation='horizontal', size_hint_y=0.2)
        input_box.add_widget(Label(text="输入芯板电压 (V):", size_hint_x=0.4))
        self.voltage_input = TextInput(text="10.0", multiline=False, size_hint_x=0.6)
        self.add_widget(input_box)
        
        # 结果显示标签
        self.result_label = Label(text="等待计算...", font_size='16sp', size_hint_y=0.3)
        self.add_widget(self.result_label)
        
        # 计算触发按钮
        self.calc_btn = Button(text="计算标准场强与换算", size_hint_y=0.3)
        self.calc_btn.bind(on_press=self.on_calculate)
        self.add_widget(self.calc_btn)

    def on_calculate(self, instance):
        try:
            val = float(self.voltage_input.text.strip())
            # 调用核心算法
            e_field = calculate_tem_field(voltage_v=val, septum_height_m=0.5)
            b_field = am_to_microtesla(val)
            self.result_label.text = f"计算结果:\n标准场强: {e_field} V/m\n等效磁感应: {b_field} uT"
        except Exception as e:
            self.result_label.text = f"输入错误: {str(e)}"

class EMFApp(App):
    def build(self):
        return CalibDemoUI()

if __name__ == '__main__':
    EMFApp().run()
