<div align="center">

  # Social Networking Service
  
  <p>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>&nbsp
    <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"></a>&nbsp
    <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"></a>&nbsp
    <br>
    <img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white"></a>&nbsp
    <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white"></a>&nbsp
    <img src="https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch"></a>&nbsp
    <br>
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"></a>&nbsp
    <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"></a>&nbsp
  </p>

</div>

## 목차
- [개발 기간](#--개발-기간--)  
- [요구 사항](#-요구사항)
- [개발 조건](#-개발-조건)
- [실행방법](#실행-방법)
- [배포](#-배포)
- [swagger](#swagger)  
- [테스트 케이스](#테스트-케이스)  
- [기술 스택](#기술-스택) 


<br><br>
<div align="center">

|                깃 허브                 |                블로그                  |                개인 노션                  |
| :-----------------------------------: | :-----------------------------------:| :-----------------------------------:|
| [Github](https://github.com/SMin1620) |[Tistory](https://smin1620.tistory.com/) |[Notion](https://tame-antelope-1cb.notion.site/SNS-Social-Networking-Service-8b7d96f2873642cb983993d1b4ffdf2f) |

  <br>

| <img height="200" width="330" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGElLjafMUhHglmqwh9lRh_sVzOCQyBiPNfQ&usqp=CAU"> |
| :----------------------------------------------------------: |
| 📒 [**Project page**](https://tame-antelope-1cb.notion.site/SNS-Social-Networking-Service-8b7d96f2873642cb983993d1b4ffdf2f) |
|        공지사항, 컨벤션 공유 등<br> 우리 팀을 위한 룰        | 요구사항 분석, 정보 공유 및<br> 원할한 프로젝트를 위해 사용  |
 <br>
  </div> 

  <h2> ⌛ 개발 기간  </h2> 
 2022/07/20  ~ 2022/07/
 <br><br>
  </div> 
  
# 💻 요구사항
### 필수 기능
  - 유저 관리 
    - 유저 회원가입
      - 이메일을 ID로 사용합니다.
    - 유저 로그인 및 인증
      - JTW 토큰을 발급받으며, 이를 추후 사용자 인증으로 사용합니다.
      
  - 게시글 관리
    - 게시글 생성
      - 제목, 내용, 해시태그 등을 입력하여 생성합니다.
      - 제목, 내용, 해시태그는 필수 입력사항이며, 작성자 정보는 request body에 존재하지 않고, 해당 API 를 요청한 인증정보에서 추출하여 등록 합니다. 
      - 해시태그는 #로 시작되고 , 로 구분되는 텍스트가 입력됩니다.
    - 게시글 수정
      - 작성자만 수정할 수 있습니다.
    - 게시글 삭제
      - 작성자만 삭제할 수 있습니다.
      - 작성자는 삭제된 게시글을 다시 복구할 수 있습니다.
    - 게시글 상세보기
      - 모든 사용자는 모든 게시물에 보기권한이 있습니다.
      - 작성자를 포함한 사용자는 본 게시글에 좋아요를 누를 수 있습니다. 좋아요된 게시물에 다시 좋아요를 누르면 취소됩니다.
      - 작성자 포함한 사용자가 게시글을 상세보기 하면 조회수가 1 증가합니다. (횟수 제한 없음)
    - 게시글 목록
      - 모든 사용자는 모든 게시물에 보기권한이 있습니다.
      - 게시글 목록에는 제목, 작성자, 해시태그, 작성일, 좋아요 수, 조회수 가 포함됩니다.
      - Ordering (= Sorting, 정렬)
        - default = -created_at
      - Searching (= 검색)
      - Filtering (= 필터링)
      - Pagination (= 페이지 기능)
        - default = 10
      - 동시에 적용이 가능해야합니다
      

### 추가기능
   - 유저 관리 -> 추가 기능 (관리자 권한)
      - 회원가입된 유저 목록을 조회합니다.
      - 유저의 상세 정보를 조회합니다.
        - 사용자가 직접 정보를 보는 데이터 포함, 권한 부여 가능 필드도 추가
      - 유저의 정보를 수정할 수 있습니다.
        - 사용자가 직접 정보를 보는 데이터 포함, 권한 부여 수정 가능
        
   - 게시글 관리 -> 추가 기능
      - 조회수 기능
        - 인가된 사용자, 인가되지 않은 사용자로 구분해서 조회수가 카운트 되도록 합니다.
        - 한번 조회수 카운트가 된 사용자는 10분동안 해당 게시글에 조회수가 반영되지 않습니다.
        
   - 댓글 관리 -> 추가 기능
      - 댓글 생성
        - 댓글의 내용을 입력해서 생성합니다. (필수 입력사항)
        - 작성자 정보는 request body에 존재하지 않고, 해당 API 를 요청한 인증정보에서 추출하여 등록 합니다. 
      - 댓글 수정
        - 작성자만 수정할 수 있습니다. 
      - 댓글 삭제
        - 작성자만 삭제할 수 있습니다.
      - 대댓글 생성
        - 대댓글의 내용을 입력해서 생성합니다. (필수 입력사항)
        - 작성자 정보는 request body에 존재하지 않고, 해당 API 를 요청한 인증정보에서 추출하여 등록 합니다. 
      - 대댓글 수정
        - 작성자만 수정할 수 있습니다.
      - 대댓글 삭제
        - 작성자만 삭제할 수 있습니다.
        
### 고도화 예정 기능
  - 채팅 기능 -> 추가 기능
    - 채팅 룸 생성
    - 채팅 메시지 생성
    - 채팅 메시지 소비
    
  - 검색 엔진 및 시각화 관리 -> 추가 기능
    - Elasticsearch
    - Kibana
    - Logstash
  
<br>

### 🚥 개발 조건 

  #### 🙆‍♂️ 필수사항  
    - Python, Django
    - REST API 구현
    - 토큰을 이용한 인증 제어 방식
    - ordering, searching, filtering, pagination
    
  #### 🔥 선택사항
  <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white"></a><br>
  #### 캐싱 전략
      SNS 서비스 특성상 많은 유저가 해당 게시글을 조회할 것으로 판단하였습니다.
      db의 접속을 줄이고 캐시 메모리를 이용해서 성능적인 부분을 고려해서 캐싱 전략을 사용했습니다.
      Redis Cache를 이용해서 key "(article_id) : value (user_id)"의 형태로 캐시 메모리에 저장한 다음, 
      같은 유저가 같은 게시글을 조회했을 때 의도적으로 조회수 카운트 상승을 방지하였습니다.
      
  #### 채팅
     미구현


