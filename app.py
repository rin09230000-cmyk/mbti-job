import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 💼",
    page_icon="✨",
    layout="centered"
)

st.title("✨ MBTI 기반 진로 추천")
st.write("너의 MBTI를 선택하면 어울리는 진로를 추천해줄게! 😎")

# MBTI 데이터
career_data = {
    "INTJ": [
        {
            "career": "데이터 사이언티스트 📊",
            "major": "컴퓨터공학과, 데이터사이언스학과",
            "personality": "논리적이고 분석하는 걸 좋아하는 사람이 잘 어울려!"
        },
        {
            "career": "건축가 🏛️",
            "major": "건축학과",
            "personality": "창의적이면서 계획 세우는 걸 좋아하는 사람에게 추천!"
        }
    ],
    "INTP": [
        {
            "career": "프로그래머 💻",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 새로운 걸 탐구하는 사람에게 딱!"
        },
        {
            "career": "연구원 🔬",
            "major": "물리학과, 화학과",
            "personality": "깊게 생각하고 실험하는 걸 좋아하는 사람이 잘 맞아!"
        }
    ],
    "ENTJ": [
        {
            "career": "CEO 🏢",
            "major": "경영학과",
            "personality": "리더십 있고 추진력 강한 사람이 잘 어울려!"
        },
        {
            "career": "변호사 ⚖️",
            "major": "법학과",
            "personality": "논리적으로 말 잘하고 목표의식 강한 사람 추천!"
        }
    ],
    "ENTP": [
        {
            "career": "마케터 📢",
            "major": "광고홍보학과",
            "personality": "아이디어 많고 사람들과 소통 좋아하는 사람에게 추천!"
        },
        {
            "career": "유튜버 🎥",
            "major": "미디어학과",
            "personality": "재밌고 창의적인 걸 좋아하는 사람에게 잘 맞아!"
        }
    ],
    "INFJ": [
        {
            "career": "상담사 💖",
            "major": "심리학과",
            "personality": "공감 능력 좋고 남을 도와주는 걸 좋아하는 사람 추천!"
        },
        {
            "career": "작가 ✍️",
            "major": "문예창작과",
            "personality": "상상력이 풍부하고 감수성이 깊은 사람에게 딱!"
        }
    ],
    "INFP": [
        {
            "career": "일러스트레이터 🎨",
            "major": "시각디자인학과",
            "personality": "감성적이고 창의적인 사람에게 잘 어울려!"
        },
        {
            "career": "작곡가 🎵",
            "major": "실용음악과",
            "personality": "자기만의 감성과 표현력을 가진 사람 추천!"
        }
    ],
    "ENFJ": [
        {
            "career": "교사 🍎",
            "major": "교육학과",
            "personality": "사람 챙기는 걸 좋아하고 책임감 있는 사람에게 추천!"
        },
        {
            "career": "HR 매니저 🤝",
            "major": "경영학과",
            "personality": "소통 능력 좋고 사람을 이끄는 걸 잘하는 사람 추천!"
        }
    ],
    "ENFP": [
        {
            "career": "기획자 🌟",
            "major": "문화콘텐츠학과",
            "personality": "에너지 넘치고 아이디어 많은 사람에게 딱!"
        },
        {
            "career": "방송인 🎤",
            "major": "방송연예과",
            "personality": "사람들과 어울리는 걸 좋아하는 사람 추천!"
        }
    ],
    "ISTJ": [
        {
            "career": "공무원 🏛️",
            "major": "행정학과",
            "personality": "책임감 강하고 꼼꼼한 사람에게 잘 맞아!"
        },
        {
            "career": "회계사 📚",
            "major": "회계학과",
            "personality": "계획적이고 정확한 걸 좋아하는 사람 추천!"
        }
    ],
    "ISFJ": [
        {
            "career": "간호사 🩺",
            "major": "간호학과",
            "personality": "배려심 많고 성실한 사람에게 추천!"
        },
        {
            "career": "사회복지사 🤗",
            "major": "사회복지학과",
            "personality": "남을 돕는 데 보람을 느끼는 사람에게 잘 맞아!"
        }
    ],
    "ESTJ": [
        {
            "career": "경찰 👮",
            "major": "경찰행정학과",
            "personality": "원칙 중요하게 생각하고 리더십 있는 사람 추천!"
        },
        {
            "career": "관리자 📋",
            "major": "경영학과",
            "personality": "체계적으로 일하는 걸 좋아하는 사람에게 딱!"
        }
    ],
    "ESFJ": [
        {
            "career": "승무원 ✈️",
            "major": "항공서비스학과",
            "personality": "친절하고 사람들과 잘 어울리는 사람 추천!"
        },
        {
            "career": "유치원 교사 🧸",
            "major": "유아교육과",
            "personality": "다정하고 돌보는 걸 좋아하는 사람에게 잘 맞아!"
        }
    ],
    "ISTP": [
        {
            "career": "엔지니어 ⚙️",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하고 문제 해결 잘하는 사람 추천!"
        },
        {
            "career": "파일럿 🛫",
            "major": "항공운항학과",
            "personality": "침착하고 집중력 좋은 사람에게 잘 어울려!"
        }
    ],
    "ISFP": [
        {
            "career": "패션 디자이너 👗",
            "major": "패션디자인학과",
            "personality": "감각적이고 개성 표현 좋아하는 사람 추천!"
        },
        {
            "career": "플로리스트 🌸",
            "major": "원예학과",
            "personality": "섬세하고 아름다운 걸 좋아하는 사람에게 딱!"
        }
    ],
    "ESTP": [
        {
            "career": "운동선수 🏆",
            "major": "체육학과",
            "personality": "활동적이고 도전 좋아하는 사람 추천!"
        },
        {
            "career": "영업 전문가 💼",
            "major": "경영학과",
            "personality": "사람 만나는 걸 좋아하고 자신감 있는 사람에게 잘 맞아!"
        }
    ],
    "ESFP": [
        {
            "career": "배우 🎬",
            "major": "연극영화과",
            "personality": "끼 많고 밝은 에너지 가진 사람 추천!"
        },
        {
            "career": "이벤트 플래너 🎉",
            "major": "관광경영학과",
            "personality": "재밌는 분위기 만드는 걸 좋아하는 사람에게 딱!"
        }
    ]
}

# MBTI 선택
mbti = st.selectbox(
    "🧠 너의 MBTI를 선택해줘!",
    list(career_data.keys())
)

# 결과 출력
if st.button("✨ 진로 추천 받기"):
    st.subheader(f"💡 {mbti} 유형에게 추천하는 진로")

    for info in career_data[mbti]:
        st.markdown(f"## {info['career']}")
        st.write(f"🎓 추천 학과 : {info['major']}")
        st.write(f"😆 잘 어울리는 성격 : {info['personality']}")
        st.divider()

    st.success("🌈 미래는 아직 무궁무진해! 여러 분야를 경험해보면서 진짜 좋아하는 걸 찾아봐 😎")
