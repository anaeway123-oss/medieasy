import streamlit as st

st.set_page_config(
    page_title="MediEasy",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

TERMS = [
    {
        "term": "hypertension",
        "kr": "고혈압",
        "category": "질환",
        "tags": ["혈압", "심장", "생활관리"],
        "easy": "혈압이 정상보다 높은 상태예요.",
        "plain": "혈관 안의 압력이 계속 높아서 심장과 혈관에 부담이 갈 수 있어요.",
        "doctor": "혈압이 높습니다. 꾸준한 관리가 필요합니다.",
        "when": "건강검진, 내과 진료, 혈압 측정 후 자주 듣는 말이에요.",
        "care": ["짜게 먹는 습관 줄이기", "하루 30분 가볍게 걷기", "혈압을 정기적으로 기록하기"],
        "warning": "가슴 통증, 심한 두통, 숨참, 어지러움이 심하면 진료가 필요해요."
    },
    {
        "term": "diabetes mellitus",
        "kr": "당뇨병",
        "category": "질환",
        "tags": ["혈당", "내분비", "생활관리"],
        "easy": "혈액 속 당이 정상보다 높게 유지되는 질환이에요.",
        "plain": "몸이 혈당을 잘 조절하지 못해서 피 속에 당이 많아진 상태예요.",
        "doctor": "혈당 관리가 필요합니다.",
        "when": "건강검진에서 공복혈당이나 당화혈색소가 높을 때 자주 들을 수 있어요.",
        "care": ["단 음료 줄이기", "규칙적으로 식사하기", "식후 가볍게 걷기"],
        "warning": "심한 갈증, 잦은 소변, 갑작스러운 체중 감소가 있으면 확인이 필요해요."
    },
    {
        "term": "hyperlipidemia",
        "kr": "고지혈증",
        "category": "검사/질환",
        "tags": ["콜레스테롤", "중성지방", "혈관"],
        "easy": "혈액 속 지방 성분이 정상보다 높은 상태예요.",
        "plain": "쉽게 말하면 혈관 속에 기름기가 많아진 상태예요.",
        "doctor": "콜레스테롤이나 중성지방 수치가 높습니다.",
        "when": "건강검진에서 콜레스테롤, LDL, 중성지방 수치가 높을 때 들을 수 있어요.",
        "care": ["기름진 음식 줄이기", "꾸준히 걷기", "금연하기"],
        "warning": "대부분 증상이 없어서 건강검진으로 확인하는 경우가 많아요."
    },
    {
        "term": "myocardial infarction",
        "kr": "심근경색",
        "category": "응급/질환",
        "tags": ["심장", "응급", "가슴통증"],
        "easy": "심장 근육에 피가 잘 가지 않아 심장 조직이 손상되는 응급 질환이에요.",
        "plain": "심장으로 가는 혈관이 막혀 심장이 위험해진 상태예요.",
        "doctor": "심근경색이 의심됩니다. 빠른 치료가 필요합니다.",
        "when": "가슴 통증, 식은땀, 숨참이 있을 때 응급실에서 들을 수 있는 말이에요.",
        "care": ["가슴 통증을 가볍게 넘기지 않기", "흡연 줄이기", "혈압·혈당·콜레스테롤 관리하기"],
        "warning": "가슴 통증, 식은땀, 왼팔 통증, 숨참이 있으면 즉시 119가 필요할 수 있어요."
    },
    {
        "term": "hypoglycemia",
        "kr": "저혈당",
        "category": "증상/상태",
        "tags": ["혈당", "어지러움", "당뇨"],
        "easy": "혈당이 너무 낮아진 상태예요.",
        "plain": "몸에 필요한 당 에너지가 부족해져서 손떨림, 식은땀, 어지러움이 생길 수 있어요.",
        "doctor": "혈당이 낮습니다. 당 보충이 필요할 수 있습니다.",
        "when": "당뇨약을 복용하거나 식사를 거른 뒤 어지러울 때 들을 수 있어요.",
        "care": ["식사를 거르지 않기", "증상이 있으면 휴식하기", "사탕이나 주스 준비하기"],
        "warning": "의식이 흐려지거나 쓰러질 것 같으면 즉시 도움을 요청하세요."
    },
    {
        "term": "gastroenteritis",
        "kr": "위장염",
        "category": "질환",
        "tags": ["복통", "설사", "소화기"],
        "easy": "위와 장에 염증이 생긴 상태예요.",
        "plain": "배 속 소화기관이 자극받고 탈이 난 상태예요.",
        "doctor": "위장염 증상으로 보입니다.",
        "when": "설사, 복통, 구토로 병원에 갔을 때 자주 듣는 말이에요.",
        "care": ["수분 섭취하기", "기름진 음식 피하기", "증상이 심하면 진료받기"],
        "warning": "피 섞인 설사, 심한 탈수, 고열이 있으면 진료가 필요해요."
    },
    {
        "term": "anemia",
        "kr": "빈혈",
        "category": "검사/상태",
        "tags": ["혈액", "어지러움", "피로"],
        "easy": "몸에 산소를 나르는 혈액 성분이 부족한 상태예요.",
        "plain": "피가 산소를 충분히 실어 나르지 못해 쉽게 피곤하고 어지러울 수 있어요.",
        "doctor": "빈혈 수치가 있습니다.",
        "when": "혈액검사에서 헤모글로빈 수치가 낮을 때 들을 수 있어요.",
        "care": ["철분이 풍부한 음식 챙기기", "피로와 어지러움 기록하기", "원인 확인을 위해 진료받기"],
        "warning": "숨참, 심한 어지러움, 검은 변이 있으면 진료가 필요해요."
    },
    {
        "term": "pneumonia",
        "kr": "폐렴",
        "category": "질환",
        "tags": ["폐", "기침", "열"],
        "easy": "폐에 염증이 생긴 질환이에요.",
        "plain": "숨 쉬는 기관인 폐에 감염이나 염증이 생겨 기침, 열, 가래가 생길 수 있어요.",
        "doctor": "폐렴이 의심됩니다.",
        "when": "기침, 열, 가래, 숨참으로 진료받을 때 들을 수 있어요.",
        "care": ["충분한 휴식", "수분 섭취", "처방받은 약 잘 복용하기"],
        "warning": "숨이 차거나 고열이 지속되면 빠르게 진료받는 것이 좋아요."
    },
]

TESTS = [
    {
        "name": "LDL",
        "kr": "나쁜 콜레스테롤",
        "easy": "혈관에 쌓이기 쉬운 콜레스테롤이에요.",
        "high": "높으면 혈관 건강에 부담이 될 수 있어요.",
        "tip": "기름진 음식 줄이기, 걷기, 금연이 도움이 될 수 있어요."
    },
    {
        "name": "HDL",
        "kr": "좋은 콜레스테롤",
        "easy": "혈관 속 남는 콜레스테롤을 치우는 데 도움을 주는 성분이에요.",
        "high": "너무 낮으면 혈관 건강 관리가 필요할 수 있어요.",
        "tip": "규칙적인 운동과 금연이 도움이 될 수 있어요."
    },
    {
        "name": "Triglyceride",
        "kr": "중성지방",
        "easy": "혈액 속 지방의 한 종류예요.",
        "high": "높으면 대사 건강과 혈관 건강에 영향을 줄 수 있어요.",
        "tip": "단 음료, 과식, 음주를 줄이는 것이 도움이 될 수 있어요."
    },
    {
        "name": "HbA1c",
        "kr": "당화혈색소",
        "easy": "최근 2~3개월간의 평균 혈당 상태를 보여주는 검사예요.",
        "high": "높으면 혈당 조절이 잘 안 되고 있을 수 있어요.",
        "tip": "식사, 운동, 약물 복용을 꾸준히 관리하는 것이 중요해요."
    },
]

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;800;900&display=swap');

* {font-family: 'Noto Sans KR', sans-serif;}

.stApp {
    background:
    radial-gradient(circle at top left, rgba(56,189,248,.22), transparent 35%),
    radial-gradient(circle at bottom right, rgba(99,102,241,.12), transparent 30%),
    linear-gradient(135deg, #f0f9ff 0%, #f8fbff 45%, #ffffff 100%);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #1e293b);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.block-container {
    padding-top: 2.2rem;
    max-width: 1200px;
}

.hero {
    padding: 54px 48px;
    border-radius: 36px;
    background: linear-gradient(135deg, #0284c7 0%, #2563eb 52%, #4f46e5 100%);
    color: white;
    box-shadow: 0 26px 70px rgba(37, 99, 235, .25);
    margin-bottom: 28px;
}

.hero h1 {
    font-size: 60px;
    margin: 0 0 14px 0;
    font-weight: 900;
    letter-spacing: -1.8px;
}

.hero p {
    font-size: 22px;
    opacity: .96;
    margin: 0;
    line-height: 1.7;
}

.search-card {
    background: rgba(255,255,255,.96);
    border: 1px solid rgba(14,165,233,.18);
    border-radius: 30px;
    padding: 28px;
    box-shadow: 0 18px 48px rgba(15,23,42,.09);
    margin-bottom: 24px;
}

.card {
    background: rgba(255,255,255,.96);
    border: 1px solid rgba(14,165,233,.15);
    padding: 28px;
    border-radius: 30px;
    box-shadow: 0 16px 42px rgba(15,23,42,.08);
    margin-bottom: 20px;
}

.feature {
    text-align:center;
    padding:28px 20px;
    border-radius:28px;
    background:white;
    box-shadow:0 14px 34px rgba(15,23,42,.08);
    border: 1px solid rgba(14,165,233,.12);
    min-height: 150px;
}

.feature .icon {
    font-size: 32px;
}

.feature b {
    display:block;
    font-size:28px;
    color:#2563eb;
    margin-top: 10px;
}

.feature span {
    color:#475569;
    font-size:16px;
}

.term-title {
    font-size: 38px;
    font-weight: 900;
    color: #0f172a;
    letter-spacing: -1px;
}

.kr-title {
    font-size: 28px;
    font-weight: 900;
    color: #2563eb;
    margin-bottom: 14px;
}

.badge {
    display:inline-block;
    padding: 7px 14px;
    border-radius:999px;
    background:#dbeafe;
    color:#1d4ed8;
    font-weight:800;
    font-size:13px;
    margin-right:7px;
}

.tag {
    display:inline-block;
    padding: 7px 13px;
    border-radius:999px;
    background:#ecfeff;
    color:#155e75;
    font-weight:800;
    font-size:13px;
    margin-right:7px;
    margin-top: 5px;
}

.blue-box {
    padding: 23px;
    border-radius: 24px;
    background: linear-gradient(135deg, #eff6ff, #ffffff);
    border: 1px solid #bfdbfe;
    margin: 18px 0;
    font-size: 18px;
    line-height: 1.8;
}

.orange-box {
    padding: 20px;
    border-radius: 22px;
    background: #fff7ed;
    border: 1px solid #fed7aa;
    color: #9a3412;
    font-weight: 700;
    margin: 16px 0;
}

.green-box {
    padding: 20px;
    border-radius: 22px;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    color: #166534;
    margin: 16px 0;
}

.popular {
    text-align:center;
    padding:26px;
    border-radius:26px;
    background:white;
    box-shadow:0 14px 34px rgba(15,23,42,.07);
    border:1px solid rgba(14,165,233,.12);
}

.popular b {
    color:#2563eb;
    font-size:28px;
}

.small {
    color:#64748b;
    font-size:15px;
}

.footer {
    text-align:center;
    color:#64748b;
    padding: 30px 0 10px 0;
    font-size: 14px;
}

</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.sidebar.title("🩺 MediEasy")
st.sidebar.caption("병원 말을 쉬운 말로")
page = st.sidebar.radio(
    "메뉴",
    ["홈", "의학용어 검색", "병원 말 번역기", "검사결과 쉽게 보기", "즐겨찾기"]
)
st.sidebar.markdown("---")
st.sidebar.info("의학정보 이해를 돕는 서비스입니다. 진단과 치료 결정은 의료진과 상담하세요.")

def find_terms(keyword):
    if not keyword:
        return TERMS
    k = keyword.lower().strip()
    return [
        t for t in TERMS
        if k in t["term"].lower()
        or k in t["kr"]
        or k in t["easy"]
        or k in t["plain"]
        or any(k in tag for tag in t["tags"])
    ]

def show_term(t):
    st.markdown(f"""
    <div class="card">
        <span class="badge">{t['category']}</span>
        <div style="margin-top:12px;">
            {" ".join([f"<span class='tag'>#{tag}</span>" for tag in t["tags"]])}
        </div>
        <div class="term-title">{t['term']}</div>
        <div class="kr-title">{t['kr']}</div>

        <div class="blue-box">
            <b>💙 쉬운 설명</b><br>
            {t['easy']}<br>
            {t['plain']}
        </div>

        <p><b>👨‍⚕️ 병원에서는 이렇게 말할 수 있어요</b><br>
        “{t['doctor']}”</p>

        <p><b>🏥 언제 듣는 말인가요?</b><br>
        {t['when']}</p>

        <div class="orange-box">
            ⚠️ {t['warning']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🌿 생활관리 힌트")
    for item in t["care"]:
        st.write("•", item)

    if st.button(f"⭐ 즐겨찾기 추가: {t['kr']}", key=f"fav_{t['term']}"):
        if t["term"] not in st.session_state.favorites:
            st.session_state.favorites.append(t["term"])
            st.success("즐겨찾기에 추가했어요.")
        else:
            st.info("이미 즐겨찾기에 있어요.")

def show_disclaimer():
    st.markdown("""
    <div class="orange-box">
    ⚠️ MediEasy는 의료진의 진단이나 치료를 대신하지 않습니다.
    증상이 있거나 치료 결정이 필요하면 반드시 의료진과 상담하세요.
    </div>
    """, unsafe_allow_html=True)

if page == "홈":
    st.markdown("""
    <div class="hero">
        <h1>🩺 MediEasy</h1>
        <p>병원에서 들은 어려운 의학용어를 누구나 쉽게 이해하도록 도와주는 의료용어 안내 서비스입니다.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="search-card">', unsafe_allow_html=True)
        st.subheader("🔍 지금 궁금한 병원 말을 검색해보세요")
        home_keyword = st.text_input(
            "검색어",
            placeholder="예: 고혈압, 고지혈증, LDL, 심근경색, diabetes",
            label_visibility="collapsed"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    if home_keyword:
        results = find_terms(home_keyword)
        st.markdown(f"### 검색 결과 {len(results)}개")
        if results:
            for t in results:
                show_term(t)
        else:
            st.warning("아직 등록되지 않은 용어예요. 다른 표현으로 검색해보세요.")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature"><div class="icon">🔍</div><b>의학용어 검색</b><span>어려운 병원 말을 쉬운 말로</span></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature"><div class="icon">🤖</div><b>병원 말 번역기</b><span>문장을 생활 언어로 풀어보기</span></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature"><div class="icon">🧾</div><b>검사결과 이해</b><span>검사항목을 쉽게 설명</span></div>', unsafe_allow_html=True)

    st.markdown("### 🔥 사람들이 많이 찾는 용어")
    cols = st.columns(4)
    popular_words = ["고혈압", "당뇨병", "고지혈증", "심근경색"]
    for i, word in enumerate(popular_words):
        with cols[i]:
            st.markdown(f"<div class='popular'><b>{word}</b><br><span class='small'>쉬운 설명 보기</span></div>", unsafe_allow_html=True)

    st.markdown("### 🌱 오늘의 건강 문장")
    st.markdown("""
    <div class="green-box">
    건강검진 결과표에 모르는 단어가 있어도 괜찮아요.  
    단어 하나씩 쉬운 말로 풀어보면 내 몸 상태를 더 잘 이해할 수 있어요.
    </div>
    """, unsafe_allow_html=True)

    show_disclaimer()

elif page == "의학용어 검색":
    st.title("🔍 의학용어 검색")
    keyword = st.text_input("궁금한 용어를 입력하세요", placeholder="예: 고혈압, hyperlipidemia, 콜레스테롤, 폐렴")
    category = st.selectbox("분류", ["전체"] + sorted(list(set([t["category"] for t in TERMS]))))

    results = find_terms(keyword)

    if category != "전체":
        results = [t for t in results if t["category"] == category]

    st.caption(f"검색 결과: {len(results)}개")

    if not results:
        st.warning("검색 결과가 없어요. 다른 단어로 검색해보세요.")
    else:
        for t in results:
            show_term(t)
            st.divider()

    show_disclaimer()

elif page == "병원 말 번역기":
    st.title("🤖 병원 말 번역기")
    st.caption("의사가 한 말, 검사결과 설명, 진료 메모를 붙여넣으면 쉬운 말로 풀어주는 데모 기능입니다.")

    user_text = st.text_area(
        "병원에서 들은 말을 입력해보세요",
        placeholder="예: 콜레스테롤 수치가 높고 혈압도 높아서 생활습관 관리가 필요합니다.",
        height=170
    )

    if st.button("쉬운 말로 바꾸기", type="primary"):
        if not user_text.strip():
            st.warning("문장을 먼저 입력해주세요.")
        else:
            found = []
            for t in TERMS:
                if t["kr"] in user_text or t["term"].lower() in user_text.lower():
                    found.append(t)
                else:
                    for tag in t["tags"]:
                        if tag in user_text:
                            found.append(t)
                            break

            st.markdown("### 💙 쉬운 설명")
            if found:
                unique = []
                seen = set()
                for t in found:
                    if t["term"] not in seen:
                        unique.append(t)
                        seen.add(t["term"])

                for t in unique:
                    st.markdown(f"""
                    <div class="card">
                        <div class="kr-title">{t['kr']}</div>
                        <div class="blue-box">{t['plain']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown("**생활관리 힌트**")
                    for item in t["care"]:
                        st.write("•", item)
            else:
                st.info("등록된 용어와 정확히 연결되지는 않았어요.")
                st.write("질환명, 검사명, 약 이름, 주의사항을 따로 나누어 검색해보세요.")

            show_disclaimer()

elif page == "검사결과 쉽게 보기":
    st.title("🧾 검사결과 쉽게 보기")
    st.caption("건강검진 결과표에서 자주 보는 수치를 쉽게 풀어드립니다.")

    test_type = st.selectbox(
        "검사항목 선택",
        ["LDL", "HDL", "Triglyceride", "HbA1c"]
    )

    value = st.number_input("검사 수치를 입력하세요", min_value=0.0, step=1.0)

    if st.button("결과 쉽게 보기", type="primary"):
        st.markdown("### 💙 쉬운 해석")

        if test_type == "LDL":
            st.markdown("""
            <div class="card">
                <div class="term-title">LDL</div>
                <div class="kr-title">나쁜 콜레스테롤</div>
                <div class="blue-box">
                LDL은 혈관에 쌓이기 쉬운 콜레스테롤이에요.
                </div>
            </div>
            """, unsafe_allow_html=True)

            if value >= 160:
                st.error("수치가 높은 편이에요. 혈관 건강 관리가 필요할 수 있어요.")
                st.write("• 기름진 음식 줄이기")
                st.write("• 걷기 운동하기")
                st.write("• 의료진과 상담하기")
            elif value >= 130:
                st.warning("약간 높은 편일 수 있어요. 생활습관 관리가 도움이 될 수 있어요.")
            else:
                st.success("일반적으로는 비교적 안정적인 범위로 볼 수 있어요.")

        elif test_type == "HDL":
            st.markdown("""
            <div class="card">
                <div class="term-title">HDL</div>
                <div class="kr-title">좋은 콜레스테롤</div>
                <div class="blue-box">
                HDL은 혈관 속 남는 콜레스테롤을 치우는 데 도움을 주는 성분이에요.
                </div>
            </div>
            """, unsafe_allow_html=True)

            if value < 40:
                st.warning("HDL이 낮은 편일 수 있어요. 운동과 금연이 도움이 될 수 있어요.")
            else:
                st.success("HDL은 너무 낮지 않은 것이 좋아요.")

        elif test_type == "Triglyceride":
            st.markdown("""
            <div class="card">
                <div class="term-title">Triglyceride</div>
                <div class="kr-title">중성지방</div>
                <div class="blue-box">
                중성지방은 혈액 속 지방의 한 종류예요.
                </div>
            </div>
            """, unsafe_allow_html=True)

            if value >= 200:
                st.error("중성지방이 높은 편이에요. 식습관 관리가 필요할 수 있어요.")
                st.write("• 단 음료 줄이기")
                st.write("• 과식 줄이기")
                st.write("• 음주 줄이기")
            elif value >= 150:
                st.warning("약간 높은 편일 수 있어요.")
            else:
                st.success("일반적으로는 비교적 안정적인 범위로 볼 수 있어요.")

        elif test_type == "HbA1c":
            st.markdown("""
            <div class="card">
                <div class="term-title">HbA1c</div>
                <div class="kr-title">당화혈색소</div>
                <div class="blue-box">
                최근 2~3개월 동안의 평균 혈당 상태를 보여주는 검사예요.
                </div>
            </div>
            """, unsafe_allow_html=True)

            if value >= 6.5:
                st.error("당뇨병 기준에 해당할 수 있어요. 의료진 상담이 필요해요.")
            elif value >= 5.7:
                st.warning("당뇨 전단계 가능성이 있어요. 생활습관 관리가 중요해요.")
            else:
                st.success("일반적으로는 비교적 안정적인 범위로 볼 수 있어요.")

        show_disclaimer()

elif page == "즐겨찾기":
    st.title("⭐ 즐겨찾기")

    if not st.session_state.favorites:
        st.info("아직 즐겨찾기에 추가한 용어가 없어요.")
    else:
        fav_terms = [t for t in TERMS if t["term"] in st.session_state.favorites]
        for t in fav_terms:
            show_term(t)
            st.divider()

        if st.button("즐겨찾기 전체 비우기"):
            st.session_state.favorites = []
            st.rerun()

    show_disclaimer()

st.markdown("""
<div class="footer">
MediEasy · 어려운 병원 말을 쉬운 말로 바꾸는 의료용어 안내 서비스
</div>
""", unsafe_allow_html=True)
