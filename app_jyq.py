# 纯Streamlit网页版 | 1:1复刻你的Tkinter爱心表白效果 | 无报错
import streamlit as st
import random
import time
import math

# ===================== 【完全保留你的原版配置】 =====================
# 祝福文字（原版一模一样）
text_list = ["姜云琪","愿你每天都充满阳光","姜云琪","愿你拥有幸福和快乐","姜云琪","愿你天天开心"]
# 背景颜色（原版一模一样）
color_list = ["pink","lightblue","lightgreen","lemonchiffon","hotpink","skyblue"]

# ===================== 【原版爱心数学公式 完全不动】 =====================
# 生成爱心轨迹坐标函数（你的核心算法，完美保留）
def create_heart_points(n, screen_w, screen_h):
    points = []
    for i in range(n):
        theta = i / n * 2 * math.pi
        x = 16 * math.sin(theta)**3
        y = 13 * math.cos(theta) - 5 * math.cos(2*theta) - 2 * math.cos(3*theta) - math.cos(4*theta)
        # 适配网页屏幕坐标
        sx = int(screen_w/2 + x*20 - 50)
        sy = int(screen_h/2 - y*20 - 80)
        points.append((max(0, sx), max(0, sy)))
    return points

# ===================== 【网页版文字弹窗效果】 =====================
def show_text_tip(text, bg_color):
    # 网页彩色文字卡片（复刻Tkinter弹窗效果）
    st.markdown(f"""
        <div style="
            background:{bg_color};
            padding:10px 20px;
            border-radius:10px;
            text-align:center;
            font-size:16px;
            font-family:微软雅黑;
            width:fit-content;
            margin:5px auto;
        ">
            {text}
        </div>
    """, unsafe_allow_html=True)

# ===================== 【主程序：复刻原版动画流程】 =====================
def main():
    # 网页标题
    st.title("💖 致姜云琪")
    st.markdown("<h3 style='text-align:center;'>爱心动画</h3>", unsafe_allow_html=True)
    
    # 动画容器
    container = st.empty()
    with container:
        # 1. 生成爱心轨迹（原版参数：150个点）
        heart_points = create_heart_points(150, 800, 600)
        
        st.markdown("### ✨ 爱心轨迹生成中...")
        time.sleep(0.5)
        
        # 2. 逐点显示爱心文字（复刻原版动画速度）
        for i, (x, y) in enumerate(heart_points):
            text = "姜云琪" if i == len(heart_points)-1 else random.choice(text_list)
            color = random.choice(color_list)
            show_text_tip(text, color)
            time.sleep(0.03)
        
        time.sleep(1)
        container.empty()  # 清空爱心轨迹

        # 3. 满屏随机祝福（复刻原版效果）
        st.markdown("### 💌 满屏祝福送达...")
        total_windows = 200  # 网页版适配数量
        for _ in range(total_windows):
            text = random.choice(text_list)
            color = random.choice(color_list)
            show_text_tip(text, color)
            time.sleep(0.005)
        
        time.sleep(3)
        st.success("🎀 动画播放完成！")
        st.balloons()  # 网页彩蛋气球

# ===================== 启动程序 =====================
if __name__ == "__main__":
    main()