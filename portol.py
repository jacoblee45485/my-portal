import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="Giant Foodsystem 통합 포털", page_icon="🏢", layout="centered")

# =====================================================================
# 🎨 1. 맞춤형 히어로 배너 (회사 배경 이미지 및 로고 디자인)
# =====================================================================
# 너무 어둡지 않게 필터(투명도 0.4~0.5)를 조절하고, 상자 크기를 세련되게 줄였습니다.
hero_banner = """
<div style="
    background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1586528116311-ad8ed7c80a71?q=80&w=2070&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    padding: 40px 20px; 
    border-radius: 12px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
">
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 10px;">
        <!-- 회사 공식 도메인 아이콘 -->
        <img src="https://logo.clearbit.com/giantfoodusa.com" onerror="this.style.display='none'" style="height: 45px; border-radius: 8px; margin-right: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        <h1 style="font-size: 2.8rem; margin: 0; font-weight: 800; letter-spacing: -1px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            <span style="color: #FF3333;">GIANT</span> <span style="color: #FFFFFF;">FOODSYSTEM</span>
        </h1>
    </div>
    <p style="font-size: 1.1rem; margin-top: 0; font-weight: 400; color: #F1F5F9; text-shadow: 1px 1px 3px rgba(0,0,0,0.4);">#1 K-Food Distributor in USA · 사내 통합 관리 포털</p>
</div>
"""
st.markdown(hero_banner, unsafe_allow_html=True)

# =====================================================================
# 📌 2. 메인 메뉴판 영역
# =====================================================================
st.markdown("<h4 style='text-align: center; color: #475569; margin-bottom: 30px;'>원하시는 업무 시스템을 선택해 주세요</h4>", unsafe_allow_html=True)

# 2칸으로 나누어서 메뉴판 만들기
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚚 물류 및 차량 관리")
    st.info("트럭, 트레일러, 장비 현황 및 사고/티켓 내역을 관리하는 핵심 대시보드입니다.")
    
    # 트럭 대시보드 실제 인터넷 주소(URL)
    TRUCK_APP_URL = "https://my-truck-dashboard-rwtytrjvzqzzdcnzlhn2j3.streamlit.app" 
    
    st.link_button("👉 트럭 관리 시스템 접속", TRUCK_APP_URL, use_container_width=True)

with col2:
    st.markdown("### 👨‍💼 인사 및 근태 관리 (준비중)")
    st.success("드라이버 및 직원 정보, 급여 내역을 관리하는 대시보드입니다.")
    
    # 나중에 다른 앱을 만드시면 이곳에 주소를 넣으시면 됩니다.
    HR_APP_URL = "https://giantfoodusa.com" 
    
    st.link_button("👉 인사 관리 시스템 접속", HR_APP_URL, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# 추가 메뉴 (아래에 한 줄 더 만들기)
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 💰 재무 및 영수증 (준비중)")
    st.warning("주유비, 톨게이트 비용 등 각종 지출 내역을 관리합니다.")
    FINANCE_APP_URL = "https://giantfoodusa.com"
    st.link_button("👉 재무 관리 시스템 접속", FINANCE_APP_URL, use_container_width=True)

with col4:
    st.markdown("### 📝 회사 공식 홈페이지")
    st.error("Giant Foodsystem의 제품, 브랜드 및 공식 안내를 확인합니다.")
    NOTICE_APP_URL = "https://giantfoodusa.com"
    st.link_button("👉 공식 홈페이지 바로가기", NOTICE_APP_URL, use_container_width=True)

# =====================================================================
# 💡 하단 안내 문구
# =====================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 0.9rem;">
    &copy; 2026 Giant Foodsystem Inc. All rights reserved. <br>
    본 시스템은 임직원 전용 데이터 관리 플랫폼입니다.
</div>
""", unsafe_allow_html=True)
