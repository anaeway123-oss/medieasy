import streamlit as st
import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent

st.set_page_config(page_title="MediEasy", page_icon="💙", layout="wide", initial_sidebar_state="collapsed")


def load_css():
    css = (BASE / "styles" / "style.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def load_terms():
    return pd.read_csv(BASE / "data" / "terms.csv")


def split_items(value):
    if pd.isna(value) or value == "":
        return []
    return [x.strip() for x in str(value).split(";") if x.strip()]


def find_terms(df, keyword):
    if not keyword:
        return pd.DataFrame()
    k = keyword.lower().strip()
    mask = df.apply(lambda row: k in " ".join(map(str, row.values)).lower(), axis=1)
    return df[mask]


def show_disclaimer():
    st.markdown("""
    <div class="warn">
    ⚠️ MediEasy는 의료정보 이해를 돕는 서비스입니다. 진단·치료 결정은 반드시 의료진과 상담하세요.
    </div>
    """, unsafe_allow_html=True)


def show_term(row):
    tags = split_items(row.get("tags", ""))
    care = split_items(row.get("care", ""))
    departments = split_items(row.get("department", ""))
    tests = split_items(row.get("related_tests", ""))
    drugs = split_items(row.get("related_drugs", ""))
    tag_html = "".join([f"<span class='label'>#{t}</span>" for t in tags])

    st.markdown(f"""
    <div class="card">
        <span class="label">{row['category']}</span>
        {tag_html}
        <div class="title">{row['term']}</div>
        <div class="kr">{row['kr']}</div>
        <div class="bluebox">
            <b>💙 쉽게 설명</b><br>
            {row['easy']}<br>{row['plain']}
        </div>
        <p><b>👨‍⚕️ 병원에서는 이렇게 말할 수 있어요</b><br>“{row['doctor']}”</p>
        <p><b>🏥 언제 듣는 말인가요?</b><br>{row['when']}</p>
        <div class="warn">⚠️ {row['warning']}</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🌿 생활관리")
        for item in care:
            st.write("•", item)
    with c2:
        st.markdown("#### 🏥 관련 진료과")
        for item in departments:
            st.write("•", item)
    with c3:
        st.markdown("#### 🧾 관련 검사/약")
        for item in tests + drugs:
            st.write("•", item)


load_css()
terms = load_terms()

st.sidebar.markdown("### 💙 MediEasy")
page = st.sidebar.radio("메뉴", ["홈", "병원말 검색", "검사결과", "약 설명", "서비스 소개"])

if page == "홈":
    st.markdown("""
    <section class="hero">
        <div class="logo">💙</div>
        <h1>MediEasy</h1>
        <h2>Understand Your Health.<br>Simply.</h2>
        <p>병원에서 들은 어려운 말, 검사결과, 약 이름을 겁주지 않고 쉬운 말로 설명합니다.</p>
    </section>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    keyword = st.text_input("검색", placeholder="🔍 고지혈증, LDL, HbA1c, 메트포르민처럼 입력해보세요", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if keyword:
        results = find_terms(terms, keyword)
        st.markdown(f"### 검색 결과 {len(results)}개")
        if len(results):
            for _, row in results.iterrows():
                show_term(row)
        else:
            st.info("아직 등록되지 않은 말이에요. 다른 표현으로 검색해보세요.")

    st.markdown("### 🔥 많이 찾는 말")
    popular = ["고혈압", "고지혈증", "당뇨병", "LDL", "HbA1c", "심근경색"]
    st.markdown("".join([f"<span class='pill'>{p}</span>" for p in popular]), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature"><div class="icon">🔍</div><b>병원말 검색</b><span>의학용어를 환자 눈높이로 설명합니다.</span></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature"><div class="icon">🧾</div><b>검사결과 이해</b><span>LDL, HbA1c 같은 수치를 쉽게 해석합니다.</span></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature"><div class="icon">💊</div><b>약 설명</b><span>약을 왜 먹는지와 주의사항을 정리합니다.</span></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="soft-card">
        <h3>💙 MediEasy의 원칙</h3>
        <p>불필요하게 겁주지 않고, 어려운 말을 생활 언어로 바꾸며, 필요한 경우 의료진 상담을 안내합니다.</p>
    </div>
    """, unsafe_allow_html=True)
    show_disclaimer()

elif page == "병원말 검색":
    st.title("🔍 병원말 검색")
    keyword = st.text_input("궁금한 병원 말을 입력하세요", placeholder="예: 고지혈증, pneumonia, 혈압, 심근경색")
    results = find_terms(terms, keyword) if keyword else terms
    st.caption(f"결과 {len(results)}개")
    for _, row in results.iterrows():
        show_term(row)
        st.divider()
    show_disclaimer()

elif page == "검사결과":
    labs = pd.read_csv(BASE / "data" / "labs.csv")
    st.title("🧾 검사결과 쉽게 보기")
    selected = st.selectbox("검사항목", labs["name"].tolist())
    value = st.number_input("검사 수치", min_value=0.0, step=1.0)
    lab = labs[labs["name"] == selected].iloc[0]

    st.markdown(f"""
    <div class="card">
        <div class="title">{lab['name']}</div>
        <div class="kr">{lab['kr']}</div>
        <div class="bluebox">{lab['easy']}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("수치 해석하기", type="primary"):
        if selected == "HDL":
            if value < float(lab["low"]):
                st.warning("낮은 편일 수 있어요. 생활습관 관리가 도움이 될 수 있어요.")
                st.write(lab["low_tip"])
            else:
                st.success("너무 낮지 않은 범위로 볼 수 있어요.")
        else:
            if value >= float(lab["caution_high"]):
                st.error("높은 편일 수 있어요. 의료진과 상담이 필요할 수 있습니다.")
                st.write(lab["high_tip"])
            elif value > float(lab["normal_high"]):
                st.warning("약간 높은 편일 수 있어요. 생활관리와 재확인이 도움이 될 수 있어요.")
            else:
                st.success("입력한 수치는 일반적으로 비교적 안정적인 범위로 볼 수 있어요.")
        show_disclaimer()

elif page == "약 설명":
    drugs = pd.read_csv(BASE / "data" / "drugs.csv")
    st.title("💊 약 설명")
    keyword = st.text_input("약 이름을 입력하세요", placeholder="예: Metformin, 아스피린, 스타틴")
    results = drugs if not keyword else drugs[drugs.apply(lambda r: keyword.lower() in " ".join(map(str, r.values)).lower(), axis=1)]
    for _, row in results.iterrows():
        st.markdown(f"""
        <div class="card">
            <div class="title">{row['name']}</div>
            <div class="kr">{row['kr']}</div>
            <div class="bluebox"><b>왜 먹나요?</b><br>{row['why']}</div>
            <p><b>어떻게 먹나요?</b><br>{row['how']}</p>
            <div class="warn">⚠️ {row['caution']}</div>
        </div>
        """, unsafe_allow_html=True)
    show_disclaimer()

elif page == "서비스 소개":
    st.title("💙 About MediEasy")
    st.markdown("""
    <div class="soft-card">
        <h2>병원에서 나오는 순간, 환자가 가장 먼저 여는 앱</h2>
        <p>MediEasy는 진단을 대신하지 않습니다. 환자가 자신의 건강 정보를 더 쉽게 이해하고, 의료진과 더 잘 소통하도록 돕습니다.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">MediEasy · Understand Your Health. Simply.</div>', unsafe_allow_html=True)
