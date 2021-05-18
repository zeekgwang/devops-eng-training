[![build-and-test](https://github.com/zeekgwang/devops-eng-training/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/zeekgwang/devops-eng-training/actions/workflows/main.yml)

# devops-eng-training
## devops-eng-training
### DevOps 연습 repo
* flask로 간단한 사칙연산 웹 페이지 구현
* pytest를 사용한 unittest, integration test 구현
* github action을 사용한 build and test 자동화
* git flow 실습
* Dockerfile을 사용한 이미지 생성 실습



### Running without Docker
#### Local
* Local 환경은 python=3.9.2 가정
```
git clone https://github.com/zeekgwang/devops-eng-training.git
cd devops-eng-training
pip install -r requirements.txt
```    
* pytest
```
pytest unittest
pytest integration
```    
* run
```
python app.py
```

### Running with Docker
#### Docker
* docker 빌드
```
#docker build . -t {이미지 이름}:{이미지 태그}
docker build . -t devops:0.1
```		
* run
```
#docer run --name {Assgin될 이름} -p {들어오는 포트}:{연결되는 포트} {이미지 정보}
docker run --name devops -p 5000:8080 devops:0.1
```
