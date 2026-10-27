
import streamlit as st
import streamlit.components.v1 as components
import json
import html

from url_shortner import urlshort_fun
from check_url import check_urls
from datbase import get_all_url

st.set_page_config(
    page_title="URL Shortener",
    page_icon="🔗",
    layout="centered"
)

# ---------------- SIDEBAR HISTORY ----------------

with st.sidebar:
    st.title("🔗 URL History")
    all_url = get_all_url()

    if not all_url:
        st.info("No URLs in history yet.")

    for i, row in enumerate(all_url):
        original_url, short_id = row

        # IMPORTANT:
        # Replace this with the actual domain where your
        # short URLs are hosted, if you have deployed the app.
        short_url = "https://" + str(short_id)

        safe_url = json.dumps(short_url)
        button_id = f"copy_{i}"

        components.html(
            f"""
            <button
                id="{button_id}"
                style="
                    width: 100%;
                    padding: 9px;
                    margin-bottom: 5px;
                    cursor: pointer;
                    border: 1px solid #888;
                    border-radius: 6px;
                    background: transparent;
                    color: white;
                    overflow-wrap: anywhere;
                "
                onclick="copyUrl()">
                📋 {html.escape(original_url)}
            </button>

            <script>
            async function copyUrl() {{
                const url = {safe_url};
                const btn = document.getElementById("{button_id}");

                try {{
                    await navigator.clipboard.writeText(url);
                    btn.innerText = "✅ Copied!";
                }} catch (err) {{
                    btn.innerText = "❌ Copy failed";
                }}
            }}
            </script>
            """,
            height=48
        )

# ---------------- MAIN PAGE ----------------

st.title("🔗 URL Shortener")
st.write("Have a long URL? Shorten it using this tool.")

url = st.text_input("Enter your URL")

reduce_percent = st.slider(
    "URL compression (%)",
    min_value=0,
    max_value=90,
    value=50
)
if st.button("Shorten URL"):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        active = check_urls(url)

        if active is False:
            st.warning("This URL is not valid. Please check it.")
       
        short_url = urlshort_fun(
                url,
                active,
                reduce_percent
        )
        st.success("Your shortened URL is ready!")
        st.code(short_url, language=None)
        st.link_button("Open shortened URL", short_url)
        st.info("Refresh the page to update the URL history.")
