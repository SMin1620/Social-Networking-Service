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
    <img src="https://img.shields.io/badge/Kibana-005571?style=for-the-badge&logo=Kibana&logoColor=white"></a>&nbsp
    <img src="https://img.shields.io/badge/logstash-005571?style=for-the-badge&logo=Logstash&logoColor=white"></a>&nbsp
    <br>
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"></a>&nbsp
    <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"></a>&nbsp
  </p>

</div>

## 목차
- [개발 기간](#--개발-기간--)  
- [요구 사항](#-요구사항)
- [개발 조건](#-개발-조건)
- [API Doc](#-API-Doc)
- [실행방법](#실행-방법)
- [배포](#-배포)
- [swagger](#swagger)   


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
  
  
# ERD
![image](https://user-images.githubusercontent.com/81574795/180919660-692e6187-ed0a-4b64-93d0-8ae20e6fdc53.png)

  
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
      - 유저끼리 팔로우, 언팔로우를 할 수 있습니다.

        
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

<br>

## 🚥 개발 조건 

  ### 🙆‍♂️ 필수사항  
    - Python, Django
    - REST API 구현
    - 토큰을 이용한 인증 제어 방식
    - ordering, searching, filtering, pagination
    
  #### Simple-JWT 라이브러리 사용
       사용자 인증에 필요한 모든 정보는 토큰 자체에 포함하기 때문에 별도의 인증 저장소가 필요없다는 점과 
       분산 마이크로 서비스 환경에서 중앙 집중식 인증 서버와 데이터베이스에 의존하지 않는 JWT 인증 방식을 선택했습니다. 
       최근에는 django-rest-framework-jwt 라이브러리를 많이 사용하지 않는다고 한다.
       또한 DRF 공식문서에 따르면 djangorestframework-simplejwt  라이브러리 사용을 권장하고 있어서 simple-jwt를 채택하였습니다.
       
  #### 소프트 딜리트
       SofrDelete 모델을 추가하고, delete할 때 delete_date 현재 시간으로 갱신되고, restore(복원)할 때에는 delete_date는 None 값으로 갱신됩니다.
  ```
       class SoftDeleteManager(models.Manager):
          use_for_related_fields = True

          def get_queryset(self):
              return super().get_queryset().filter(delete_date__isnull=True)


       class DeleteManager(models.Manager):
          use_for_related_fields = True

          def get_queryset(self):
              return super().get_queryset().filter(delete_date__isnull=False)
              
              .
              .
              .
              
        def delete(self, using=None, keep_parents=False):
            self.delete_date = now()
            self.save(update_fields=['delete_date'])

        def restore(self):
            self.delete_date = None
            self.save(update_fields=['delete_date'])
  ```

  ### 🔥 추가사항
  #### 조회수
      조회수 반영에는 로그인 하지 않은 사용자도 포함되어야 하기 때문에 데어터가 매우 많을 것으로 예상하여서, 기본적으로 redis 캐싱 전략을 사용하였습니다.
      조회수는 두 가지로 나눠지는데 로그인한 사용자(인가된 사용자)와 로그인 하지 않은 사용자(인가되지 않은 사용자)로 나누어서 개발하였습니다.
      인가된 사용자는 기본적으로 인증된 id 값을 캐시메모리에 저장해서 확인하는 절차를 선택하였고, 
      인가되지 않은 사용자는 해당 고유의 PC ip를 이용해서 조회수에 반영되도록 하였습니다.
      또한, 무분별한 조회수 올리는 것을 방지하기 위해서 expire time(TTL)을 두어 10분뒤에 다시 게시글에 접속하면 조회수가 오르도록 구현하였습니다.
  #### 팔로우
      각 사용자는 다른 사용자와 팔로우 관계를 맺을 수 있습니다. 
      다른 사람을 팔로우 할 때에는, 먼저 자신이 그 사람을 팔로우 했는지부터 여부를 확인하고 진행하게 됩니다.
      언팔로우도 마찬가지로 같은 로직으로 구현되었습니다.
     
  #### 댓글 및 대댓글
      아래의 방식으로 댓글과 대댓글을 구현하였습니다.
  <img width="400" height="200" src="https://user-images.githubusercontent.com/81574795/180916409-c3b03b29-6597-41aa-8c1e-2b0a88fa0c03.png">
   
    
  
  ### 🔥 선택사항
  #### migration 파일에 더미 데이터 삽입
<a align='left'>
  <img src="https://user-images.githubusercontent.com/81574795/180950620-d47fff73-e475-4466-bc38-05825784679f.png" widht="400" height="300">
</a>
<a align='right'>
  <img src="https://user-images.githubusercontent.com/81574795/180950896-cf765c19-7016-4598-8b9b-71b86fec8a95.png" widht="400" height="300">
</a>

  
  
  <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white"></a><br>
  #### 캐싱 전략
      SNS 서비스 특성상 많은 유저가 해당 게시글을 조회할 것으로 판단하였습니다.
      db의 접속을 줄이고 캐시 메모리를 이용해서 성능적인 부분을 고려해서 캐싱 전략을 사용했습니다.
      Redis Cache를 이용해서 key "(article_id) : value (user_id)"의 형태로 캐시 메모리에 저장한 다음, 
      같은 유저가 같은 게시글을 조회했을 때 의도적으로 조회수 카운트 상승을 방지하였습니다.
      
      
  #### 채팅
     미구현
     
  #### 검색 엔진
  ```
  검색 엔진으로 엘라스틱 서치를 사용하였습니다. 인덱스 색인 및 매핑 작업으로 하고 title, content, hashtags를 검색 가능하도록 설정합니다.
  그리고 로그 스태시로 mysql과 연동하게 하고, 키바나로 검색 단어를 분석 및 시각화 작업을 합니다.
  ```
  ```
  {
  "properties": {
    "id": {
      "type": "long"
    },
    "title": {
      "type": "keyword",
      "copy_to": ["title_nori"]
    },
    "title_nori": {
      "type": "text",
      "analyzer": "nori_analyzer"
    },
    "content": {
      "type": "keyword",
      "copy_to": ["content_nori"]
    },
    "content_nori": {
      "type": "text",
      "analyzer": "nori_analyzer"
    },
    "hashtags": {
      "type": "keyword",
      "copy_to": ["hashtags_nori"]
    },
    "hashtags_nori": {
      "type": "text",
      "analyzer": "nori_analyzer"
    }
  }
```
<img width="1423" alt="image" src="https://user-images.githubusercontent.com/81574795/180952148-80348f11-d0f6-4fdd-9b52-c87eba1bbd9e.png">

     

## 👀 API Doc
</details>
<details>
  <summary>2. 로그인</summary>
  
  ```
  💬 [POST] 로그인
  /user/login/
  ```
  - Request
    ```
    {
    "email": string",
    "password": string
    }

    ```
  - Response 200
    ```
    SUCCESS {
    "message": "로그인 되었습니다. 반갑습니다 {user.email}님",
    "token": {
      "user": 2,
      "access_token": string,
      "refresh_token": string
      }
    }
    ```
</details>

<details>
  <summary>2. 회원가입 </summary>
  
  ```
  💬 [POST] 회원가입
  /user/register/
  ```
  - Request
    ```
    {
    "email": email,
    "password1": string,
    "password2": string,
    "username": string
    }
    ```
  - Response 201
    ```
    SUCCESS {
    "message": "회원가입 되었습니다. 반갑습니다 user2@email.com님",
    "user": int
    }
    ```
</details>

<details>
  <summary>3. 유저 조회 및 수정, 삭제 </summary>
  
  ```
  💬 [GET] 상세 조회
  /user/{user_id}/
  ```
  - Request
    ```
    {
      "user_id": 1
    }

    ```
  - Response
    ```
    {
    "id": 1,
    "email": "admin@email.com",
    "username": "admin",
    "gender": "",
    "follower": 0,
    "followee": 0,
    "reg_date": "2022-07-26T10:11:50.507286+09:00",
    "update_date": "2022-07-26T10:11:50.507302+09:00",
    "last_login": null
    }
    ```
  ```
  💬 [PATCH] 부분 수정
  /user/{user_id}/
  ```
  - Request
    ```
    {
      "username": "string",
      "gender": "M"
    }
    ```
  - Response  200
    ```
    {
      "id": 2
      "username": "string",
      "gender": "M"
    }
    ```
  ```
  💬 [DELETE] 삭제
  /user/{user_id}/
  ```
  - Request
    ```
    {
      "user_id": 2
    }

    ```
  - Response  204
    ```
    {
    }
    ```
</details>
<details>
  <summary>4. 팔로우 </summary>
  
  ```
  💬 [POST] 팔로우 및 언팔로우
  /user/{user_id}/follow/
  ```
  - Request
    ```
    {
    }
    ```
  - Response 201
    ```
    {
    }
    ```
</details>

<br/>

</details>
<details>
  <summary>5. 게시글 리스트 조회 </summary>
  
  ```
  💬 [GET] 게시글 리스트 조회
  /article/
  ```
  - Request
    ```
    {
    }
    ```
  - Response 201
    ```
    {
      "count": 2,
      "next": null,
      "previous": null,
      "results": [
        {
          "user": "user2@email.com",
          "id": 2,
          "title": "잠실 맛집",
          "hashtags": "#맛집, #밥집, #좋반, #갬성",
          "content": "일단 맛집임 ㅇㅇ"
        },
        {
          "user": "admin@email.com",
          "id": 1,
          "title": "서울 분위기 좋은 카페 추천해줌",
          "hashtags": "#맛집, #카페, #좋아요반사",
          "content": "감성지면 개추"
        }
      ]
    }
    ```
    
   ```
  💬 [GET] 게시글 searching, filtering, pagination, ordering 조회 (동시 적용 가능!)
  /article/?page=1&page_size=1&hashtags=밥집&search=잠실&orderby=-created_at
  ```
  - Request
    ```
    {
    }
    ```
  - Response 201
    ```
    {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
        {
          "user": "user2@email.com",
          "id": 2,
          "title": "잠실 맛집",
          "hashtags": "#맛집, #밥집, #좋반, #갬성",
          "content": "일단 맛집임 ㅇㅇ"
        }
      ]
    }
    ```
</details>

<details>
  <summary>6. 게시글 생성 </summary>
  
  ```
  💬 [POST] 게시글 생성
  /article/
  ```
  - Request
    ```
    {
      "title": "테스트 게시글",
      "hashtags": "#테스트, #이게뭐지",
      "content": "아무튼 테스트임"
    }
    ```
  - Response 201
    ```
    {
      "user": "user2@email.com",
      "id": 3,
      "title": "테스트 게시글",
      "hashtags": "#테스트, #이게뭐지",
      "content": "아무튼 테스트임"
    }
    ```
</details>

<details>
  <summary>7. 게시글 상세 조회 및 수정, 삭제 </summary>
  
  ```
  💬 [POST] 게시글 상세 조회
  /article/{article_id}/
  ```
  - Request
    ```
    {
    }
    ```
  - Response 200
    ```
    {
      "id": 3,
      "title": "테스트 게시글",
      "content": "아무튼 테스트임",
      "hashtags": "#테스트, #이게뭐지",
      "hits": 1,
      "like_count": 0,
      "delete_date": null,
      "comments": [
        {
          "id": 1,
          "article": 3,
          "user": "user2",
          "content": "테스트 댓글임",
          "created_at": "2022-07-26T11:17:51.661538+09:00",
          "re_comments": []
        }
      ]
    }
    ```
  ```
  💬 [POST] 게시글 수정
  /article/{article_id}/
  ```
  - Request
    ```
    {
      "title": "테스트 게시글 수정해보기"
    }
    ```
  - Response 200
    ```
    {
      "title": "테스트 게시글 수정해보기",
      "hashtags": "#테스트, #이게뭐지",
      "content": "아무튼 테스트임"
    }
    ```
  ```
  💬 [POST] 게시글 삭제
  /article/{article_id}/
  ```
  - Request (path parm : article_id)
    ```
    {
    "article_id": 3
    }
    ```
  - Response 204
    ```
    {
    }
    ```
</details>

<details>
  <summary>8. 게시글 좋아요 </summary>
  
  ```
  💬 [POST] 게시글 좋아요
  /article/{article_id}/like
  ```
  - Request (path param : article_id)
    ```
    {
    }
    ```
  - Response 200
    ```
    {
    "message": "좋아요 했습니다."
    }
    ```
</details>

<details>
  <summary>8. 게시글 소프트 딜리트 </summary>
  
  ```
  💬 [GET] 게시글 소프트 딜리트 전체 조회
  /article/delete/
  ```
  - Request
    ```
    {
    }
    ```
  - Response 200
    ```
    {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
        {
          "id": 3,
          "title": "테스트 게시글",
          "hashtags": "#테스트, #이게뭐지",
          "user": {
            "id": 2,
            "email": "user2@email.com",
            "username": "user2"
          },
          "delete_date": "2022-07-26T11:51:31.466405+09:00"
        }
      ]
    }
    ```
  ```
  💬 [GET] 게시글 소프트 딜리트 상세 조회
  /article/delete/{article_id}/
  ```
  - Request (path param : article_id)
    ```
    {
    }
    ```
  - Response 200
    ```
    {
      "id": 3,
      "title": "테스트 게시글",
      "hashtags": "#테스트, #이게뭐지",
      "user": {
        "id": 2,
        "email": "user2@email.com",
        "username": "user2"
      },
      "delete_date": "2022-07-26T11:51:31.466405+09:00"
    }
    ```
  ```
  💬 [PATCH] 게시글 복원
  /article/delete/{article_id}/
  ```
  - Request (path param : article_id)
    ```
    {
    }
    ```
  - Response 200
    ```
    {
      "message": "복원되었습니다"
    }
    ```
</details>

<br/>

<details>
  <summary>9. 댓글 리스트 조회 </summary>
  
  ```
  💬 [GET] 댓글 리스트 조회
  /comment/
  ```
  - Request
    ```
    {
    }
    ```
  - Response 200
    ```
    {
      "id": 1,
      "article": 3,
      "user": "user2",
      "content": "테스트 댓글임",
      "created_at": "2022-07-26T11:17:51.661538+09:00",
      "re_comments": []
    }
    ```
</details>

<details>
  <summary>10. 댓글 생성 </summary>
  
  ```
  💬 [POST] 댓글 생성
  /comment/{article_id}/comment/
  ```
  - Request (path param : article_id)
    ```
    {
      "content": "테스트 댓글임"
    }
    ```
  - Response 201
    ```
    {
      "content": "테스트 댓글임",
      "user": "user2@email.com",
      "article": "테스트 게시글"
    }
    ```
</details>


<details>
  <summary>11. 댓글 수정 및 삭제 </summary>
  
  ```
  💬 [PATCH] 댓글 부분 수정
  /comment/{comment_id}/
  ```
  - Request (path param : comment_id)
    ```
    {
      "content": "테스트 댓글 수정임"
    }
    ```
  - Response 201
    ```
    {
      "id": 1
      "content": "테스트 댓글 수정임"
    }
    ```
  ```
  💬 [DELETE] 댓글 삭제
  /comment/{comment_id}/
  ```
  - Request (path param : comment_id)
    ```
    {
    }
    ```
  - Response 204
    ```
    {
    }
    ```
</details>

<details>
  <summary>12. 대댓글 조회 및 생성 </summary>
  
  ```
  💬 [GET] 대댓글 상세 조회
  /comment/{comment_id}/recomment/
  ```
  - Request (path param : comment_id)
    ```
    {
      "comment_id": 1
    }
    ```
  - Response 200
    ```
    {
       "id": 1,
       "content": "테스트 대댓글임",
       "created_at": "2022-07-26T11:35:07.693475+09:00",
       "user": "user3",
       "comment": 1
     }
    ```
  ```
  💬 [POST] 대댓글 생성
  /comment/{comment_id}/recomment/
  ```
  - Request (path param : comment_id)
    ```
    {
      "content": "테스트 대댓글임"
    }
    ```
  - Response 201
    ```
    {
      "content": "테스트 대댓글임",
      "user": "user3",
      "comment": 1
    }
    ```
</details>

<details>
  <summary>13. 대댓글 수정 및 삭제 </summary>
  
  ```
  💬 [PATCH] 대댓글 수정
  /comment/recomment/{recomment_id}/
  ```
  - Request (path param : comment_id)
    ```
    {
      "content": "대댓글 부분수정"
    }
    ```
  - Response 200
    ```
    {
      "content": "대댓글 부분수정"
    }
    ```
  ```
  💬 [DELETE] 대댓글 삭제
  /comment/recomment/{recomment_id}/
  ```
  - Request (path param : comment_id)
    ```
    {
    }
    ```
  - Response 204
    ```
    {
    }
    ```
</details>

<br/>
<br/>

## 실행 방법

```
📌 Dependency

# 로컬에서 바로 서버 구동
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# 도커 실행 (prod branch)
pip install docker
pip install docker-compose
docker-compose up -d

(장고 서버는 15초 대기 시간을 걸었습니다.)
```

<br/>

## 🔥 배포

docker를 이용해 프로젝트 api를 컨테이너화 하여 GCP에 배포했습니다  

[API Link]()

GCP 배포, 테스트 및 동작을 확인하였으며, 비용 등의 이유로 현재는 접속불가할 수 있습니다.
<br><br>



## swagger

[API 명세서 (Swagger)]()

<br><br>
