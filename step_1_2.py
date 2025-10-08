import json
import os
from pathlib import Path

from datakart import Naver

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.


def query_naver_shop(query: str, display: int = 1) -> dict:
    # 환경변수에서 API 키 가져오기 (Streamlit Cloud 배포용)
    NAVER_KEY = os.getenv("NAVER_CLIENT_ID", " 1scWD4LESufT6Om36Xf_")  # 네이버 서비스 API 'Client ID'
    NAVER_SEC = os.getenv("NAVER_CLIENT_SECRET", "TK_298i8_L")  # 네이버 서비스 API 'Client Secret'
    naver = Naver(NAVER_KEY, NAVER_SEC)  # Naver 객체 생성
    return naver.shop(query=query, display=display)


if __name__ == "__main__":
    query = "원피스"  # 검색 키워드
    resp = query_naver_shop(query)  # 네이버 쇼핑 상품 검색
    with open(OUT_DIR / f"{Path(__file__).stem}.json", "w", encoding="utf-8") as fp:
        json.dump(resp, fp, ensure_ascii=False, indent=2)  # JSON으로 저장
