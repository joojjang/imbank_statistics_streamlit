import streamlit as st
import streamlit.components.v1 as components

# 스트림릿 페이지 기본 설정 (선택 사항)
st.set_page_config(page_title="내 HTML 앱", layout="wide")

st.title("스트림릿으로 만든 웹 페이지 🚀")
st.write("아래 영역은 준비하신 HTML 코드로 렌더링된 화면입니다.")

# 💡 여기에 가지고 계신 HTML 코드를 그대로 붙여넣으세요.
my_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tableau Dashboard</title>
</head>
<body>

<h1>My Dashboard</h1>

<div class='tableauPlaceholder' id='viz1774230973292' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt='시트 1'
                 src='https://public.tableau.com/static/images/_1/_17742307171120/1/1_rss.png'
                 style='border: none' />
        </a>
    </noscript>

    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https://public.tableau.com/' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='_17742307171120/1' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='language' value='ko-KR' />
    </object>
</div>

<script type='text/javascript'>
    var divElement = document.getElementById('viz1774230973292');
    var vizElement = divElement.getElementsByTagName('object')[0];

    vizElement.style.width = '1000px';
    vizElement.style.height = '800px';

    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';

    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f2f6; padding: 20px; }
        .box { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <div class="box">
        <h2>안녕하세요!</h2>
        <p>이곳에 가지고 계신 진짜 HTML 코드를 덮어쓰시면 됩니다.</p>
    </div>
</body>
</html>
"""

# HTML 코드를 화면에 렌더링합니다.
# height 값으로 세로 길이를 조절할 수 있습니다.
components.html(my_html, height=600, scrolling=True)
