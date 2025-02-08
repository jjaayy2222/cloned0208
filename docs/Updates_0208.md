# 프로젝트 관련 변경 및 보고

#####################################
#* **settings.py** 변경됨           #
#* **email_app** 변경됨             #
#* **.env** 변경됨 (teams 폴더 확인) #
#* **docs** 추가                    #
#####################################

## (1) 변경내용_0208(토)

#### ⅰ. app_email app 변경
- **`/docs/`** 폴더 추가: 프로젝트 문서화 및 설정 파일을 보관하기 위한 폴더
  - **`/static/`** 폴더 변경: 정적 파일들이 `/static/` 폴더로 재구성
- **`/static/`** 폴더 변경: 정적 파일들이 `/static/` 폴더로 재구성

#### ⅱ. /app/ 내 변경
- **'/app/views.py/'** : view 함수 추가 (이유는 (2)의 프로젝트 구조 및 경로 설정 참고) → bug (작동 X)
    - @login_required
        * def send_email(request):
        * return render(request, "email_app/send_email.html")

    - @login_required
        * def email_list(request):
        * return render(request, "email_app/email_list.html")

    - @login_required
      * def email_detail(request, email_id):
      * return render(request, "email_app/email_detail.html")
  
#### ⅲ. /email_app/ 변경 : 전체 변경  
- **'/email_app/templates/email_app/'** 
      - **send_email.html** : 'home' 화면, email_list에서 등 관리자에게 작성 가능 / 새 창 띄우기(모달)
      - **email_list.html** : 'home'화면 / 로그인 개별 드롭다운 메뉴의 **메일 목록** → 작동 X (∵ 경로 설정 참고)
      - **email_detail.html** : **email_list.html**에서 해당 이메일을 눌렀을 경우 새 창(모달)에서 상세 내용 확인 기능 제공 → 작동 여부 아직 확인 못 함
- **'/email_app/views.py/'**
- **'/email_app/models.py/'**
- **'/email_app/urls.py/'**
- **'/email_app/forms.py/'** 

#### ⅲ. 프로젝트 단위 변경 (team6, 루트 하위)
- **'/settings.py/'**
      - email 설정 관련 내용 추가
      - login 후, logout 후 redirection 경로 변경
      - BASE_DIR 변경
      - INS_APP 추가
      - etc..
- **`마이그레이트 필요`**
      - 마이그레이션 실행
        - email_app 변경으로 마이그레이션 파일 생성
        - `/email_app/migrations/0002_alt.../`
  
      - **`마이그레이트`** 필요
        - `python manage.py migrate`
  
- **'.gitignore'** : 추가 ( git 삭제 및 커밋 오류 ) → log 커밋 X 
      - ai_playground/dalle3
      - ai_playground/gpt4o-mini
  
- **'current_requirements.txt'** : requirementx.txt 추가된 내용
      - `crispy-forms`, `crispyforms-bootstrap5` 패키지 추가
      - 실제 써보니 매우 깔끔하고 심플
  
- **'/docs/Updates_0208.md'**


## (2) 보고

#### ⅰ. Django 프로젝트 구조
- **Django 프로젝트의 구조**
    - 기본적인 Django
    **myproject/**  - 프로젝트 명명
    │
    ├── myproject/                     # 프로젝트 루트 디렉토리
    │   ├── settings.py                # Django 설정 파일
    │   ├── urls.py                    # 프로젝트 전체 URL 패턴 관리
    │   ├── wsgi.py                    # 배포 관련 파일    ↑
    │   ├── asgi.py                    # 배포 관련 파일    │
    │                                                     │
    ├── templates/                     # 프로젝트 전체 템플릿 폴더
    │   ├── main.html                  # 최상위 템플릿 (헤더, 푸터 포함)
    │   ├── home.html                  # 홈페이지 템플릿
    │
    ├── app/                           # 첫 번째 앱 (or  기본 앱) 
    │   ├── templates/                 # 앱별 템플릿 폴더
    │   │   └── app_name/              # 앱의 템플릿 디렉토리
    │   │       └── index.html         # 앱의 기본 템플릿
    │   ├── views.py                   # 앱의 뷰 함수
    │   ├── urls.py                    # 앱의 URL 패턴
    │   ├── models.py                  # 앱의 모델
    │   ├── admin.py                   # 모델을 Admin에 등록
    │                                  # admin (관리자 페이지)에서 관리 가능
    │
    ├── app2/                          # 두 번째 앱
    │   ├── templates/                 # 앱별 템플릿 폴더
    │   │   └── app_name/              # 앱의 템플릿 디렉토리
    │   │       └── index.html         # 앱2의 기본 템플릿
    │   ├── views.py                   # 앱2의 뷰 함수
    │   ├── urls.py                    # 앱2의 URL 패턴
    │   ├── models.py                  # 앱2의 모델
    │   ├── admin.py                   # 모델을 Admin에 등록하면 관리 가능
    │
    ├── manage.py                      # Django 관리 파일
    │
    └── requirements.txt 등등... 

    - 우리 프로젝트의 구조에 반영
    **INSPERATION/**  - 프로젝트 명명
        │
        ├── team6/                         # 프로젝트 루트 디렉토리에 해당 
        │   ├── settings.py                # Django 설정 파일
        │   ├── **viwes.py**                   # 프로젝트 전체 관련 뷰 함수
        │   ├── **urls.py**                    # 프로젝트 전체 URL 패턴 관리
        │   ├── wsgi.py                    # 배포 관련 파일    ↑
        │   ├── asgi.py                    # 배포 관련 파일    │
        │   └── __init__.py                                   │
        │                                                     │
        ├── **templates/**                     # 프로젝트 전체 템플릿 폴더
        │   ├── main.html                  # 최상위 템플릿 (헤더, 푸터 포함)
        │   ├── home.html                  # 홈페이지 템플릿
        │
        ├── app/                           # 기본 앱
        │   ├── **templates/**                 # 앱 템플릿 폴더
        │   │   └── app/                   # 앱의 템플릿 디렉토리
        │   │       ├── index.html                # 기본 템플릿
        │   │       ├── generate_image.html       # main_이미지 생성    
        │   │       ├──  ...                                        
        │   │       └── board.html      
        │   │                         
        │   ├── **views.py**                   # 앱의 뷰 함수
        │   │
        │   │                
        │   ├── **urls.py**                    # 앱의 URL 패턴
        │   │
        │   │                
        │   ├── models.py                  # 앱의 모델
        │   ├── admin.py                   # 모델을 Admin 등록 
        │   │                               # admin (관리자 페이지)에서 관리 가능
        │   │
        ├── ai_playground/                 # 두 번째 앱
        │   ├── templates/                 # 앱별 템플릿 폴더
        │   │   └── ai_playground/              # 앱의 템플릿 디렉토리
        │   │       └── image_history.html         # 앱2의 기본 템플릿
        │   ├── views.py                   # 뷰 함수
        │   ├── urls.py                    # URL 패턴
        │   ├── models.py                  # 모델
        │   ├── admin.py                   # 미등록 - Admin에 등록하면 관리자 페이지에서 관리 가능
        │   └── 기타 ipynb,py 파일 ... 
        │
        ├── artwork/                       # (임시) 앱 - 아직 설정 기능 없음 / 바꿔도 됨
        │   ├── templates/                 # 앱별 템플릿 폴더
        │   │   └── artwork/               # 앱의 템플릿 디렉토리
        │   │       └── index.html         # (임시, 이름 = index) - 공개 갤러리용 으로 생각? 구상? / 바꿔도 됨
        │   ├── views.py                   # 뷰 함수 (임시 / 바꿔도 됨)
        │   ├── urls.py                    # URL 패턴 (임시 / 바꿔도 됨)
        │   ├── models.py                  # 모델 (임시 / 바꿔도 됨됨)
        │   └── admin.py                   # 미등록 - Admin에 등록하면 관리자 페이지에서 관리 가능
        │
        ├── accounts/                       # 계정 관련 앱앱
        │   ├── templates/                  # 앱별 템플릿 폴더
        │   │   └── accounts/               # 앱의 템플릿 디렉토리
        │   │       │   login.html              # 로그인 → 현재 'app/templates/app/main(부모)-navtion_var' url 경로'   
        │   │       │   loginmodal.html              # └→ 로그인 페이지를 새창으로 띄우기(모달) 위한 페이지  
        │   │       │   profile_update.html              # 프로필 수정 → 현재 'app/templates/app/main(부모)-navtion_var' url 경로'  
        │   │       └── singup.html             # 회원가입 → 현재 'app/templates/app/main(부모)-navtion_var' url 경로' (but, html 삭제됨됨)
        │   ├── views.py                        # 뷰 함수 (임시 / 바꿔도 됨)
        │   ├── urls.py                    # URL 패턴 (임시 / 바꿔도 됨)
        │   ├── models.py                  # 모델 (임시 / 바꿔도 됨됨)
        │   └── admin.py                   # Admin에 등록 
        ├── artwork/                       # (임시) 앱 - 아직 설정 기능 없음 / 바꿔도 됨
        │   ├── templates/                 # 앱별 템플릿 폴더
        │   │   └── artwork/               # 앱의 템플릿 디렉토리
        │   │       └── index.html         # (임시, 이름 = index) - 공개 갤러리용 으로 생각? 구상? / 바꿔도 됨
        │   ├── views.py                   # 뷰 함수 (임시 / 바꿔도 됨)
        │   ├── urls.py                    # URL 패턴 (임시 / 바꿔도 됨)
        │   ├── models.py                  # 모델 (임시 / 바꿔도 됨됨)
        │   └── admin.py                   # 미등록 - Admin에 등록하면 관리자 페이지에서 관리 가능
        │
        ├── static/                        # 프로젝트 전체의 정적 파일 (개발 환경에서 필요요)
        │   ├── css/                            # CSS 파일
        │   ├── js/                             # JavaScript 파일
        │   └── img/                            # 이미지 파일
        │
        ├── staticfiles/                   # `collectstatic`으로 모은 정적 파일 (배포 환경에서 필요)
        │   ├── css/                            # 배포용 CSS
        │   ├── js/                             # 배포용 JS
        │   └── img/                            # 배포용 이미지
        │
        │           ```python``` : `settings.py` in Django
        │           - 개발 환경에서 사용되는 static 폴더 : `STATIC_URL = '/static/'`
        │           - 프로젝트의 정적 파일 디렉토리 : `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`  # 개발 중인 static 폴더
        │           - 배포 환경에서 정적 파일을 모을 폴더 : `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`  # `collectstatic`으로 모을 폴더
        │
        ├── READEME.md    # 프로젝트 전반 안내
        │
        ├── manage.py                      # Django 관리 파일
        │
        └── requirements.txt 등등... 

- 
- 프로젝트 루트 디렉토리 = `team6`
- 루트 
    - / urls.py
        - 앱_name/templates/앱_name/`OOO.html` 
        - include로 포함
        - 부모-자식 템플릿으로 연결 가능 → 유지 보수 유리
  
    - / views.py
        - 프로젝트 전반적인 뷰 함수 관리
        - 루트/templates/ OOO.html에 들어가는 기능 조정
            - `main.html`
            - `home.html`  등
        - 프로젝트 공통 뷰, 기본적인 설정 관리
  

#### ⅱ. 경로 설정 관련
- 작업 방식
      - 경로 충돌 방지 및 Django의 프로젝트 구조 특성 반영 작업 (위 구조 참고)
      - Django : 모델, 템플릿, 뷰 패턴 → 유지보수성, UI 변경 일관성 등
- 현 상황
      - 루트 
            - / template / → 사라짐 + /app/으로 통합 
            - `views.py` → 사라짐 +  /app/으로 통합합
      - /app/
            - `/ template /` ≒ 루트의 `templates` 역할 
            - `views.py` , `urls.py` 등 루트의 `templates` 역할
      - 변동 상황에서 경로 다시 잡기 어려움 ㅠㅠ
            - html 다듬고, 개발 서버 활성화 후에 결과 확인이 잘 되지 않음
            - 코드의 문제인지, 경로의 문제인지 ㅠㅠ 
            - 애증의 장고.......... (이제는 증만 남은 것 같은... )

## (3) 건의 

#### ⅰ. 경로 및 역할 혹은 일정 조율 부탁 
- 경로 설정 도움 요청 ㅠㅠ 
      - 경로 설정 어려움 토로 
      - email_app을 만들었으나 확인이 안되....어서.. 참.. 그렇습니다..
      - 속상하고, 미안하고, 죄송하고 ㅠㅠ 
  
- 일정 조율 도움 요청 ㅠㅠ 
      - BE 작업이 어느 정도 마무리 되면 FE 작업에 집중할 수 있을 것 같아요 ㅠㅠ
      - 작업 흐름에 바로 따라가지 못하더라도 양해를 부탁 ㅠㅠ   

#### ⅱ. 다음주 서비스 확장 관련 아이디어
- **서비스 확장** 관련 아이디어
    - 웹페이지의 **Event** 에 팀원들이 참여한 것처럼 각자 하고 싶은 것을 해보기 (선택적) → **Azure AI service, Azure power platform 등 다양하게 활용**
    - 
    - **Event** menu - `insperAItion의 영감을 보여주세요!`
        - [ 예시 ] insperAItion = 이미지 생성 서비스 
                - → 생각보다 내가 원하는 이미지가 안나와요! 
                - → 좋은 프롬프트 contest → **좋은 프롬프트 생성기 or 프롬프트 라이브러리 만들어 하나의 메뉴 or 서비스**로 제공
        - [ 예시 ] - (선한 영향력?) 도움이 될 수 있는 디자인해보기기
                - 참조 : 일본 콘서트의 긴테 문화 [https://theqoo.net/square/3425149540]
                - 쓰레기로 버리거나 낭비하지 않는 디자인에 활용해보기
             
        - [교육 자료] 만들기
                - 교사 or 학생 참여 가정
                 
        - [ 지역 홍보 자료 ] 
                - 지자체 or 공무원 참여 가정
                 
        - 내가 갖고 싶은 굿즈 직접 디자인하기기
                - 참조 : 국립 중앙 박물관 굿즈 [https://www.museumshop.or.kr/kor/main.do]
                - 너무 예쁜 키보드.jpg ![img](https://www.museumshop.or.kr/kor/product/product_view.do?str_bcode=264708&str_goodcode=202411250002)
                - 센스 넘치는 인센스.jpg ![img](https://www.museumshop.or.kr/kor/product/product_view.do?str_bcode=001003002&str_goodcode=202409130001)
                - 미소짓는 간장 종지.jpg ![img](https://m.cafe.daum.net/nomakeup/cCbd/3012?svc=TOPRANK)
                 
        - 전시 자료 만들기
                - 미디어 아트 전시 디자인
                - 디지털 아트 or 몰입형 미디어 전시
                - 참조 [https://post.naver.com/viewer/postView.naver?volumeNo=33582968&memberNo=37451778]
                - 참조 [https://blog.naver.com/kcc_press/223593823198]
                - 참조 [https://brunch.co.kr/@poiu044/35]
                
        - 실시간 AI 생성 - 전시 중 실시간으로 AI가 이미지를 생성하고 변형하는 작품 전시회
                - 매번 새로운 경험 제공
                - 예시 : 픽 아나돌(Refik Anadol)의 작품을 들 수 있습니다. 아나돌은 최근 뉴욕 현대미술관(MoMA)에서 'Unsupervised(감독하지 않은)'이라는 전시를 통해 AI와 빅데이터를 사용하여 실시간으로 이미지를 생성해내는 작업을 선보임
                      - 인공지능이 수면 중 꿈을 꾸는 것처럼 이미지를 무한히 생성
                      - 실시간으로 변화하는 이미지로 관객의 시선을 사로잡음
                      - AI가 학습한 데이터를 바탕으로 새로운 시각적 경험 생성
                      - 참조 [https://datamuseum.tistory.com/51]
                - 디지털 아트의 예시 : [https://nilili.co.kr/%EB%94%94%EC%A7%80%ED%84%B8%EC%95%84%ED%8A%B8odyssey/%ED%95%9C%EB%88%88%EC%97%90-%EB%B3%B4%EB%8A%94-%EB%94%94%EC%A7%80%ED%84%B8-%EC%95%84%ED%8A%B8-%EC%A2%85%EB%A5%98%EC%99%80-%EC%98%88%EC%8B%9C/#4_%EC%BB%B4%ED%93%A8%ED%84%B0_%EC%83%9D%EC%84%B1_%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98]
        - 데이터 시각화 아트 등
        - 수화 예쁘게 디자인 하기
        - 픽토그램 만들기
        - 싸인 만들어주는 프로그램
        - 로고, 라벨, 스티커 만들어주는 프로그램 등

    ▶ **Event** 형식으로 열어 각자 하고 싶은 것을 하고, 서비스로 만들어 메뉴에 포함 → (가능하면) **웹페이지 버전 업 (서비스 업그레이드!)**!!