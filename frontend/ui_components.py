# UI 컴포넌트 모듈
import streamlit as st


def setup_page_config():
    # 페이지 설정
    st.set_page_config(
        page_title="AI 상담 프로토타입",
        page_icon="💬",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def render_sidebar():
    # 사이드바 - 상담 단계 표시
    st.sidebar.title("📋 상담 단계")
    
    # 현재 단계 정보 가져오기
    from .chat_handler import get_current_stage_info
    stage_info = get_current_stage_info()
    
    stages = [
        ("1.초기 접수 (Intake)", "증상과 감정을 수집합니다", "#2E5C8A"),
        ("2.가설 생성 (Hypothesis Generation)", "관련 질환을 검색 중입니다", "#2D8659"),
        ("3.진단 검증 (Validation)", "질환을 감별하고 확정합니다", "#CC6F35"),
        ("4.솔루션 및 요약 (Solution & Summary)", "최종 요약과 행동 계획을 제시합니다", "#7D3C98")
    ]
    current_stage = stage_info["stage"] if stage_info else 1
    
    for idx, (name, desc, name_color) in enumerate(stages, 1):
        if idx == current_stage:
            # 현재 단계는 글씨체를 키워서 강조하고 색상 적용
            st.sidebar.markdown(
                f'<p style="font-weight: bold; font-size: 1.2em; color: {name_color}; margin-bottom: 5px;">{name}</p>',
                unsafe_allow_html=True
            )
            st.sidebar.markdown(f"   <span style='color: #666;'>{desc}</span>", unsafe_allow_html=True)
        elif idx < current_stage:
            # 완료된 단계는 회색 처리
            st.sidebar.markdown(
                f'<p style="font-weight: bold; color: #999; margin-bottom: 5px;">{name}</p>',
                unsafe_allow_html=True
            )
        else:
            # 아직 진행하지 않은 단계는 회색 처리
            st.sidebar.markdown(
                f'<p style="font-weight: bold; color: #999; margin-bottom: 5px;">{name}</p>',
                unsafe_allow_html=True
            )
            st.sidebar.markdown(f"   <span style='color: #999;'>{desc}</span>", unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # 초기화(개발,테스트용) 버튼 (개발/테스트용)
    if st.sidebar.button("초기화(개발,테스트용)"):
        if "stage_handler" in st.session_state:
            st.session_state.stage_handler.reset_stage()
            st.session_state.messages = []
            st.rerun()


def render_main_header():
    # 메인 헤더 표시
    st.title("💬 AI 정신건강 상담 도우미")
    st.markdown("---")


def render_chat_messages(messages):
    # 채팅 메시지들을 화면에 표시
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def render_user_input():
    # 사용자 입력창 표시
    return st.chat_input("지금 어떤 기분이신가요?")


def render_assistant_response(response):
    # AI 응답을 화면에 표시
    with st.chat_message("assistant"):
        st.markdown(response)

