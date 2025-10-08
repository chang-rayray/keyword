import os
from datakart import NaverAd

# 환경변수에서 API 키 가져오기 (Streamlit Cloud 배포용)
AD_KEY = os.getenv("NAVER_ACCESS_LICENSE", "엑세스라이선스")  # 검색광고 API '엑세스라이선스'
AD_SEC = os.getenv("NAVER_SECRET_KEY", "비밀키")  # 검색광고 API '비밀키'
AD_CUST_ID = os.getenv("NAVER_CUSTOMER_ID", "CUSTOMER_ID")  # 검색광고 API 'CUSTOMER_ID'
naver_ad = NaverAd(AD_KEY, AD_SEC, AD_CUST_ID)  # NaverAd 객체 생성
resp = naver_ad.keywords_tool(keywords="화장품")  # 연관 키워드 검색
print([row["relKeyword"] for row in resp["keywordList"]])  # ['화장품', '한방화장품', ...]

resp = naver_ad.keywords_tool(event=86)  # '반려동물' 시즌 테마 연관 키워드 검색
print([row["relKeyword"] for row in resp["keywordList"]])  # ['동물병원', '애견미용', ...]
