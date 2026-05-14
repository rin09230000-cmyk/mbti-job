import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 & 포켓몬 추천 ✨",
    page_icon="🎮",
    layout="centered"
)

st.title("✨ MBTI 진로 & 포켓몬 추천")
st.write("너의 MBTI를 선택하면 어울리는 진로와 닮은 포켓몬을 알려줄게! 😆")

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "careers": [
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
        "pokemon": {
            "name": "뮤츠 🧬",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
            "desc": "차갑고 똑똑한 전략가 타입! 혼자 생각하는 걸 좋아하고 목표를 향해 끝까지 가는 성격 😎"
        }
    },

    "INTP": {
        "careers": [
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
        "pokemon": {
            "name": "후딘 🔮",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
            "desc": "IQ 높은 천재 포켓몬! 생각 많고 분석 좋아하는 INTP랑 찰떡 🤓"
        }
    },

    "ENTJ": {
        "careers": [
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
        "pokemon": {
            "name": "리자몽 🔥",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
            "desc": "카리스마 넘치는 리더 느낌! 강한 승부욕과 자신감이 특징 😤"
        }
    },

    "ENTP": {
        "careers": [
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
        "pokemon": {
            "name": "팬텀 👻",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
            "desc": "장난기 많고 독특한 매력의 포켓몬! 자유로운 ENTP 느낌 그 자체 😆"
        }
    },

    "INFJ": {
        "careers": [
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
        "pokemon": {
            "name": "루기아 🌊",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
            "desc": "신비롭고 깊은 분위기의 포켓몬! 조용하지만 강한 내면을 가진 타입 ✨"
        }
    },

    "INFP": {
        "careers": [
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
        "pokemon": {
            "name": "이브이 🌈",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
            "desc": "가능성이 무한한 포켓몬! 감성 풍부하고 따뜻한 INFP와 잘 어울려 🥺"
        }
    },

    "ENFJ": {
        "careers": [
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
        "pokemon": {
            "name": "피카츄 ⚡",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "desc": "친화력 최고! 밝은 에너지로 주변 사람들을 행복하게 만드는 타입 😄"
        }
    },

    "ENFP": {
        "careers": [
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
        "pokemon": {
            "name": "파이리 🔥",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
            "desc": "열정 넘치고 귀여운 분위기! 새로운 도전을 좋아하는 ENFP 느낌 🔥"
        }
    },

    "ISTJ": {
        "careers": [
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
        "pokemon": {
            "name": "거북왕 💧",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
            "desc": "든든하고 믿음직한 타입! 책임감 강한 ISTJ랑 찰떡 👍"
        }
    },

    "ISFJ": {
        "careers": [
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
        "pokemon": {
            "name": "해피너스 💕",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
            "desc": "상냥하고 치유해주는 느낌의 포켓몬! 따뜻한 ISFJ와 잘 어울려 😊"
        }
    },

    "ESTJ": {
        "careers": [
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
        "pokemon": {
            "name": "보만다 🐉",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/373.png",
            "desc": "강하고 듬직한 리더 느낌! 목표를 향해 돌진하는 타입 😤"
        }
    },

    "ESFJ": {
        "careers": [
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
        "pokemon": {
            "name": "푸린 🎤",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
            "desc": "사람들에게 행복을 주는 귀여운 분위기! 인기 많은 ESFJ 느낌 💖"
        }
    },

    "ISTP": {
        "careers": [
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
        "pokemon": {
            "name": "루카리오 👊",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
            "desc": "쿨하고 실전 능력 뛰어난 타입! 조용하지만 강한 ISTP 느낌 😎"
        }
    },

    "ISFP": {
        "careers": [
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
        "pokemon": {
            "name": "세레비 🌿",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/251.png",
            "desc": "감성적이고 자연을 사랑하는 분위기! 순수한 ISFP 느낌 🍀"
        }
    },

    "ESTP": {
        "careers": [
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
        "pokemon": {
            "name": "괴력몬 💪",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
            "desc": "에너지 넘치고 행동력 최고! 몸으로 부딪히는 ESTP 스타일 🔥"
        }
    },

    "ESFP": {
        "careers": [
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
        ],
        "pokemon": {
            "name": "냐오닉스 🎭",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/678.png",
            "desc": "매력 넘치고 분위기 메이커 느낌! 사람들 시선 끄는 걸 잘해 😆"
        }
    }
}

# MBTI 선택
mbti = st.selectbox(
    "🧠 너의 MBTI를 선택해줘!",
    list(mbti_data.keys())
)

# 버튼
if st.button("✨ 결과 보기"):
    data = mbti_data[mbti]

    st.header(f"💼 {mbti} 유형 추천 진로")

    for info in data["careers"]:
        st.subheader(info["career"])
        st.write(f"🎓 추천 학과 : {info['major']}")
        st.write(f"😆 잘 어울리는 성격 : {info['personality']}")
        st.divider()

    # 포켓몬 추천
    st.header("🎮 너와 닮은 포켓몬")

    st.image(data["pokemon"]["image"], width=180)

    st.subheader(data["pokemon"]["name"])
    st.write(data["pokemon"]["desc"])

    st.success("🌈 결과는 재미로 보는 거지만, 진짜 중요한 건 네가 좋아하는 걸 찾는 거야! 😎")
