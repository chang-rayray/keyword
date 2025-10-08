import json
import os
from pathlib import Path

from datakart import NaverAd

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.


def query_keywords_tool(keywords: str, event: int = None) -> list:
    # 환경변수에서 API 키 가져오기 (Streamlit Cloud 배포용)
    AD_KEY = os.getenv("NAVER_ACCESS_LICENSE", "0100000000039e2b17cc615102a8f0992c68c406bfa9203cfdcc6043f9b366eb0ce351e124")  # 검색광고 API '엑세스라이선스'
    AD_SEC = os.getenv("NAVER_SECRET_KEY", "AQAAAAADnisXzGFRAqjwmSxoxAa/tN9IV+qGRYodMleavmgarQ==")  # 검색광고 API '비밀키'
    AD_CUST_ID = os.getenv("NAVER_CUSTOMER_ID", "3313613")  # 검색광고 API 'CUSTOMER_ID'
    naver_ad = NaverAd(AD_KEY, AD_SEC, AD_CUST_ID)  # NaverAd 객체 생성
    resp = naver_ad.keywords_tool(keywords=keywords, event=event, show_detail=True)
    return resp.get("keywordList", [])


if __name__ == "__main__":
    keywords = "원피스"  # 검색 키워드
    resp = query_keywords_tool(keywords)  # 연관 키워드 검색
    with open(OUT_DIR / f"{Path(__file__).stem}.json", "w", encoding="utf-8") as fp:
        json.dump(resp, fp, ensure_ascii=False, indent=2)  # JSON으로 저장
